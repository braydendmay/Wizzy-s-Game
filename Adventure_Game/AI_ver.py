import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG Interface")
clock = pygame.time.Clock()

# Fonts and colors
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 48)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (230, 230, 230)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Global game state
current_screen = "menu"
username = ""
input_active = False
input_box = pygame.Rect(250, 300, 300, 40)

selected_class = None
equipped_weapon = None
gold = 100
inventory = ["Basic Wand", "Health Potion", "Rare Katana"]
shop_items = {"Health Potion": 10, "Fire Scroll": 25, "Steel Sword": 40}
class_stats = {
    'Wizard':     {'Health': 25, 'Defense': 10, 'Strength': 5, 'Intelligence': 20, 'Magic': 15, 'Luck': 10},
    'Sorcerer':   {'Health': 25, 'Defense': 10, 'Strength': 10, 'Intelligence': 20, 'Magic': 10, 'Luck': 10},
    'Knight':     {'Health': 25, 'Defense': 10, 'Strength': 10, 'Intelligence': 20, 'Magic': 10, 'Luck': 10},
    'Samurai':    {'Health': 25, 'Defense': 10, 'Strength': 10, 'Intelligence': 20, 'Magic': 10, 'Luck': 10},
    'Ninja':      {'Health': 25, 'Defense': 10, 'Strength': 10, 'Intelligence': 20, 'Magic': 10, 'Luck': 10},
    'Archer':     {'Health': 25, 'Defense': 10, 'Strength': 10, 'Intelligence': 20, 'Magic': 10, 'Luck': 10},
    'Tank':       {'Health': 25, 'Defense': 10, 'Strength': 10, 'Intelligence': 20, 'Magic': 10, 'Luck': 10},
    'Brainiac':   {'Health': 25, 'Defense': 10, 'Strength': 10, 'Intelligence': 20, 'Magic': 10, 'Luck': 10},
    'Mechanic':   {'Health': 25, 'Defense': 10, 'Strength': 10, 'Intelligence': 20, 'Magic': 10, 'Luck': 10}
}

class Button:
    def __init__(self, text, x, y, w, h, callback, color=GRAY):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        txt_surf = font.render(self.text, True, BLACK)
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        surface.blit(txt_surf, txt_rect)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.callback()

# Screen transitions
def go_to_class_select():
    global current_screen
    current_screen = "class_select"

def go_to_stats():
    global current_screen
    current_screen = "stats"

def go_to_inventory():
    global current_screen
    current_screen = "inventory"

def go_to_shop():
    global current_screen
    current_screen = "shop"

def go_to_combat():
    global current_screen
    current_screen = "combat"

def quit_game():
    pygame.quit()
    sys.exit()

menu_buttons = [
    Button("Start Game", 300, 200, 200, 50, go_to_class_select),
    Button("Quit", 300, 270, 200, 50, quit_game)
]

def draw_menu():
    screen.fill(WHITE)
    title = big_font.render("Welcome to the RPG!", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
    for button in menu_buttons:
        button.draw(screen)

def draw_name_input():
    prompt = font.render("Enter your name:", True, BLACK)
    screen.blit(prompt, (input_box.x, input_box.y - 40))
    pygame.draw.rect(screen, BLACK if input_active else GRAY, input_box, 2)
    name_surface = font.render(username, True, BLACK)
    screen.blit(name_surface, (input_box.x + 5, input_box.y + 5))

def draw_class_select():
    screen.fill(WHITE)
    y = 100
    title = big_font.render("Choose a Class", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))
    for cls in class_stats:
        btn = Button(cls, 300, y, 200, 40, lambda c=cls: select_class(c))
        btn.draw(screen)
        class_buttons.append(btn)
        y += 50

class_buttons = []
def select_class(cls):
    global selected_class
    selected_class = cls
    go_to_stats()

def draw_stats():
    screen.fill(WHITE)
    title = big_font.render(f"{username} the {selected_class}", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))
    y = 120
    for stat, value in class_stats[selected_class].items():
        stat_text = font.render(f"{stat}: {value}", True, BLACK)
        screen.blit(stat_text, (WIDTH // 2 - stat_text.get_width() // 2, y))
        y += 40
    gold_text = font.render(f"Gold: {gold}", True, BLACK)
    screen.blit(gold_text, (WIDTH // 2 - gold_text.get_width() // 2, y + 10))
    Button("Inventory", WIDTH//2 - 160, y + 60, 140, 40, go_to_inventory).draw(screen)
    Button("Shop", WIDTH//2 + 20, y + 60, 100, 40, go_to_shop).draw(screen)
    Button("Combat", WIDTH//2 - 50, y + 110, 100, 40, go_to_combat).draw(screen)

def draw_inventory():
    screen.fill(WHITE)
    title = big_font.render("Inventory", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))
    y = 120
    if inventory:
        for i, item in enumerate(inventory):
            label = f"Equip {item}" if "Sword" in item or "Katana" in item or "Wand" in item else f"Use {item}"
            btn = Button(label, 250, y, 300, 40, lambda i=item: handle_item(i), color=LIGHT_GRAY)
            btn.draw(screen)
            inventory_buttons.append(btn)
            y += 50
    else:
        empty_text = font.render("Inventory is empty.", True, BLACK)
        screen.blit(empty_text, (WIDTH // 2 - empty_text.get_width() // 2, y))
    if equipped_weapon:
        equip_text = font.render(f"Equipped: {equipped_weapon}", True, BLACK)
        screen.blit(equip_text, (WIDTH // 2 - equip_text.get_width() // 2, HEIGHT - 50))

def handle_item(item):
    global equipped_weapon
    if "Sword" in item or "Katana" in item or "Wand" in item:
        equipped_weapon = item
    else:
        inventory.remove(item)

def draw_shop():
    screen.fill(WHITE)
    title = big_font.render("Shop", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))
    y = 120
    for item, price in shop_items.items():
        btn = Button(f"Buy {item} - {price}g", 250, y, 300, 40, lambda i=item: buy_item(i), color=GREEN)
        btn.draw(screen)
        shop_buttons.append(btn)
        y += 50
    gold_text = font.render(f"Gold: {gold}", True, BLACK)
    screen.blit(gold_text, (10, 10))

def buy_item(item):
    global gold
    price = shop_items[item]
    if gold >= price:
        gold -= price
        inventory.append(item)

def draw_combat():
    screen.fill(WHITE)
    title = big_font.render("Combat Screen", True, RED)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))
    enemy_text = font.render("A wild Goblin appears!", True, BLACK)
    screen.blit(enemy_text, (WIDTH // 2 - enemy_text.get_width() // 2, 150))
    weapon_text = font.render(f"Weapon: {equipped_weapon if equipped_weapon else 'None'}", True, BLACK)
    screen.blit(weapon_text, (WIDTH // 2 - weapon_text.get_width() // 2, 200))
    Button("Attack", WIDTH // 2 - 75, 300, 150, 50, lambda: print("Attacked!"), color=RED).draw(screen)

inventory_buttons = []
shop_buttons = []

# Main loop
while True:
    screen.fill(WHITE)
    class_buttons.clear()
    inventory_buttons.clear()
    shop_buttons.clear()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()

        if current_screen == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in menu_buttons:
                    button.check_click(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    if len(username) < 16:
                        username += event.unicode

        elif current_screen == "class_select":
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in class_buttons:
                    button.check_click(event.pos)

        elif current_screen == "stats":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH//2 - 160 <= event.pos[0] <= WIDTH//2 - 20 and 400 <= event.pos[1] <= 440:
                    go_to_inventory()
                elif WIDTH//2 + 20 <= event.pos[0] <= WIDTH//2 + 120 and 400 <= event.pos[1] <= 440:
                    go_to_shop()
                elif WIDTH//2 - 50 <= event.pos[0] <= WIDTH//2 + 50 and 450 <= event.pos[1] <= 490:
                    go_to_combat()

        elif current_screen == "inventory":
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in inventory_buttons:
                    button.check_click(event.pos)

        elif current_screen == "shop":
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in shop_buttons:
                    button.check_click(event.pos)

    if current_screen == "menu":
        draw_menu()
        draw_name_input()
    elif current_screen == "class_select":
        draw_class_select()
    elif current_screen == "stats":
        draw_stats()
    elif current_screen == "inventory":
        draw_inventory()
    elif current_screen == "shop":
        draw_shop()
    elif current_screen == "combat":
        draw_combat()

    pygame.display.flip()
    clock.tick(60)
