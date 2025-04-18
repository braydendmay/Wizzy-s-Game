import json
import random
import os

# -----------------------------
# Game Classes
# -----------------------------

class Player:
    def __init__(self, name, cls):
        self.name = name
        self.cls = cls
        self.hp = 100
        self.level = 1
        self.exp = 0
        self.gold = 10
        self.inventory = ["Potion"]
        self.set_stats(cls)

    def set_stats(self, cls):
        classes = {
            "Warrior": {"atk": 10, "defense": 8},
            "Mage": {"atk": 12, "defense": 5},
            "Rogue": {"atk": 9, "defense": 6}
        }
        self.atk = classes[cls]["atk"]
        self.defense = classes[cls]["defense"]

    def stats(self):
        return f"{self.name} the {self.cls} | HP: {self.hp} | ATK: {self.atk} | DEF: {self.defense} | Gold: {self.gold} | EXP: {self.exp}"

    def is_alive(self):
        return self.hp > 0


class Enemy:
    def __init__(self, name, hp, atk, defense, exp_reward, gold_reward):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.exp_reward = exp_reward
        self.gold_reward = gold_reward

    def is_alive(self):
        return self.hp > 0

# -----------------------------
# Game Functions
# -----------------------------

def character_creation():
    print("Welcome, adventurer! Choose your class:")
    print("1. Warrior\n2. Mage\n3. Rogue")
    choice = input("Enter choice: ")
    cls = {"1": "Warrior", "2": "Mage", "3": "Rogue"}.get(choice, "Warrior")
    name = input("Enter your character's name: ")
    return Player(name, cls)

def save_game(player):
    with open("savegame.json", "w") as f:
        json.dump(player.__dict__, f)
    print("Game saved.")

def load_game():
    if not os.path.exists("savegame.json"):
        print("No saved game found.")
        return None
    with open("savegame.json", "r") as f:
        data = json.load(f)
        player = Player(data['name'], data['cls'])
        player.__dict__.update(data)
        print("Game loaded.")
        return player

def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")

    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name} HP: {player.hp} | {enemy.name} HP: {enemy.hp}")
        action = input("Do you want to (A)ttack or (R)un? ").lower()
        if action == "a":
            dmg = max(0, player.atk - enemy.defense + random.randint(-2, 3))
            enemy.hp -= dmg
            print(f"You hit {enemy.name} for {dmg} damage.")
            if enemy.is_alive():
                enemy_dmg = max(0, enemy.atk - player.defense + random.randint(-2, 3))
                player.hp -= enemy_dmg
                print(f"{enemy.name} hits you for {enemy_dmg} damage.")
        elif action == "r":
            if random.random() > 0.5:
                print("You fled successfully!")
                return
            else:
                print("You failed to escape!")
                enemy_dmg = max(0, enemy.atk - player.defense)
                player.hp -= enemy_dmg
                print(f"{enemy.name} hits you for {enemy_dmg} damage.")
        else:
            print("Invalid input.")
    
    if player.is_alive():
        print(f"You defeated {enemy.name}!")
        player.exp += enemy.exp_reward
        player.gold += enemy.gold_reward
        level_up(player)
    else:
        print("You were defeated... Game over.")
        exit()

def level_up(player):
    if player.exp >= player.level * 20:
        player.level += 1
        player.hp = 100
        player.atk += 2
        player.defense += 1
        print(f"\n*** Level Up! You are now level {player.level} ***")
        print(f"Stats increased: ATK +2, DEF +1, HP restored.")

def explore(player):
    print("\nYou explore the area...")
    encounter = random.choice(["enemy", "item", "nothing"])
    if encounter == "enemy":
        enemies = [
            Enemy("Goblin", 30, 6, 2, 10, 5),
            Enemy("Skeleton", 40, 7, 3, 12, 8),
            Enemy("Bandit", 50, 9, 4, 15, 12)
        ]
        battle(player, random.choice(enemies))
    elif encounter == "item":
        item = random.choice(["Potion", "Elixir", "Gold Pouch"])
        if item == "Gold Pouch":
            gold = random.randint(5, 20)
            player.gold += gold
            print(f"You found a pouch with {gold} gold!")
        else:
            player.inventory.append(item)
            print(f"You found a {item}!")
    else:
        print("Nothing happened...")

def use_item(player):
    if not player.inventory:
        print("You have no items!")
        return
    print("Inventory:", player.inventory)
    item = input("Enter item to use: ")
    if item in player.inventory:
        if item == "Potion":
            player.hp = min(100, player.hp + 30)
            print("You used a Potion. +30 HP.")
        elif item == "Elixir":
            player.hp = 100
            print("You used an Elixir. HP fully restored.")
        player.inventory.remove(item)
    else:
        print("Item not found.")

def main_menu():
    print("\n=== Main Menu ===")
    print("1. Explore")
    print("2. View Stats")
    print("3. Inventory")
    print("4. Save Game")
    print("5. Quit")
    return input("Choose an option: ")

# -----------------------------
# Game Loop
# -----------------------------

def main():
    print("Welcome to the Python RPG!")
    if os.path.exists("savegame.json"):
        cont = input("Load saved game? (y/n): ").lower()
        if cont == "y":
            player = load_game()
        else:
            player = character_creation()
    else:
        player = character_creation()

    while player.is_alive():
        choice = main_menu()
        if choice == "1":
            explore(player)
        elif choice == "2":
            print(player.stats())
        elif choice == "3":
            use_item(player)
        elif choice == "4":
            save_game(player)
        elif choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice.")

# -----------------------------
# Start Game
# -----------------------------

if __name__ == "__main__":
    main()
