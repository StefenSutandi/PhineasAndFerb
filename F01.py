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

def is_valid_username(username):
    valid_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-')
    return all(char in valid_characters for char in username)

def load_monsters_from_file(filename):
    monsters = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            # Buat deskripsi berdasarkan atribut-atribut yang tersedia
            type_name = row['type']
            atk_power = int(row['atk_power'])
            def_power = int(row['def_power'])
            hp = int(row['hp'])
            
            # Format deskripsi sesuai dengan atribut-atribut
            description = f"Type: {type_name}, ATK: {atk_power}, DEF: {def_power}, HP: {hp}"
            
            # Buat objek Monster dan tambahkan ke list monsters
            monster = Monster(type_name, description)
            monsters.append(monster)
    return monsters


def register_agent():
    # Load monsters from CSV file
    monsters = load_monsters_from_file('monster.csv')

    # Get user input for username and password
    while True:
        username = input("Masukan username: ")
        if not is_valid_username(username):
            print("Username hanya boleh berisi huruf, angka, underscore (_), dan strip (-).")
        else:
            break

    password = input("Masukan password: ")

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

    # Welcome message
    print(f"Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {selected_monster.name}!")

# Main program
agents = []
current_user = None  # Track currently logged in user

# Main loop for user interactions
while True:
    print("\n>>> REGISTER")
    register_agent()