# F16 - Exit

import os

def save_data(folder_name):
    save_folder = os.path.join('data', folder_name)  # Assuming 'data' as the parent save folder
    
    # Check if the folder exists
    if not os.path.exists(save_folder):
        print(f"Folder '{folder_name}' belum ada.")
        print("Membuat folder 'save'...")
        os.makedirs(save_folder, exist_ok=True)
        print(f"Membuat folder 'save/{folder_name}'...")
    else:
        print(f"Folder '{folder_name}' sudah ada.")

    # Perform save operation
    print(f"Menyimpan data di 'data/{folder_name}'...")
    # Simulate saving process (replace with actual saving logic)

def exit_program():
    try:
        response = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ").lower()
        
        if response not in ['y', 'n']:
            print("Input tidak valid. Harap masukkan 'y' atau 'n'.")
            return exit_program()  # Recursive call to prompt again
        
        if response == 'y':
            folder_name = input("Masukkan nama folder untuk menyimpan data: ")
            if not folder_name:
                print("Nama folder tidak boleh kosong!")
                return exit_program()  # Recursive call to prompt again
            
            save_data(folder_name)
        
        print("Terima kasih telah menggunakan program. Sampai jumpa!")
        exit()  # Exit the program
    
    except Exception as e:
        print(f"Error: {e}")

# Main function to run the script
def main():
    try:
        print("Agent dan Admin, apakah Anda mau keluar dari petualangan?")
        exit_program()
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
