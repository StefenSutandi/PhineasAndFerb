# F05 - Monster

import csv
import random

class Monster:
    def __init__(self, type, atk_power, def_power, hp):
        self.type = type
        self.base_atk_power = atk_power
        self.base_def_power = def_power
        self.hp = hp

    def calculate_attack(self):
        """Menghitung nilai serangan dengan rentang ±30% dari base_atk_power."""
        min_attack = int(self.base_atk_power * 0.7)
        max_attack = int(self.base_atk_power * 1.3)
        return random.randint(min_attack, max_attack)

    def calculate_defense(self):
        """Menghitung nilai pertahanan berdasarkan base_def_power."""
        return self.base_def_power

def load_monsters_from_file(filename):
    monsters = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            monster = Monster(
                type=row['type'],
                atk_power=int(row['atk_power']),
                def_power=int(row['def_power']),
                hp=int(row['hp'])
            )
            monsters.append(monster)
    return monsters

def main():
    # Load monsters from CSV file
    monsters = load_monsters_from_file('monster.csv')

    # Display information for each monster
    print("============= OWCA-DEX =============")
    for i, monster in enumerate(monsters, start=1):
        print(f"Monster {i}: {monster.type}")
        print(f"   ATK Power: {monster.base_atk_power}")
        print(f"   DEF Power: {monster.base_def_power}")
        print(f"   HP: {monster.hp}")
        print()

if __name__ == "__main__":
    main()
