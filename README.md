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

### Video Processing:
- Frame extraction dengan temporal sampling
- Metadata analysis (fps, resolution, duration, frame count)
- BGR to RGB conversion untuk proper visualization
- Video classification berdasarkan resolusi (HD, Full HD, 4K)

### Output Files Generated:
- Resampled audio files dengan sample rate berbeda
- Filtered audio dengan berbagai jenis filter
- Pitch-shifted audio untuk sound effects
- Remixed music dengan tempo dan key matching
- Test visualization outputs untuk environment verification

---



## License & References

**Academic Use Only** - Tugas Kuliah Sistem Teknologi Multimedia

**References:**
- Librosa Documentation: https://librosa.org/
- OpenCV Documentation: https://opencv.org/
- Matplotlib Documentation: https://matplotlib.org/
- NumPy Documentation: https://numpy.org/

---