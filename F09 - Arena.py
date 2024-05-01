# F09 - Arena

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

def arena(agent_monster):
    print("============ ARENA ============")
    print("Selamat datang di Arena!!\n")

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
        monster_name = "Chacha"
    elif monster_choice == 2:
        monster_name = "Pikachow"
    else:
        monster_name = "Zeze"

    print(f"\nRAWRRR, Agent X mengeluarkan monster {agent_monster.name} !!!\n")
    print(f"Name      : {agent_monster.name}")
    print(f"ATK Power : {agent_monster.base_atk_power}")
    print(f"DEF Power : {agent_monster.base_def_power}")
    print(f"HP        : {agent_monster.base_hp}")
    print(f"Level     : {agent_monster.level}\n")

    stage_rewards = [30, 50, 100, 150, 200]  # OC rewards for each stage
    total_reward = 0
    total_damage_given = 0
    total_damage_taken = 0

    for stage in range(5):
        print(f"============= STAGE {stage + 1} =============")
        enemy_level = stage + 1
        enemy = Monster(monster_name, 20 + (5 * enemy_level), 5 + (2 * enemy_level), 100 + (20 * enemy_level), enemy_level)

        while True:
            battle_result = battle(agent_monster, enemy)

            if battle_result == "win":
                print(f"\nSTAGE CLEARED! Anda akan mendapatkan {stage_rewards[stage]} OC pada sesi ini!\n")
                total_reward += stage_rewards[stage]
                agent_monster.current_hp = agent_monster.base_hp  # Restore HP after stage clear
                break
            elif battle_result == "lose":
                print(f"\nGAME OVER! Sesi latihan berakhir pada stage {stage + 1}!\n")
                print("============== STATS ==============")
                print(f"Total hadiah      : {total_reward} OC")
                print(f"Jumlah stage      : {stage}")
                print(f"Damage diberikan  : {total_damage_given}")
                print(f"Damage diterima   : {total_damage_taken}")
                return

    print(f"\nSelamat, Anda berhasil menyelesaikan seluruh stage Arena !!!\n")
    print("============== STATS ==============")
    print(f"Total hadiah      : {total_reward} OC")
    print(f"Jumlah stage      : 5")
    print(f"Damage diberikan  : {total_damage_given}")
    print(f"Damage diterima   : {total_damage_taken}")

def battle(agent_monster, enemy):
    print(f"RAWRRR, Monster {enemy.name} telah muncul !!!\n")
    print(f"Name      : {enemy.name}")
    print(f"ATK Power : {enemy.base_atk_power}")
    print(f"DEF Power : {enemy.base_def_power}")
    print(f"HP        : {enemy.base_hp}")
    print(f"Level     : {enemy.level}\n")

    while True:
        print(f"============ TURN ({agent_monster.name}) ============")
        print("1. Attack")
        print("2. Use Potion")
        print("3. Quit")

        try:
            choice = int(input("Pilih perintah: "))
            if choice == 1:
                attack_damage = agent_monster.attack()
                print(f"\nSCHWINKKK, {agent_monster.name} menyerang {enemy.name} !!!\n")
                reduced_damage = enemy.defend(attack_damage)
                print(f"Name      : {enemy.name}")
                print(f"ATK Power : {enemy.base_atk_power}")
                print(f"DEF Power : {enemy.base_def_power}")
                print(f"HP        : {enemy.current_hp}")
                print(f"Level     : {enemy.level}")
                print(f"ATT Results: {attack_damage}, Reduced by: {reduced_damage}, HP terakhir: {enemy.current_hp}\n")
                
                if enemy.current_hp <= 0:
                    print(f"Selamat, Anda berhasil mengalahkan monster {enemy.name} !!!\n")
                    return "win"
                
                print(f"============= TURN ({enemy.name}) ============")
                print(f"\nSCHWINKKK, {enemy.name} menyerang {agent_monster.name} !!!\n")
                attack_damage = enemy.attack()
                reduced_damage = agent_monster.defend(attack_damage)
                print(f"Name      : {agent_monster.name}")
                print(f"ATK Power : {agent_monster.base_atk_power}")
                print(f"DEF Power : {agent_monster.base_def_power}")
                print(f"HP        : {agent_monster.current_hp}")
                print(f"Level     : {agent_monster.level}")
                print(f"ATT Results: {attack_damage}, Reduced by: {reduced_damage}, HP terakhir: {agent_monster.current_hp}\n")

                if agent_monster.current_hp <= 0:
                    print(f"Yahhh, Anda dikalahkan monster {enemy.name}. Jangan menyerah, coba lagi !!!\n")
                    return "lose"
                
            elif choice == 2:
                print("Anda tidak memiliki Potion dalam inventory!\n")
            elif choice == 3:
                print("Anda berhasil kabur dari BATTLE!\n")
                return "quit"
            else:
                print("Pilihan perintah tidak valid!\n")
        except ValueError:
            print("Masukkan nomor yang valid!\n")

# Test Case
if __name__ == "__main__":
    pikachow = AgentMonster("Pikachow", 25, 5, 120, 1)
    arena(pikachow)
