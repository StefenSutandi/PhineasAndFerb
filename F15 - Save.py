# F15 - Save

import os

def save_data(folder_name):
    save_folder = os.path.join('data', folder_name)  # Assuming 'data' as the parent save folder
    
    # Check if the folder exists
    if not os.path.exists(save_folder):
        print(f"Folder {folder_name} belum ada\n")
        print("Saving...\n")
        
        # Create the folder and parent save folder (if not exist)
        os.makedirs(save_folder, exist_ok=True)
        print(f"Membuat folder data/{folder_name}...\n")
        print(f"Berhasil menyimpan data di folder data/{folder_name}!")
    else:
        print(f"Folder {folder_name} sudah ada\n")
        print("Saving...\n")
        
        # Save data to the existing folder
        print(f"Berhasil menyimpan data di folder data/{folder_name}!")

# Main function to run the script
def main():
    try:
        folder_name = input("Masukkan nama folder: ")
        
        if not folder_name:
            print("Nama folder tidak boleh kosong!")
            return
        
        save_data(folder_name)
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
