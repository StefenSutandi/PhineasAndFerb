# F08 - Battle

import random
import math

class Monster:
    def __init__(self, name, atk_power, def_power, hp, level):
        self.name = name
        self.base_atk_power = atk_power
        self.base_def_power = def_power
        self.base_hp = hp
        self.level = level
        self.current_hp = hp
    
    def attack(self):
        return self.base_atk_power
    
    def defend(self, damage):
        reduced_damage = damage * (self.base_def_power / 100)
        self.current_hp = max(0, math.floor(self.current_hp - reduced_damage))
        return reduced_damage

class AgentMonster:
    def __init__(self, name, atk_power, def_power, hp, level):
        self.name = name
        self.base_atk_power = atk_power
        self.base_def_power = def_power
        self.base_hp = hp
        self.level = level
        self.current_hp = hp
        self.atk_buff = 0
        self.def_buff = 0
    
    def attack(self):
        return (self.base_atk_power + self.atk_buff)
    
    def defend(self, damage):
        reduced_damage = damage * (self.base_def_power / 100) - self.def_buff
        self.current_hp = max(0, math.floor(self.current_hp - reduced_damage))
        return reduced_damage

def battle(agent_monster, enemy):
    print("=========== BATTLE ===========")
    print(f"RAWRRR, Monster {enemy.name} telah muncul !!!\n")
    print(f"Name      : {enemy.name}")
    print(f"ATK Power : {enemy.base_atk_power}")
    print(f"DEF Power : {enemy.base_def_power}")
    print(f"HP        : {enemy.base_hp}")
    print(f"Level     : {enemy.level}\n")

    print("============ MONSTER LIST ============")
    print("1. Chacha")
    print("2. Pikachow")
    print("3. Zeze")

    while True:
        try:
            monster_choice = int(input("Pilih monster untuk bertarung: "))
            if monster_choice not in [1, 2, 3]:
                print("Pilihan nomor tidak tersedia!")
                continue
            
            break
        except ValueError:
            print("Masukkan nomor yang valid!")

    if monster_choice == 1:
        agent_name = "Chacha"
    elif monster_choice == 2:
        agent_name = "Pikachow"
    else:
        agent_name = "Zeze"

    print(f"\nRAWRRR, Agent X mengeluarkan monster {agent_name} !!!\n")
    print(f"Name      : {agent_monster.name}")
    print(f"ATK Power : {agent_monster.base_atk_power}")
    print(f"DEF Power : {agent_monster.base_def_power}")
    print(f"HP        : {agent_monster.base_hp}")
    print(f"Level     : {agent_monster.level}\n")

    turn = 1
    while True:
        print(f"============ TURN {turn} ({agent_monster.name}) ============")
        print("1. Attack")
        print("2. Use Potion")
        print("3. Quit")

        try:
            choice = int(input("Pilih perintah: "))
            if choice == 1:
                attack_damage = agent_monster.attack()
                print(f"\nSCHWINKKK, {agent_name} menyerang {enemy.name} !!!\n")
                reduced_damage = enemy.defend(attack_damage)
                print(f"Name      : {enemy.name}")
                print(f"ATK Power : {enemy.base_atk_power}")
                print(f"DEF Power : {enemy.base_def_power}")
                print(f"HP        : {enemy.current_hp}")
                print(f"Level     : {enemy.level}")
                print(f"ATT Results: {attack_damage}")
                print(f"HP terakhir: {enemy.current_hp}\n")

                if enemy.current_hp <= 0:
                    oc_earned = random.randint(5, 30)
                    print(f"Selamat, Anda berhasil mengalahkan monster {enemy.name} !!!\n")
                    print(f"Total OC yang diperoleh: {oc_earned}\n")
                    break

            elif choice == 2:
                print("============ POTION LIST ============")
                print("1. Strength Potion (Qty: 3) - Increases ATK Power")
                print("2. Resilience Potion (Qty: 4) - Increases DEF Power")
                print("3. Healing Potion (Qty: 1) - Restores Health")
                print("4. Cancel")

                potion_choice = int(input("Pilih perintah: "))
                if potion_choice == 1:
                    # Implement use potion logic here
                    print("Setelah meminum ramuan ini, aura kekuatan terlihat mengelilingi Pikachow dan gerakannya menjadi lebih cepat dan mematikan.")
                elif potion_choice == 2:
                    # Implement use potion logic here
                    print("Setelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar Pikachow yang membuatnya terlihat semakin tangguh dan sulit dilukai.")
                elif potion_choice == 3:
                    # Implement use potion logic here
                    print("Setelah meminum ramuan ini, luka-luka yang ada di dalam tubuh Pikachow sembuh dengan cepat. Dalam sekejap, Pikachow terlihat kembali prima dan siap melanjutkan pertempuran.")
                elif potion_choice == 4:
                    continue

            elif choice == 3:
                print("Anda berhasil kabur dari BATTLE!\n")
                break

            else:
                print("Pilihan nomor tidak tersedia!")

            turn += 1
        
        except ValueError:
            print("Masukkan nomor yang valid!")

# Test Case
if __name__ == "__main__":
    agent_monster = AgentMonster("Pikachow", 25, 5, 120, 1)
    enemy = Monster("Zuko", 20, 20, 100, 1)
    battle(agent_monster, enemy)
