# F14 - Load

import argparse
import os

def load_data_from_folder(folder_name):
    try:
        if not os.path.exists(folder_name):
            raise FileNotFoundError(f"Folder '{folder_name}' tidak ditemukan.")
        
        # Implementasi proses memuat data dari folder
        print("Loading...")
        # Panggil fungsi atau prosedur untuk memuat data dari folder
        
        print("Selamat datang di program OWCA!")
        return True

    except FileNotFoundError as e:
        print(e)
        return False

def main():
    parser = argparse.ArgumentParser(description='Program untuk memuat data dari folder eksternal')
    parser.add_argument('folder', type=str, nargs='?', default=None, help='Nama folder yang berisi file penyimpanan')

    args = parser.parse_args()

    if not args.folder:
        print("Tidak ada nama folder yang diberikan!")
        print("Usage: python main.py <nama_folder>")
        return

    if not load_data_from_folder(args.folder):
        return

    # Lanjutkan dengan logika program selanjutnya

if __name__ == "__main__":
    main()
