# F01 - Register
import csv

class Agent:
    def __init__(self, username, password, monster):
        self.username = username
        self.password = password
        self.role = "agent"
        self.owca_coins = 0
        self.monster = monster

class Monster:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def load_monsters_from_file(filename):
    monsters = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            name, description = row
            monsters.append(Monster(name, description))
    return monsters

def register_agent():
    # Load monsters from CSV file
    monsters = load_monsters_from_file('monsters.csv')

    # Check if user is already logged in
    if current_user:
        print("Register gagal!")
        print(f"Anda telah login dengan username {current_user.username}, silahkan lakukan 'LOGOUT' sebelum melakukan register.")
        return

    # Get user input for username and password
    while True:
        username = input("Masukkan username: ")
        if not is_valid_username(username):
            print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
        elif find_agent_by_username(username):
            print("Username sudah terpakai, silahkan gunakan username lain!")
        else:
            break

    password = input("Masukkan password: ")

    # Display available monsters for selection
    print("\nSilahkan pilih salah satu monster sebagai monster awalmu:")
    for i, monster in enumerate(monsters, start=1):
        print(f"{i}. {monster.name}")

    # Prompt user to choose a monster
    while True:
        try:
            choice = int(input("Monster pilihanmu: "))
            if 1 <= choice <= len(monsters):
                selected_monster = monsters[choice - 1]
                break
            else:
                print("Pilihan tidak valid. Silahkan pilih nomor monster yang tersedia.")
        except ValueError:
            print("Input tidak valid. Masukkan nomor pilihan monster.")

    # Create and register the new agent
    new_agent = Agent(username, password, selected_monster)
    agents.append(new_agent)
    print(f"Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {selected_monster.name}!")

def is_valid_username(username):
    # Check if username contains only allowed characters
    return all(c.isalnum() or c == '_' or c == '-' for c in username)

def find_agent_by_username(username):
    # Check if username is already registered
    return any(agent.username == username for agent in agents)

# Main program
agents = []
current_user = None  # Track currently logged in user

# Main loop for user interactions
while True:
    print("\n>>> REGISTER")
    register_agent()
