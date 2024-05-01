# F11 - Laboratory

class Monster:
    def __init__(self, name, level):
        self.name = name
        self.level = level

class Laboratory:
    def __init__(self, monsters):
        self.monsters = monsters

    def display_monsters(self):
        print("============ MONSTER LIST ============")
        for index, monster in enumerate(self.monsters, start=1):
            print(f"{index}. {monster.name} (Level: {monster.level})")

    def upgrade_monster(self):
        self.display_monsters()
        selected_index = int(input(">>> Pilih monster: ")) - 1

        monster = self.monsters[selected_index]
        if monster.level >= 5:
            print(f"Maaf, {monster.name} sudah mencapai level maksimum.")
            return

        upgrade_costs = {
            1: 300,
            2: 500,
            3: 800,
            4: 1000
        }

        current_level = monster.level
        next_level = current_level + 1

        if next_level not in upgrade_costs:
            print(f"Maaf, {monster.name} tidak dapat di-upgrade ke level selanjutnya.")
            return

        upgrade_cost = upgrade_costs[next_level]
        confirmation = input(f"{monster.name} akan di-upgrade ke level {next_level}. Harga untuk upgrade: {upgrade_cost} OC. Lanjutkan upgrade? (Y/N): ")

        if confirmation.upper() == 'Y':
            # Implementasi untuk cek OC cukup dan proses upgrade
            print(f"Selamat, {monster.name} berhasil di-upgrade ke level {next_level}!")
            monster.level = next_level
        else:
            print("Upgrade dibatalkan.")

# Test Case
if __name__ == "__main__":
    monsters = [
        Monster("Chacha", 1),
        Monster("Pikachow", 2),
        Monster("Zeze", 5)
    ]

    lab = Laboratory(monsters)

    while True:
        print("\n>>> LABORATORY")
        lab.upgrade_monster()

        continue_prompt = input("\nLakukan upgrade lagi? (Y/N): ")
        if continue_prompt.upper() != 'Y':
            break

    print("Terima kasih telah menggunakan Laboratorium.")
