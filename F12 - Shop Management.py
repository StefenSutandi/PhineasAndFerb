import csv

class ShopManagement:
    def __init__(self, item_file_path, monster_file_path):
        self.items = self.load_items(item_file_path)
        self.monsters = self.load_monsters(monster_file_path)

    def load_items(self, item_file_path):
        items = {}
        with open(item_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                item_type = row['type']
                stock = int(row['stock'])
                price = int(row['price'])
                items[len(items) + 1] = {'type': item_type, 'stock': stock, 'price': price}
        return items

    def load_monsters(self, monster_file_path):
        monsters = {}
        with open(monster_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                monster_id = int(row['monster_id'])
                stock = int(row['stock'])
                price = int(row['price'])
                monsters[monster_id] = {'stock': stock, 'price': price}
        return monsters

    def view_items(self, item_type):
        if item_type not in ['monster', 'potion']:
            print("Invalid item type. Please choose 'monster' or 'potion'.")
            return

        print(f"ID | Type          | Stok | Harga")
        for item_id, details in self.items.items():
            if details['type'] == item_type:
                print(f"{item_id:<2} | {details['type']:<14} | {details['stock']:<4} | {details['price']:<5}")

    def add_item(self, item_type):
        if item_type not in ['monster', 'potion']:
            print("Invalid item type. Please choose 'monster' or 'potion'.")
            return

        print(f"Menampilkan seluruh {item_type} yang ada di database tetapi belum ada pada shop:")
        print("ID | Type")
        if item_type == 'monster':
            for monster_id, details in self.monsters.items():
                print(f"{monster_id:<2} | {details['type']}")
        elif item_type == 'potion':
            for item_id, details in self.items.items():
                if details['type'] != 'monster':
                    print(f"{item_id:<2} | {details['type']}")

        item_id = input("Masukkan ID item yang ingin ditambahkan ke shop: ")
        if item_id.isdigit() and int(item_id) in self.monsters:
            stock = int(input("Masukkan stok awal item: "))
            price = int(input("Masukkan harga item: "))
            self.items[len(self.items) + 1] = {'type': self.monsters[int(item_id)]['type'], 'stock': stock, 'price': price}
            print(f"{self.monsters[int(item_id)]['type']} berhasil ditambahkan ke dalam shop!")
        else:
            print("ID item tidak valid atau tidak ada di database.")

    def update_item(self, item_type):
        if item_type not in ['monster', 'potion']:
            print("Invalid item type. Please choose 'monster' or 'potion'.")
            return

        print(f"Menampilkan seluruh {item_type} yang ada di shop:")
        print("ID | Type          | Stok | Harga")
        for item_id, details in self.items.items():
            if details['type'] == item_type:
                print(f"{item_id:<2} | {details['type']:<14} | {details['stock']:<4} | {details['price']:<5}")

        item_id = input("Masukkan ID item yang ingin diubah stok/harganya: ")
        if item_id.isdigit() and int(item_id) in self.items:
            new_stock = input("Masukkan stok baru item: ")
            new_price = input("Masukkan harga baru item: ")

            if new_stock:
                self.items[int(item_id)]['stock'] = int(new_stock)
            if new_price:
                self.items[int(item_id)]['price'] = int(new_price)

            print(f"{self.items[int(item_id)]['type']} berhasil diubah dengan stok baru {new_stock} "
                  f"dan harga baru {new_price}!")
        else:
            print("ID item tidak valid atau tidak ada di shop.")

    def delete_item(self, item_type):
        if item_type not in ['monster', 'potion']:
            print("Invalid item type. Please choose 'monster' or 'potion'.")
            return

        print(f"Menampilkan seluruh {item_type} yang ada di shop:")
        print("ID | Type          | Stok | Harga")
        for item_id, details in self.items.items():
            if details['type'] == item_type:
                print(f"{item_id:<2} | {details['type']:<14} | {details['stock']:<4} | {details['price']:<5}")

        item_id = input(f"Masukkan ID {item_type} yang ingin dihapus dari shop: ")
        if item_id.isdigit() and int(item_id) in self.items:
            confirm = input(f"Apakah anda yakin ingin menghapus {self.items[int(item_id)]['type']} dari shop (y/n)? ")
            if confirm.lower() == 'y':
                del self.items[int(item_id)]
                print(f"{self.items[int(item_id)]['type']} berhasil dihapus dari shop!")
        else:
            print("ID item tidak valid atau tidak ada di shop.")

    def run_shop_management(self):
        while True:
            print("\n======== Shop Management Menu =======")
            print("1. Lihat Item")
            print("2. Tambah Item")
            print("3. Ubah Item")
            print("4. Hapus Item")
            print("5. Keluar")

            choice = input("Pilih aksi (1/2/3/4/5): ")
            if choice == '1':
                item_type = input("Mau lihat apa? (monster/potion): ")
                self.view_items(item_type)
            elif choice == '2':
                item_type = input("Mau tambah apa? (monster/potion): ")
                self.add_item(item_type)
            elif choice == '3':
                item_type = input("Mau ubah apa? (monster/potion): ")
                self.update_item(item_type)
            elif choice == '4':
                item_type = input("Mau hapus apa? (monster/potion): ")
                self.delete_item(item_type)
            elif choice == '5':
                print("Dadah Mr. Yanto, sampai jumpa lagi!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")

# Main function to run the shop management
def main():
    item_file_path = 'item_shop.csv'
    monster_file_path = 'monster_shop.csv'
    shop_manager = ShopManagement(item_file_path, monster_file_path)
    shop_manager.run_shop_management()

if __name__ == "__main__":
    main()
