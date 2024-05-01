# F07 - Inventory

import csv

class InventoryManager:
    def __init__(self, user_id):
        self.user_id = user_id
        self.monsters = []
        self.potions = []
        self.load_inventory()

    def load_inventory(self):
        self.load_monsters_from_file('monster_inventory.csv')
        self.load_items_from_file('item_inventory.csv')

    def load_monsters_from_file(filename):
        monsters = []
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file, delimiter=';')
                for row in reader:
                    monster = {
                        'user_id': int(row['user_id']),
                        'monster_id': int(row['monster_id']),
                        'level': int(row['level'])
                    }
                    monsters.append(monster)
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
        except Exception as e:
            print(f"Error occurred while loading {filename}: {e}")
        return monsters

    def load_items_from_file(self, filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                if row['type'] == 'Potion':
                    potion = {
                        'type': row['type'],
                        'quantity': int(row['quantity'])
                    }
                    self.potions.append(potion)

    def display_inventory_summary(self):
        print(f"============ INVENTORY LIST (User ID: {self.user_id}) ============")
        id = 1
        for monster in self.monsters:
            print(f"{id}. Monster       (Name: {monster['name']}, Lvl: {monster['level']}, HP: {monster['hp']})")
            id += 1
        for potion in self.potions:
            print(f"{id}. Potion        (Type: {potion['type']}, Qty: {potion['quantity']})")
            id += 1

    def display_item_details(self, item_id):
        item_index = item_id - 1
        if 0 <= item_index < len(self.monsters):
            monster = self.monsters[item_index]
            print(f"Monster")
            print(f"Name      : {monster['name']}")
            print(f"ATK Power : {monster['atk_power']}")
            print(f"DEF Power : {monster['def_power']}")
            print(f"HP        : {monster['hp']}")
            print(f"Level     : {monster['level']}")
        elif len(self.monsters) <= item_index < len(self.monsters) + len(self.potions):
            potion = self.potions[item_index - len(self.monsters)]
            print(f"Potion")
            print(f"Type      : {potion['type']}")
            print(f"Quantity  : {potion['quantity']}")
        else:
            print("Invalid item ID.")

    def process_inventory(self):
        while True:
            print("\nKetikkan id untuk menampilkan detail item:")
            user_input = input(">>> ")
            if user_input.upper() == 'KELUAR':
                break
            try:
                item_id = int(user_input)
                self.display_item_details(item_id)
            except ValueError:
                print("Input tidak valid. Masukkan ID item atau 'KELUAR' untuk kembali.")

def main():
    user_id = 1 
    inventory_manager = InventoryManager(user_id)
    inventory_manager.display_inventory_summary()
    inventory_manager.process_inventory()

if __name__ == "__main__":
    main()
