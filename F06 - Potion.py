# F06 - Potion

class Potion:
    def __init__(self, type):
        self.type = type

    def apply(self, agent):
        if self.type == 'strength':
            self.apply_strength_potion(agent)
        elif self.type == 'resilience':
            self.apply_resilience_potion(agent)
        elif self.type == 'healing':
            self.apply_healing_potion(agent)

    def apply_strength_potion(self, agent):
        """Meningkatkan ATK Power sebanyak 5% dari base ATK Power."""
        agent.increase_atk_power(agent.base_atk_power * 0.05)

    def apply_resilience_potion(self, agent):
        """Meningkatkan DEF Power sebanyak 5% dari base DEF Power."""
        agent.increase_def_power(agent.base_def_power * 0.05)

    def apply_healing_potion(self, agent):
        """Mengisi darah sebanyak 25% dari base HP."""
        heal_amount = agent.base_hp * 0.25
        agent.heal(heal_amount)

class Agent:
    def __init__(self, name, base_atk_power, base_def_power, base_hp):
        self.name = name
        self.base_atk_power = base_atk_power
        self.base_def_power = base_def_power
        self.base_hp = base_hp
        self.current_hp = base_hp

    def increase_atk_power(self, amount):
        """Meningkatkan ATK Power agent."""
        self.base_atk_power += amount

    def increase_def_power(self, amount):
        """Meningkatkan DEF Power agent."""
        self.base_def_power += amount

    def heal(self, amount):
        """Menambah darah agent, pastikan tidak melebihi base HP."""
        self.current_hp = min(self.base_hp, self.current_hp + amount)

def main():
    # Membuat contoh Agent
    agent = Agent('Agent X', 500, 50, 1000)

    # Membuat dan mengaplikasikan potion
    strength_potion = Potion('strength')
    resilience_potion = Potion('resilience')
    healing_potion = Potion('healing')

    strength_potion.apply(agent)
    resilience_potion.apply(agent)
    healing_potion.apply(agent)

    # Menampilkan informasi setelah menggunakan potion
    print(f"Setelah menggunakan potion:")
    print(f"ATK Power: {agent.base_atk_power}")
    print(f"DEF Power: {agent.base_def_power}")
    print(f"HP: {agent.current_hp}/{agent.base_hp}")

if __name__ == "__main__":
    main()