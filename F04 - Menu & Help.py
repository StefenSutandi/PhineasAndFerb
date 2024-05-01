# F04 - Menu & Help

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

def help_before_login():
    """Fungsi untuk menampilkan bantuan sebelum login."""
    print("=========== HELP ===========")
    print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
    print("1. Login: Masuk ke dalam akun yang sudah terdaftar")
    print("2. Register: Membuat akun baru")
    print("\nFootnote:")
    print("1. Untuk menggunakan aplikasi, masukkan nama fungsi yang terdaftar")
    print("2. Pastikan memasukkan input yang valid")

def help_after_login(role, username):
    """Fungsi untuk menampilkan bantuan setelah login."""
    print(f"=========== HELP ===========")
    if role == "Agent":
        print(f"Halo Agent {username}. Kamu memanggil command HELP.")
        print("Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
        print("1. Logout: Keluar dari akun yang sedang digunakan")
        print("2. Monster: Melihat owca-dex yang dimiliki oleh Agent")
        # Tambahkan opsi lain yang dapat dilakukan oleh Agent
    elif role == "Admin":
        print(f"Selamat datang, Admin {username}.")
        print("Berikut adalah hal-hal yang dapat kamu lakukan:")
        print("1. Logout: Keluar dari akun yang sedang digunakan")
        print("2. Shop: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent")
        # Tambahkan opsi lain yang dapat dilakukan oleh Admin
    print("\nFootnote:")
    print("1. Untuk menggunakan aplikasi, masukkan nama fungsi yang terdaftar")
    print("2. Pastikan memasukkan input yang valid")

# Dummy list of users (for demonstration)
users = [
    User("Purry", "pl@tYPu5", "Agent"),
    User("Admin123", "adminpass", "Admin")
]

# Main program logic
def main():
    current_user = None

    while True:
        command = input("\n>>> ").strip().upper()

        if command == "LOGIN":
            # Implementasi login disini
            continue
        elif command == "REGISTER":
            # Implementasi register disini
            continue
        elif command == "HELP":
            if current_user is None:
                help_before_login()
            else:
                # Cari user yang sedang login
                user = next((u for u in users if u.username == current_user), None)
                if user:
                    help_after_login(user.role, user.username)
                else:
                    print("User tidak ditemukan.")
        else:
            print("Command tidak valid. Silakan masukkan command 'LOGIN', 'REGISTER', atau 'HELP'.")

if __name__ == "__main__":
    main()