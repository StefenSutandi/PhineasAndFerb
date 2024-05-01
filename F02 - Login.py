class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

def find_user_by_username(username):
    # Dummy implementation to find user by username
    for user in users:
        if user.username == username:
            return user
    return None

def login():
    global current_user
    
    if current_user:
        print("Login gagal!")
        print(f"Anda telah login dengan username {current_user.username}, silahkan lakukan 'LOGOUT' sebelum melakukan login kembali.")
        return
    
    while True:
        username = input("Username: ")
        user = find_user_by_username(username)
        
        if not user:
            print("Username tidak terdaftar!")
            continue
        
        password = input("Password: ")
        
        if user.password == password:
            if user.role == "Agent" or user.role == "Admin":
                print(f"Selamat datang, {user.username}!")
                print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
                current_user = user  # Assign current_user after successful login
                break
        else:
            print("Password salah!")

# List of dummy users (for demonstration)
users = [
    User("Purry", "pl@tYPu5", "Agent"),
    User("Admin123", "adminpass", "Admin")
]

# Global variable to track current logged in user
current_user = None

# Main loop for user interactions
while True:
    command = input("\n>>> LOGIN\n")
    if command.strip().upper() == "LOGIN":
        login()
    else:
        print("Command tidak valid. Silahkan masukkan command 'LOGIN'.")
