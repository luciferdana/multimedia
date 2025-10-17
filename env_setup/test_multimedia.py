#!/usr/bin/env python3
"""
Script verifikasi instalasi library multimedia
Worksheet 1: Setup Python Environment untuk Multimedia
Nama: Ferdana Al-Hakim (122140012)
"""

import sys
import importlib

def test_import(module_name, description=""):
    """Test import library dan tampilkan versi jika ada"""
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, '__version__', 'Unknown version')
        print(f"[OK] {module_name:<20} - {version:<15} - {description}")
        return True
    except ImportError as e:
        print(f"[FAIL] {module_name:<20} - GAGAL IMPORT - {e}")
        return False
    except Exception as e:
        print(f"[ERROR] {module_name:<20} - ERROR - {e}")
        return False

def main():
    print("=" * 80)
    print("VERIFIKASI INSTALASI LIBRARY MULTIMEDIA")
    print("Ferdana Al-Hakim (122140012)")
    print("=" * 80)
    
    print(f"\nPython Version: {sys.version}")
    print(f"Python Executable: {sys.executable}")
    
    # Daftar library yang perlu ditest
    libraries = [
        # Audio Processing
        ("librosa", "Audio analysis library"),
        ("soundfile", "Audio file I/O"),
        ("scipy", "Scientific computing"),
        
        # Image Processing  
        ("cv2", "OpenCV - Computer vision"),
        ("PIL", "Pillow - Image processing"),
        ("skimage", "Scikit-image - Image processing"),
        ("matplotlib", "Plotting library"),
        
        # Video Processing
        ("moviepy", "Video editing"),
        ("ffmpeg", "FFmpeg Python bindings"),
        
        # General Purpose
        ("numpy", "Numerical computing"),
        ("pandas", "Data analysis"),
        ("jupyter", "Jupyter notebook"),
        
        # Additional useful libraries
        ("IPython", "Interactive Python"),
        ("matplotlib.pyplot", "Matplotlib plotting interface")
    ]
    
    print("\n" + "=" * 80)
    print("HASIL VERIFIKASI LIBRARY:")
    print("=" * 80)
    
    success_count = 0
    total_count = len(libraries)
    
    for module_name, description in libraries:
        if test_import(module_name, description):
            success_count += 1
    
    print("\n" + "=" * 80)
    print("SUMMARY:")
    print("=" * 80)
    print(f"Total libraries tested: {total_count}")
    print(f"Successfully imported: {success_count}")
    print(f"Failed to import: {total_count - success_count}")
    print(f"Success rate: {(success_count/total_count)*100:.1f}%")
    
    if success_count == total_count:
        print("\n[SUCCESS] SEMUA LIBRARY BERHASIL DIIMPORT!")
        print("Environment multimedia siap digunakan!")
    else:
        print(f"\n[WARNING] {total_count - success_count} library gagal diimport.")
        print("Periksa instalasi library yang gagal.")
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()