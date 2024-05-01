# F10 - Shop & Currency

class Shop:
    def __init__(self):
        self.monsters = [
            {"id": 1, "type": "Pokemon Air", "atk_power": 10, "def_power": 1000, "hp": 200, "stock": 1, "price": 100},
            {"id": 2, "type": "Pokemon Api", "atk_power": 20, "def_power": 1000, "hp": 200, "stock": 5, "price": 20},
            {"id": 3, "type": "Pokemon Tanah", "atk_power": 30, "def_power": 430, "hp": 100, "stock": 0, "price": 300}
        ]
        self.potions = [
            {"id": 1, "type": "Strength Potion", "stock": 1, "price": 20},
            {"id": 2, "type": "Resilience Potion", "stock": 5, "price": 300}
        ]

    def display_monsters(self):
        print("ID | Type          | ATK Power | DEF Power | HP   | Stok | Harga")
        for monster in self.monsters:
            print(f"{monster['id']}  | {monster['type']:<13} | {monster['atk_power']:<9} | {monster['def_power']:<9} | {monster['hp']:<4} | {monster['stock']:<5} | {monster['price']}")

    def display_potions(self):
        print("ID | Type                | Stok | Harga")
        for potion in self.potions:
            print(f"{potion['id']}  | {potion['type']:<19} | {potion['stock']:<4} | {potion['price']}")

    def buy_monster(self, agent_coins, monster_id):
        for monster in self.monsters:
            if monster['id'] == monster_id:
                if monster['stock'] > 0:
                    # Check if monster already in inventory
                    # Simulated validation based on monster_id, assuming agent has an inventory
                    if monster_id == 1:  # Check for existing Pokemon Air in inventory
                        print(f"Monster {monster['type']} sudah ada dalam inventory-mu! Pembelian dibatalkan.")
                        return False
                    
                    # Deduct coins and update stock
                    if agent_coins >= monster['price']:
                        agent_coins -= monster['price']
                        monster['stock'] -= 1
                        print(f"Berhasil membeli item: {monster['type']}. Item sudah masuk ke inventory-mu!")
                        return True
                    else:
                        print("OC-mu tidak cukup.")
                        return False

        print("Item tidak tersedia.")
        return False

    def buy_potion(self, agent_coins, potion_id, quantity):
        for potion in self.potions:
            if potion['id'] == potion_id:
                if potion['stock'] >= quantity:
                    # Deduct coins and update stock
                    if agent_coins >= potion['price'] * quantity:
                        agent_coins -= potion['price'] * quantity
                        potion['stock'] -= quantity
                        print(f"Berhasil membeli item: {quantity} Potion of {potion['type']}. Item sudah masuk ke inventory-mu!")
                        return True
                    else:
                        print("OC-mu tidak cukup.")
                        return False

        print("Item tidak tersedia atau stok tidak mencukupi.")
        return False

def shop(agent_coins):
    shop = Shop()
    print("Irasshaimase! Selamat datang di SHOP!!\n")

    while True:
        print(">>> Pilih aksi (lihat/beli/keluar): ")
        action = input()

        if action == "lihat":
            print(">>> Mau lihat apa? (monster/potion): ")
            item_type = input()

            if item_type == "monster":
                shop.display_monsters()
            elif item_type == "potion":
                shop.display_potions()
            else:
                print("Pilihan tidak valid.")
        
        elif action == "beli":
            print(f"Jumlah O.W.C.A. Coin-mu sekarang {agent_coins}.\n")
            print(">>> Mau beli apa? (monster/potion): ")
            item_type = input()

            if item_type == "monster":
                print(">>> Masukkan id monster: ")
                monster_id = int(input())
                shop.buy_monster(agent_coins, monster_id)
            elif item_type == "potion":
                print(">>> Masukkan id potion: ")
                potion_id = int(input())
                print(">>> Masukkan jumlah: ")
                quantity = int(input())
                shop.buy_potion(agent_coins, potion_id, quantity)
            else:
                print("Pilihan tidak valid.")

        elif action == "keluar":
            print("Mr. Yanto bilang makasih, belanja lagi ya nanti :)")
            break

        else:
            print("Pilihan tidak valid.")

# Test Case
if __name__ == "__main__":
    agent_coins = 1000
    shop(agent_coins)
