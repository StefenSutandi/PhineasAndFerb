# F13 - Monster Management

import csv

class MonsterManagement:
    def __init__(self, monster_file_path):
        self.monster_file_path = monster_file_path
        self.monsters = self.load_monsters()

    def load_monsters(self):
        monsters = {}
        with open(self.monster_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                monster_id = int(row['id'])
                monster_type = row['type']
                atk_power = int(row['atk_power'])
                def_power = int(row['def_power'])
                hp = int(row['hp'])
                monsters[monster_id] = {'type': monster_type, 'atk_power': atk_power, 'def_power': def_power, 'hp': hp}
        return monsters

    def display_all_monsters(self):
        print("\n>>> Tampilkan semua Monster")
        print("ID | Type          | ATK Power | DEF Power | HP")
        for monster_id, details in self.monsters.items():
            print(f"{monster_id:<2} | {details['type']:<14} | {details['atk_power']:<10} | {details['def_power']:<10} | {details['hp']}")

    def add_new_monster(self):
        print("\n>>> Tambah Monster baru")
        while True:
            new_type = input("Masukkan Type / Nama : ").strip()
            if new_type in [monster['type'] for monster in self.monsters.values()]:
                print("Nama sudah terdaftar, coba lagi!")
                continue

            while True:
                try:
                    new_atk_power = int(input("Masukkan ATK Power : "))
                    break
                except ValueError:
                    print("Masukkan input bertipe Integer, coba lagi!")

            while True:
                try:
                    new_def_power = int(input("Masukkan DEF Power (0-50) : "))
                    if 0 <= new_def_power <= 50:
                        break
                    else:
                        print("DEF Power harus bernilai 0-50, coba lagi!")
                except ValueError:
                    print("Masukkan input bertipe Integer, coba lagi!")

            while True:
                try:
                    new_hp = int(input("Masukkan HP : "))
                    break
                except ValueError:
                    print("Masukkan input bertipe Integer, coba lagi!")

            print(f"\nType : {new_type}")
            print(f"ATK Power : {new_atk_power}")
            print(f"DEF Power : {new_def_power}")
            print(f"HP : {new_hp}")

            confirm = input(">>> Tambahkan Monster ke database (Y/N) : ").strip().lower()
            if confirm == 'y':
                new_id = max(self.monsters.keys()) + 1 if self.monsters else 1
                self.monsters[new_id] = {'type': new_type, 'atk_power': new_atk_power, 'def_power': new_def_power, 'hp': new_hp}
                self.update_monster_file()
                print("Monster baru telah ditambahkan!")
                break
            elif confirm == 'n':
                print("Monster gagal ditambahkan!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih 'Y' atau 'N'.")

    def update_monster_file(self):
        with open(self.monster_file_path, 'w', newline='') as csvfile:
            fieldnames = ['id', 'type', 'atk_power', 'def_power', 'hp']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            for monster_id, details in self.monsters.items():
                writer.writerow({'id': monster_id, 'type': details['type'], 'atk_power': details['atk_power'],
                                 'def_power': details['def_power'], 'hp': details['hp']})

    def run_monster_management(self):
        while True:
            print("\n>>> MONSTER")
            print("SELAMAT DATANG DI DATABASE PARA MONSTER !!!")
            print("1. Tampilkan semua Monster")
            print("2. Tambah Monster baru")
            choice = input(">>> Pilih Aksi : ")

            if choice == '1':
                self.display_all_monsters()
            elif choice == '2':
                self.add_new_monster()
            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")

# Main function to run the monster management
def main():
    monster_file_path = 'monster.csv'
    monster_manager = MonsterManagement(monster_file_path)
    monster_manager.run_monster_management()

if __name__ == "__main__":
    main()
