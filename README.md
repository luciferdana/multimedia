# Sistem Teknologi Multimedia - Repository

**Mata Kuliah:** Sistem & Teknologi Multimedia  
**Nama:** Ferdana Al-Hakim  
**NIM:** 122140012  

---

## Struktur Repository

Repository ini berisi implementasi dan analisis multimedia mencakup audio, gambar, dan video processing menggunakan Python. Struktur lengkap repository:

```
Sistem Teknologi Multimedia/
├── ho_audio/                           # Audio Processing & Analysis
│   └── 122140012_AudioExercise.ipynb  # Notebook audio processing lengkap
├── env_setup/                          # Environment Setup & Testing
│   ├── requirements.txt                # Dependencies list
│   ├── test_audio_simple.py           # Audio testing script
│   ├── test_image_simple.py           # Image testing script
│   ├── test_multimedia.py             # Comprehensive testing
│   ├── sine_wave_test.png             # Output test audio
│   ├── test_image.png                 # Output test image
│   └── figure/                        # Test visualization outputs
│       ├── env.png
│       ├── Figure_1.png
│       └── ifitera-header.png
├── Worksheet_2/                        # Multimedia Analysis Worksheet
│   ├── 122140012_Worksheet2.ipynb     # Worksheet notebook
│   └── 122140012_Worksheet2.pdf       # PDF export hasil analisis
├── worksheet_4/                        # Image Processing Worksheet
│   ├── 122140012_worksheet4.ipynb     # Notebook image processing
│   ├── 122140012_worksheet4.pdf       # PDF export hasil
│   ├── assets_ws4/                    # Input images
│   │   ├── image1.jpg                 # Selfie untuk cropping & filter
│   │   ├── image2.jpg                 # Objek dengan tekstur
│   │   └── image3.jpg                 # Objek datar untuk perspektif
│   └── results_ws4/                   # Output hasil pemrosesan
│       ├── face_crop_920x920.png
│       ├── bg_crop_920x920.png
│       ├── soal1_comparison.png
│       ├── soal2_rgb_modified.png
│       ├── soal2_histogram_comparison.png
│       ├── soal3_edge_filter_comparison.png
│       ├── soal4_face_filter_comparison.png
│       └── soal5_perspective_correction.png
├── rppg/                               # Real-time rPPG Heart Rate Detection
│   ├── rppg_122140012.py              # Script utama deteksi detak jantung
│   ├── README.md                       # Laporan implementasi rPPG
│   └── credit.png                      # Credit AI usage
├── data/                               # Dataset & Audio Files
│   ├── audio.wav                      # Audio untuk worksheet
│   ├── Audio1.wav                     # Multi-level voice recording
│   ├── Audio2.wav                     # Noisy audio recording
│   ├── song1.wav                      # Lagu sedih (Adele)
│   ├── song2.wav                      # Lagu ceria (Pharrell)
│   ├── image.jpeg                     # Gambar untuk analisis
│   └── [processed audio files]        # Hasil pemrosesan audio
├── 122140012/                          # Audio Recording Projects
│   ├── rekaman_1/
│   ├── rekaman_2/
│   └── rekaman_3/
├── multimedia-uv/                      # Virtual Environment
│   ├── Scripts/                        # Python executables
│   ├── Lib/site-packages/             # Installed packages
│   └── [other env files]
├── README.md                           # Dokumentasi ini
└── [other project files]
```

---

## ho_audio/

**Deskripsi:** Implementasi lengkap audio processing dan analysis

**Konten:**
- `122140012_AudioExercise.ipynb` - Notebook utama untuk audio processing

**Data Input:**
- `Audio1.wav` - Multi-level voice recording (berbisik hingga berteriak)
- `Audio2.wav` - Audio dengan background noise kipas angin
- `song1.wav` - Lagu sedih (Adele - Someone Like You)
- `song2.wav` - Lagu ceria (Happy - Pharrell Williams)

**Hasil Pemrosesan Audio:**
- `Audio1_combined_pitch.wav` - Gabungan pitch shifting +7 dan +12 semitones
- `suara_resample.wav` - Audio ter-resample dari 48kHz ke 22kHz
- `suara_lowpass.wav` - Hasil low-pass filter 2000 Hz
- `suara_highpass.wav` - Hasil high-pass filter 500 Hz
- `suara_bandpass.wav` - Hasil band-pass filter 300-3000 Hz
- `remix_result.wav` - Hasil remix kedua lagu dengan tempo/key matching

**Fitur yang diimplementasikan:**
- Multi-level audio analysis (berbisik hingga berteriak)
- Noise reduction dengan filtering (High-pass, Low-pass, Band-pass)
- Pitch shifting untuk efek chipmunk (+7 dan +12 semitones)
- Audio processing chain (EQ, Compression, Normalization, Noise Gate)
- Music remix dengan tempo & key matching menggunakan crossfading

**Analisis yang dilakukan:**
- Metadata extraction (sample rate, durasi, channel count)
- Waveform visualization dan analisis amplitudo
- Spectrogram analysis dalam domain waktu-frekuensi
- Resampling comparison dan quality assessment
- Filter effectiveness evaluation untuk noise reduction
- Pitch shifting impact analysis
- Professional audio processing workflow
- Music tempo detection dan key estimation

**Cara menjalankan:**
```bash
cd ho_audio
jupyter notebook 122140012_AudioExercise.ipynb
```

---

## env_setup/

**Deskripsi:** Setup environment dan testing multimedia libraries

**Konten:**
- `requirements.txt` - Dependencies yang diperlukan
- `test_audio_simple.py` - Test script untuk audio processing
- `test_image_simple.py` - Test script untuk image processing
- `test_multimedia.py` - Comprehensive multimedia testing

**Output Testing:**
- `sine_wave_test.png` - Visualisasi gelombang sinus test audio
- `test_image.png` - Hasil test image processing
- `figure/env.png` - Environment verification output
- `figure/Figure_1.png` - Test visualization result
- `figure/ifitera-header.png` - Header template untuk dokumentasi

**Fungsi Testing:**
- Audio library compatibility (librosa, soundfile)
- Image processing capabilities (PIL, OpenCV)
- Matplotlib visualization functionality
- NumPy numerical computing verification
- Environment setup validation

**Cara setup environment:**
```bash
# 1. Create virtual environment
python -m venv multimedia-uv

# 2. Activate environment (Windows PowerShell)
multimedia-uv\Scripts\Activate.ps1

# 3. Install dependencies
cd env_setup
pip install -r requirements.txt

# 4. Test installation
python test_multimedia.py
```

---

## Worksheet_2/

**Deskripsi:** Worksheet analisis multimedia komprehensif

**Konten:**
- `122140012_Worksheet2.ipynb` - Notebook worksheet multimedia analysis
- `122140012_Worksheet2.pdf` - Export PDF hasil analisis lengkap

**Data Input yang Digunakan:**
- `data/audio.wav` - File audio musik untuk analisis spektral
- `data/image.jpeg` - Gambar pemandangan alam untuk analisis RGB
- `data/video.mp4` - Video klip sorotan untuk frame extraction

**Analisis Audio (Bagian A):**
- Metadata extraction: sample rate 44.1kHz, durasi 85 detik, format mono
- Waveform analysis: pola amplitudo dinamis dengan variasi intensitas
- Spectrogram analysis: representasi waktu-frekuensi dalam skala log-dB
- MFCC extraction: 13 koefisien untuk representasi perceptual audio
- Interpretasi: karakteristik musik dengan dinamika beragam dan struktur spektral kompleks

**Analisis Gambar (Bagian B):**
- Format: RGB dengan dimensi 1128x736 pixels, 3 channels, dtype uint8
- Ukuran memori: ~2.4MB untuk pemrosesan
- Histogram RGB: distribusi intensitas per channel dengan kontras baik
- Analisis visual: pemandangan dengan gradasi warna natural dan pencahayaan balanced
- Interpretasi: gambar memiliki dynamic range yang baik dengan variasi warna komprehensif

**Analisis Video (Bagian C):**
- Metadata: resolusi 1280x714, frame rate 60fps, durasi 30 detik
- Total frames: 1,800 frames dengan klasifikasi Standard Definition
- Frame extraction: awal, tengah, akhir dengan konversi BGR ke RGB
- Temporal analysis: progression visual dengan dynamic content
- Interpretasi: parameter sesuai untuk media sosial dan streaming platform

**Perbandingan Representasi Media:**
- Audio (1D temporal): amplitudo vs waktu dengan analisis spektral
- Gambar (2D spasial): matriks intensitas pixel dalam koordinat x,y
- Video (2D + temporal): sequence frame dengan parameter frame rate

**Learning Outcomes:**
- Pemahaman dimensi representasi multimedia berbeda
- Teknik visualisasi domain frekuensi vs waktu
- Importance metadata untuk preprocessing
- Interpretasi hasil analisis kontekstual

**Cara menjalankan:**
```bash
cd Worksheet_2
jupyter notebook 122140012_Worksheet2.ipynb
```

---

## worksheet_4/

**Deskripsi:** Worksheet analisis dan manipulasi citra digital komprehensif

**Konten:**
- `122140012_worksheet4.ipynb` - Notebook image processing lengkap
- `122140012_worksheet4.pdf` - Export PDF hasil analisis
- `assets_ws4/` - Folder input gambar asli
- `results_ws4/` - Folder output hasil pemrosesan

**Data Input yang Digunakan:**
- `image1.jpg` - Selfie untuk cropping, color manipulation, dan face filter
- `image2.jpg` - Objek dengan background tekstur untuk edge detection
- `image3.jpg` - Objek datar (papan peringatan) untuk koreksi perspektif

**Soal 1 - Cropping dan Konversi Warna:**
- Cropping manual area wajah (kotak persegi) dan background (persegi panjang)
- Resize hasil crop menjadi 920x920 piksel
- Konversi ke ruang warna Grayscale dan HSV
- Anotasi teks nama pada gambar dengan custom font styling
- Perbandingan visual RGB vs Grayscale vs HSV

**Soal 2 - Manipulasi Channel Warna RGB:**
- Channel manipulation: +50 intensitas Red, -30 intensitas Blue
- Clipping untuk memastikan nilai tetap dalam range 0-255
- Histogram comparison per channel (R, G, B) sebelum dan sesudah modifikasi
- Analisis pergeseran distribusi warna dan efek warm-toned

**Soal 3 - Deteksi Tepi dan Filter Citra:**
- Canny Edge Detection dengan threshold (50, 150)
- Binary thresholding dengan nilai T=130 untuk segmentasi objek
- Manual bounding box pada objek utama
- Gaussian Blur (15x15 kernel) untuk smoothing
- Sharpening filter menggunakan kernel konvolusi custom
- Perbandingan efek blur vs sharpening pada detail gambar

**Soal 4 - Deteksi Wajah dan Filter Digital Kreatif:**
- Face detection menggunakan OpenCV Haar Cascade Classifier
- Estimasi landmark wajah (forehead, nose, eyes) dari bounding box
- Creative filter overlay: Vintage Hat + Handlebar Mustache
- Drawing langsung menggunakan cv2.ellipse dan cv2.rectangle
- Proportional scaling berdasarkan ukuran wajah terdeteksi
- Perbandingan gambar asli vs hasil filter

**Soal 5 - Perspektif dan Peningkatan Kualitas Citra:**
- Perspective transformation menggunakan 4 titik manual
- Koreksi distorsi geometris dengan homography matrix
- Adaptive Thresholding (Gaussian, block_size=11, C=2)
- Otsu Thresholding untuk perbandingan
- Enhancement untuk document scanning dan OCR preprocessing

**Teknik yang Diimplementasikan:**
- Manual cropping dengan koordinat proporsional
- Color space conversion (RGB, Grayscale, HSV)
- Channel-level manipulation dengan numpy array operations
- Edge detection algorithms (Canny)
- Binary thresholding techniques (fixed & adaptive)
- Spatial filtering (Gaussian blur, custom sharpening kernel)
- Face detection dengan Haar Cascade
- Geometric drawing untuk creative filters
- Perspective transformation dengan getPerspectiveTransform
- Adaptive vs Otsu thresholding comparison

**Output Files Generated:**
- `face_crop_920x920.png` - Hasil crop wajah dengan anotasi
- `bg_crop_920x920.png` - Hasil crop background
- `soal1_comparison.png` - Perbandingan RGB, Grayscale, HSV
- `soal2_rgb_modified.png` - Gambar hasil modifikasi channel
- `soal2_histogram_comparison.png` - Histogram comparison
- `soal3_canny_edges.png` - Hasil edge detection
- `soal3_threshold.png` - Hasil binary thresholding
- `soal3_bbox.png` - Gambar dengan bounding box
- `soal3_edge_filter_comparison.png` - Grid perbandingan filter
- `soal4_filtered_face.png` - Gambar dengan creative filter
- `soal4_face_filter_comparison.png` - Perbandingan sebelum/sesudah
- `soal5_perspective.png` - Hasil koreksi perspektif
- `soal5_adaptive_thresh.png` - Adaptive thresholding output
- `soal5_otsu_thresh.png` - Otsu thresholding output
- `soal5_perspective_correction.png` - Grid semua tahap pemrosesan

**Learning Outcomes:**
- Pemahaman struktur data citra digital (pixels, channels, color spaces)
- Teknik cropping dan resizing untuk ROI extraction
- Efek konversi ruang warna pada persepsi visual
- Manipulasi channel-level untuk color grading
- Algoritma edge detection dan segmentasi
- Spatial filtering untuk blur dan sharpening
- Face detection dan landmark estimation
- Creative filter overlay dengan proportional scaling
- Geometric transformation untuk perspective correction
- Adaptive thresholding untuk varying illumination

**Cara menjalankan:**
```bash
cd worksheet_4
jupyter notebook 122140012_worksheet4.ipynb
```

---

## rppg/

**Deskripsi:** Real-time Remote Photoplethysmography (rPPG) untuk deteksi detak jantung menggunakan webcam tanpa kontak fisik

**Konten:**
- `rppg_122140012.py` - Script utama real-time heart rate detection
- `README.md` - Laporan singkat implementasi rPPG
- `credit.png` - Credit penggunaan AI

**Pustaka yang Digunakan:**
- **OpenCV (cv2)** - Antarmuka webcam, manipulasi frame, dan visualisasi overlay
- **MediaPipe** - Deteksi wajah dan 468 titik face landmarks untuk ROI extraction
- **NumPy** - Operasi numerik, perhitungan rata-rata, dan manipulasi array
- **SciPy** - Bandpass filter (Butterworth) dan FFT untuk analisis frekuensi
- **Matplotlib** - Visualisasi grafik sinyal secara real-time

**Metode Implementasi:**
- **Video Capture:** Webcam 30 FPS dengan resolusi 640x480
- **Face Detection:** MediaPipe Face Mesh untuk landmark wajah presisi
- **ROI Extraction:** Area dahi sebagai Region of Interest (kulit tipis, pembuluh darah dekat permukaan)
- **Signal Extraction:** Rata-rata intensitas Green Channel (~540nm wavelength)
- **Signal Processing:** Sliding window buffer 300 sampel (10 detik × 30 FPS)
- **Filtering:** Bandpass filter 0.67-4.0 Hz (setara 40-240 BPM)
- **BPM Estimation:** FFT untuk mencari frekuensi dominan, konversi ke BPM

**Fitur yang Diimplementasikan:**
- Real-time heart rate detection tanpa kontak fisik
- MediaPipe Face Mesh dengan 468 landmark points untuk ROI akurat
- Green channel extraction untuk respons optimal terhadap perubahan aliran darah
- Butterworth bandpass filtering untuk isolasi sinyal detak jantung
- FFT-based frequency estimation untuk BPM calculation
- BPM smoothing dengan moving average window
- Real-time visualization: Raw Signal, Filtered Signal, Power Spectrum
- Webcam overlay dengan BPM display dan buffer progress

**Aspek Pembeda dengan Demo di Kelas:**
- Visualisasi grafik sinyal real-time dalam window terpisah (3 subplot)
- ROI pada area dahi tengah (lebih optimal daripada seluruh wajah)
- Stabilitas tracking menggunakan MediaPipe Face Mesh
- BPM smoothing untuk hasil yang lebih stabil

**Konfigurasi Parameter:**
```python
FPS = 30                    # Frame rate webcam
WINDOW_SIZE = 10            # Buffer size dalam detik
BUFFER_SIZE = 300           # Total sampel (FPS × WINDOW_SIZE)
MIN_HR_BPM = 40             # Minimum heart rate
MAX_HR_BPM = 240            # Maximum heart rate
PLOT_UPDATE_INTERVAL = 30   # Update grafik setiap N frame
BPM_SMOOTHING_WINDOW = 5    # Window untuk smoothing BPM
```

**Cara menjalankan:**
```bash
cd rppg
python rppg_122140012.py

# Instructions:
# 1. Posisikan wajah di depan kamera
# 2. Tunggu buffer mencapai 100%
# 3. Tekan 'q' untuk keluar
```

**Requirements Tambahan:**
```bash
pip install mediapipe
```

---

## Quick Start

### Prerequisites
- Python 3.8+
- Jupyter Notebook
- Virtual environment (recommended)

### Installation Steps

1. **Clone/Download repository**
   ```bash
   git clone <repository-url>
   cd "Sistem Teknologi Multimedia"
   ```

2. **Setup Environment**
   ```bash
   python -m venv multimedia-uv
   multimedia-uv\Scripts\Activate.ps1  # Windows PowerShell
   pip install -r env_setup\requirements.txt
   ```

3. **Test Installation**
   ```bash
   cd env_setup
   python test_multimedia.py
   ```

4. **Run Notebooks**
   ```bash
   jupyter notebook
   # Pilih notebook yang ingin dijalankan
   ```

---

## Dependencies

**Core Libraries:**
- `numpy` - Numerical computing
- `matplotlib` - Plotting and visualization
- `librosa` - Audio analysis
- `soundfile` - Audio I/O
- `opencv-python` - Computer vision
- `PIL/Pillow` - Image processing
- `jupyter` - Interactive notebooks
- `mediapipe` - Face detection dan landmark (untuk rPPG)
- `scipy` - Signal processing dan FFT (untuk rPPG)

**Full list:** Lihat `env_setup/requirements.txt`

---

## Data Requirements

Untuk menjalankan semua notebook, pastikan Anda memiliki folder `data/` dengan:

```
data/
├── audio.wav          # Audio untuk worksheet analysis
├── Audio1.wav         # Multi-level voice recording
├── Audio2.wav         # Noisy audio recording
├── song1.wav          # Lagu sedih (Adele - Someone Like You)
├── song2.wav          # Lagu ceria (Happy - Pharrell Williams)
├── image.jpeg         # Gambar pemandangan untuk analisis
├── video.mp4          # Video klip untuk frame extraction
└── [processed files]  # Output hasil pemrosesan audio
    ├── Audio1_combined_pitch.wav
    ├── suara_resample.wav
    ├── suara_bandpass.wav
    ├── suara_highpass.wav
    ├── suara_lowpass.wav
    └── remix_result.wav
```

---

## Cara Menggunakan

### 1. Audio Processing (ho_audio)
```bash
# Jalankan notebook audio processing
cd ho_audio
jupyter notebook 122140012_AudioExercise.ipynb

# Follow workflow secara sequential:
# Soal 1: Multi-level analysis → metadata, waveform, spectrogram, resampling
# Soal 2: Noise reduction → filtering dengan high-pass, low-pass, band-pass
# Soal 3: Pitch shifting → efek chipmunk +7 dan +12 semitones
# Soal 4: Processing chain → EQ, gain, normalization, compression, noise gate
# Soal 5: Music remix → tempo matching, key matching, crossfading
```

### 2. Environment Testing (env_setup)
```bash
# Test individual components
python test_audio_simple.py    # Test audio capabilities dengan sine wave
python test_image_simple.py    # Test image processing dengan gradient
python test_multimedia.py      # Test comprehensive semua fitur multimedia
```

### 3. Multimedia Worksheet (Worksheet_2)
```bash
# Comprehensive multimedia analysis
cd Worksheet_2
jupyter notebook 122140012_Worksheet2.ipynb

# Sections analysis:
# Bagian A: Audio Analysis (metadata, waveform, spectrogram, MFCC)
# Bagian B: Image Analysis (RGB display, metadata, histogram RGB)
# Bagian C: Video Analysis (metadata, frame extraction awal-tengah-akhir)
# Perbandingan representasi multimedia dan learning outcomes
```

### 4. Image Processing Worksheet (worksheet_4)
```bash
# Comprehensive digital image analysis dan manipulation
cd worksheet_4
jupyter notebook 122140012_worksheet4.ipynb

# Sections processing:
# Soal 1: Cropping manual (wajah + background) dan konversi warna (RGB, Grayscale, HSV)
# Soal 2: Manipulasi channel RGB (+50 Red, -30 Blue) dengan histogram comparison
# Soal 3: Edge detection (Canny), thresholding, bounding box, blur vs sharpening
# Soal 4: Face detection dengan Haar Cascade dan creative filter overlay
# Soal 5: Perspective correction dan adaptive/Otsu thresholding comparison
```

### 5. Real-time rPPG Heart Rate Detection (rppg)
```bash
# Jalankan script rPPG untuk deteksi detak jantung real-time
cd rppg
python rppg_122140012.py

# Workflow program:
# 1. Webcam capture pada 30 FPS dengan resolusi 640x480
# 2. Face detection menggunakan MediaPipe Face Mesh (468 landmarks)
# 3. ROI extraction pada area dahi untuk signal extraction
# 4. Green channel mean extraction dari ROI
# 5. Buffer sliding window 300 sampel (10 detik × 30 FPS)
# 6. Bandpass filtering (0.67-4.0 Hz = 40-240 BPM)
# 7. FFT untuk estimasi frekuensi dominan → konversi ke BPM
# 8. Real-time visualization (Raw Signal, Filtered, Spectrum)

# Instructions:
# - Posisikan wajah di depan kamera dengan pencahayaan baik
# - Tunggu buffer mencapai 100% untuk hasil akurat
# - Tekan 'q' untuk keluar dari program
```

---

## Features & Capabilities

### Audio Processing:
- Multi-level intensity analysis (berbisik hingga berteriak)
- Noise reduction filtering (high-pass, low-pass, band-pass)
- Spectral analysis (STFT, Spectrogram dalam log-dB scale)
- Feature extraction (MFCC 13 koefisien)
- Pitch shifting effects (+7 dan +12 semitones untuk chipmunk effect)
- Professional audio processing chain (EQ, gain, fade, compression, noise gate)
- Music tempo & key detection menggunakan librosa
- Audio remix dengan crossfading dan time stretching

### Image Processing:
- RGB format handling dengan konversi BGR ke RGB
- Metadata extraction (dimensi, channels, dtype, memory usage)
- Color histogram analysis untuk setiap channel RGB
- Visual quality assessment berdasarkan distribusi intensitas
- Manual cropping untuk ROI extraction (wajah dan background)
- Color space conversion (RGB, Grayscale, HSV)
- Channel-level manipulation dan color grading
- Edge detection dengan Canny algorithm
- Binary thresholding (fixed dan adaptive)
- Spatial filtering (Gaussian blur, custom sharpening kernel)
- Face detection menggunakan Haar Cascade Classifier
- Creative filter overlay dengan geometric drawing (ellipse, rectangle)
- Perspective transformation dan homography
- Otsu thresholding untuk automatic threshold selection
- Document scanning enhancement dan preprocessing

### Video Processing:
- Frame extraction dengan temporal sampling
- Metadata analysis (fps, resolution, duration, frame count)
- BGR to RGB conversion untuk proper visualization
- Video classification berdasarkan resolusi (HD, Full HD, 4K)

### rPPG Heart Rate Detection:
- Real-time heart rate detection tanpa kontak fisik menggunakan webcam
- Face detection dengan MediaPipe Face Mesh (468 landmark points)
- ROI extraction pada area dahi (kulit tipis, pembuluh darah dekat permukaan)
- Green channel signal extraction (~540nm wavelength optimal untuk hemoglobin)
- Sliding window buffer untuk continuous signal processing
- Butterworth bandpass filtering (0.67-4.0 Hz = 40-240 BPM range)
- FFT-based frequency analysis untuk estimasi BPM
- BPM smoothing dengan moving average window
- Real-time 3-panel visualization (Raw Signal, Filtered Signal, Power Spectrum)
- Webcam overlay dengan BPM display dan buffer progress indicator

### Output Files Generated:
- Resampled audio files dengan sample rate berbeda
- Filtered audio dengan berbagai jenis filter
- Pitch-shifted audio untuk sound effects
- Remixed music dengan tempo dan key matching
- Cropped images (face dan background) dengan resize 920x920
- RGB modified images dengan channel manipulation
- Edge detection dan thresholding results
- Face filtered images dengan creative overlay
- Perspective corrected images untuk document scanning
- Histogram comparisons dan visual analysis grids
- Test visualization outputs untuk environment verification

---

## License & References

**Academic Use Only** - Tugas Kuliah Sistem Teknologi Multimedia

**References:**
- Librosa Documentation: https://librosa.org/
- OpenCV Documentation: https://opencv.org/
- Matplotlib Documentation: https://matplotlib.org/
- NumPy Documentation: https://numpy.org/
- MediaPipe Documentation: https://mediapipe.dev/
- SciPy Documentation: https://scipy.org/

---