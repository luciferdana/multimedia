import cv2
import numpy as np
import mediapipe as mp
from scipy import signal
from scipy.fft import fft, fftfreq
from collections import deque
import matplotlib.pyplot as plt
import time

# =============================================================================
# KONFIGURASI
# =============================================================================
FPS = 30
WINDOW_SIZE = 10
BUFFER_SIZE = int(FPS * WINDOW_SIZE)

MIN_HR_BPM = 40
MAX_HR_BPM = 240
MIN_HR_HZ = MIN_HR_BPM / 60.0
MAX_HR_HZ = MAX_HR_BPM / 60.0

PLOT_UPDATE_INTERVAL = 30
BPM_SMOOTHING_WINDOW = 5

# =============================================================================
# SIGNAL PROCESSING
# =============================================================================

def bandpass_filter(data, fps, low_freq, high_freq):
    """Apply Butterworth bandpass filter"""
    nyquist = fps / 2.0
    low = low_freq / nyquist
    high = high_freq / nyquist
    b, a = signal.butter(4, [low, high], btype='band')
    return signal.filtfilt(b, a, data)


def estimate_bpm(data, fps):
    """Estimate BPM using FFT"""
    fft_data = fft(data)
    freqs = fftfreq(len(data), 1.0/fps)

    mask = (freqs >= MIN_HR_HZ) & (freqs <= MAX_HR_HZ)
    freqs = freqs[mask]
    power = np.abs(fft_data[mask])

    if len(power) > 0:
        bpm = freqs[np.argmax(power)] * 60.0
    else:
        bpm = 0

    return bpm, freqs, power


# =============================================================================
# FACE & ROI DETECTION
# =============================================================================

def get_forehead_roi(frame, face_landmarks):
    """Extract forehead ROI mask"""
    h, w = frame.shape[:2]

    # Get landmark points
    points = [(int(lm.x * w), int(lm.y * h)) for lm in face_landmarks.landmark]

    # Forehead landmarks
    roi_idx = [10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288,
               397, 365, 379, 378, 400, 377, 152, 148, 176, 149, 150, 136,
               172, 58, 132, 93, 234, 127, 162, 21, 54, 103, 67, 109]

    roi_points = [points[i] for i in roi_idx if i < len(points)]

    if len(roi_points) < 3:
        return None, None

    # Create mask
    mask = np.zeros((h, w), dtype=np.uint8)
    cv2.fillConvexPoly(mask, np.array(roi_points, dtype=np.int32), 255)

    # Bounding box
    bbox = cv2.boundingRect(np.array(roi_points, dtype=np.int32))

    return mask, bbox


def extract_green_mean(frame, mask):
    """Extract mean green channel value from ROI"""
    if mask is None:
        return 0
    green = frame[:, :, 1]
    return np.mean(green[mask > 0])


# =============================================================================
# rPPG PROCESSOR
# =============================================================================

class rPPGProcessor:
    def __init__(self, fps=30, window_size=10, smoothing=5):
        self.fps = fps
        self.buffer_size = int(fps * window_size)
        self.signal_buffer = deque(maxlen=self.buffer_size)
        self.bpm_buffer = deque(maxlen=smoothing)
        self.current_bpm = 0
        self.filtered = None
        self.freqs = None
        self.power = None

    def add_signal(self, value):
        self.signal_buffer.append(value)

    def process(self):
        if len(self.signal_buffer) < self.buffer_size:
            return False

        # Detrend and filter
        data = np.array(self.signal_buffer)
        data = data - np.mean(data)
        self.filtered = bandpass_filter(data, self.fps, MIN_HR_HZ, MAX_HR_HZ)

        # Estimate BPM
        bpm, self.freqs, self.power = estimate_bpm(self.filtered, self.fps)

        # Smooth BPM
        if 40 <= bpm <= 240:
            self.bpm_buffer.append(bpm)

        if len(self.bpm_buffer) > 0:
            self.current_bpm = np.mean(self.bpm_buffer)

        return True

    def get_bpm(self):
        return self.current_bpm

    def get_data(self):
        return {
            'raw': np.array(self.signal_buffer),
            'filtered': self.filtered,
            'freqs': self.freqs,
            'power': self.power
        }


# =============================================================================
# VISUALIZATION
# =============================================================================

# Global figure and axes for real-time plotting
fig_plot = None
axes_plot = None
lines_plot = {}

def init_plot():
    """Initialize matplotlib figure for real-time plotting"""
    global fig_plot, axes_plot, lines_plot
    
    plt.ion()
    fig_plot, axes_plot = plt.subplots(3, 1, figsize=(8, 6))
    fig_plot.suptitle('rPPG Signal Analysis', fontsize=12, fontweight='bold')
    
    # Initialize empty lines
    lines_plot['raw'], = axes_plot[0].plot([], [], 'b-', linewidth=1)
    axes_plot[0].set_title('Raw Signal (Green Channel)', fontsize=9)
    axes_plot[0].set_ylabel('Intensity')
    axes_plot[0].grid(True, alpha=0.3)
    
    lines_plot['filtered'], = axes_plot[1].plot([], [], 'r-', linewidth=1)
    axes_plot[1].set_title('Filtered Signal', fontsize=9)
    axes_plot[1].set_ylabel('Amplitude')
    axes_plot[1].grid(True, alpha=0.3)
    
    lines_plot['spectrum'], = axes_plot[2].plot([], [], 'g-', linewidth=1)
    lines_plot['peak'] = axes_plot[2].axvline(x=0, color='r', linestyle='--', linewidth=2, visible=False)
    axes_plot[2].set_title('Frequency Spectrum', fontsize=9)
    axes_plot[2].set_xlabel('Heart Rate (BPM)')
    axes_plot[2].set_ylabel('Power')
    axes_plot[2].grid(True, alpha=0.3)
    axes_plot[2].set_xlim([MIN_HR_BPM, MAX_HR_BPM])
    
    plt.tight_layout()
    fig_plot.canvas.draw()
    fig_plot.canvas.flush_events()
    
    return fig_plot, axes_plot


def update_plot(data, bpm):
    """Update matplotlib plots in real-time (reuse existing figure)"""
    global fig_plot, axes_plot, lines_plot
    
    if fig_plot is None or not plt.fignum_exists(fig_plot.number):
        return
    
    try:
        # Update raw signal
        if data['raw'] is not None and len(data['raw']) > 0:
            x_raw = np.arange(len(data['raw']))
            lines_plot['raw'].set_data(x_raw, data['raw'])
            axes_plot[0].set_xlim(0, len(data['raw']))
            axes_plot[0].set_ylim(np.min(data['raw']) - 5, np.max(data['raw']) + 5)
        
        # Update filtered signal
        if data['filtered'] is not None and len(data['filtered']) > 0:
            x_filt = np.arange(len(data['filtered']))
            lines_plot['filtered'].set_data(x_filt, data['filtered'])
            axes_plot[1].set_xlim(0, len(data['filtered']))
            y_min, y_max = np.min(data['filtered']), np.max(data['filtered'])
            margin = max(0.1, (y_max - y_min) * 0.1)
            axes_plot[1].set_ylim(y_min - margin, y_max + margin)
        
        # Update power spectrum
        if data['freqs'] is not None and data['power'] is not None:
            bpm_freqs = data['freqs'] * 60
            lines_plot['spectrum'].set_data(bpm_freqs, data['power'])
            axes_plot[2].set_ylim(0, np.max(data['power']) * 1.1 if np.max(data['power']) > 0 else 1)
            
            # Update peak line
            if bpm > 0:
                lines_plot['peak'].set_xdata([bpm, bpm])
                lines_plot['peak'].set_visible(True)
                axes_plot[2].set_title(f'Frequency Spectrum (BPM: {bpm:.1f})', fontsize=9)
            else:
                lines_plot['peak'].set_visible(False)
        
        # Redraw canvas efficiently
        fig_plot.canvas.draw_idle()
        fig_plot.canvas.flush_events()
        
    except Exception as e:
        pass  # Ignore errors during plot update


def draw_info(frame, bpm, buffer_pct, bbox=None):
    """Draw info overlay on frame"""
    if bbox is not None:
        x, y, w, h = bbox
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Info box
    cv2.rectangle(frame, (10, 10), (250, 100), (0, 0, 0), -1)
    cv2.rectangle(frame, (10, 10), (250, 100), (255, 255, 255), 2)

    # BPM
    color = (0, 255, 0) if 40 <= bpm <= 240 else (0, 0, 255)
    text = f"BPM: {bpm:.1f}" if bpm > 0 else "BPM: --"
    cv2.putText(frame, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    # Buffer
    cv2.putText(frame, f"Buffer: {buffer_pct:.0f}%", (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    return frame


# =============================================================================
# MAIN
# =============================================================================

def run_rppg():
    """Main function"""
    print("=" * 60)
    print("Real-time rPPG System (Optimized)")
    print("Sistem Teknologi Multimedia - ITERA")
    print("=" * 60)

    # Initialize MediaPipe
    mp_face = mp.solutions.face_mesh
    face_mesh = mp_face.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    # Initialize processor
    processor = rPPGProcessor(FPS, WINDOW_SIZE, BPM_SMOOTHING_WINDOW)

    # Open webcam
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, FPS)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("ERROR: Cannot open webcam!")
        return

    print("\nInstructions:")
    print("1. Position face in front of camera")
    print("2. Wait for buffer to reach 100%")
    print("3. Press 'q' to quit")
    print("=" * 60)

    # Setup matplotlib
    init_plot()

    frame_count = 0
    start_time = time.time()

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Detect face
            results = face_mesh.process(rgb_frame)
            bbox = None

            if results.multi_face_landmarks:
                landmarks = results.multi_face_landmarks[0]
                mask, bbox = get_forehead_roi(frame, landmarks)

                if mask is not None:
                    green_mean = extract_green_mean(frame, mask)
                    processor.add_signal(green_mean)

                    if len(processor.signal_buffer) >= processor.buffer_size:
                        processor.process()

            # Draw info
            buffer_pct = (len(processor.signal_buffer) / processor.buffer_size) * 100
            bpm = processor.get_bpm()
            frame = draw_info(frame, bpm, buffer_pct, bbox)

            # Update plot every N frames
            frame_count += 1
            if frame_count % PLOT_UPDATE_INTERVAL == 0 and buffer_pct >= 100:
                data = processor.get_data()
                update_plot(data, bpm)

            # Show webcam
            cv2.imshow('rPPG Real-time', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("\nStopped by user")

    finally:
        cap.release()
        cv2.destroyAllWindows()
        plt.close('all')
        face_mesh.close()

        elapsed = time.time() - start_time
        fps = frame_count / elapsed if elapsed > 0 else 0

        print("\n" + "=" * 60)
        print("Statistics")
        print("=" * 60)
        print(f"Frames: {frame_count}")
        print(f"Duration: {elapsed:.2f}s")
        print(f"FPS: {fps:.2f}")
        print(f"Final BPM: {bpm:.1f}")
        print("=" * 60)


if __name__ == "__main__":
    run_rppg()