# F00 - Random Number Generator

class LCG:
    def __init__(self, seed, a, c, m):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def next_random(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def random_range(self, start, end):
        random_number = self.next_random()
        scaled = start + (random_number % (end - start))
        return scaled


# Eksekusi:
if __name__ == "__main__":
    class Agent:
        def __init__(self, username, password, role, oc):
            self.username = username
            self.password = password
            self.role = role
            self.oc = oc
    
    def is_valid_username(username):
        allowed_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-")
        return all(char in allowed_characters for char in username)
    
    def register_agent():
        # Pendaftaran akun baru
        print(">>> REGISTER")
        username = input("Masukkan username: ")
        
        while not is_valid_username(username):
            print("Username hanya boleh berisi huruf, angka, underscore (_), dan strip (-).")
            username = input("Masukkan username: ")
        
        password = input("Masukkan password: ")
        role = "agent"
        oc = 0
        
        # Buat objek Agent baru
        new_agent = Agent(username, password, role, oc)
        
        print(f"Selamat datang Agent {username}!")
        return new_agent


    # Fungsi untuk memuat data monster dari file CSV
    def load_monsters(filename):
        monsters = []
        with open(filename, 'r') as file:
            next(file)  # Skip header
            for line in file:
                data = line.strip().split(';')
                monster_id = int(data[0])
                type = data[1]
                atk_power = int(data[2])
                def_power = int(data[3])
                hp = int(data[4])
                monster = {
                    'id': monster_id,
                    'type': type,
                    'atk_power': atk_power,
                    'def_power': def_power,
                    'hp': hp
                }
                monsters.append(monster)
        return monsters


    # Penggunaan untuk CSV
    monster_file = "monsters.csv"
    monsters_data = load_monsters(monster_file)

    print("Daftar Monster:")
    for monster in monsters_data:
        print(f"{monster['id']}. {monster['type']} (ATK: {monster['atk_power']}, DEF: {monster['def_power']}, HP: {monster['hp']})")

    # Penggunaan RNG untuk memilih monster secara acak
    rng = LCG(seed=123, a=1103515245, c=12345, m=2**31)
    random_monster_id = rng.random_range(1, len(monsters_data) + 1)

    selected_monster = None
    for monster in monsters_data:
        if monster['id'] == random_monster_id:
            selected_monster = monster
            break

    if selected_monster:
        print(f"Monster yang dipilih secara acak: {selected_monster['type']}")
    else:
        print("Tidak ada monster yang dipilih.")

