import time
import os
import random

clear = lambda: os.system('cls')


weapon = 'Basic Wand'
first_weapon = weapon
weapon_value = 20
current_weapon_damage = 10
gold = 200
player_exp = 0
player_level = 1 # add function with combat and repetitive functons to update frequently
health_potion = 1

def weapon_damage():

    global weapons_list
    global random_weapon_choosen
    global random_weapon

#weapon - damage - value - elemental check(0 = yes, 1 = no)
    weapons_list = [['Uncomon Wand', 15, 40, 0],['Common Sword', 20, 40, 1]]

    random_weapon = random.randint(0,1)

    random_weapon_choosen = weapons_list[random_weapon][0] + ' | ' + 'Damage: ' + str(weapons_list[random_weapon][1]) + ' | ' + str(weapons_list[random_weapon][2]) + 'g'

    return random_weapon_choosen

start_game = '-'

def second_scene():

    second_scene = input('Would you like to visit the Store, Mines, or Blacksmith? (store, mine, blacksmith): ')
    
    if second_scene == 'store':
        clear()
        store()
        
    elif second_scene == 'mine':
        clear()
        mine()
    
    elif second_scene == 'blacksmith':
        clear()
        blacksmith()

def store():

    global weapon
    global gold
    global health_potion
    
    print('Upon arriving at the store the clerk welcomes you and shows you his wares, look like he has a number of useful items;')
    purchase = input(f'Store items:                     Gold: {gold}g\n1.Health Potion 40g\n2.{first_weapon} 15g\n3.Sell items\nPress ENTER to leave store\nINPUT: ')

    if purchase == '1':
        if gold >= 40:
            health_potion += 1
            gold = gold - 40
            clear()
            store()

    elif purchase == '2':
        if gold >= 15 and weapon == '':
            weapon = 'Basic Wand'
            gold -= 15
            clear()
            store()

    elif purchase == '3':
        clear()
        sell_items = input(f'What items do you wish to sell?: \n1.Health Potion 40g\n2.Basic Wand 20g\nPress ENTER to go back\nINPUT: ')

        if sell_items == '2':
            if weapon != '':
                weapon = ''
                gold += 20
                clear()
                store()
            else:
                clear()
                print('You do not have a weapon to sell')
                time.sleep(2)
                clear()
                store()

        elif sell_items == '1':
            if health_potion >= 1:
                health_potion -= 1
                gold += 40
                clear()
                store()
            else:
                health_potion = 0
                clear()
                print('You have no Potions to sell')
                time.sleep(2)
                clear()
                store()
        
        elif sell_items == '.dev':
            clear()
            password = input('What is the password?: ')
            if password == 'wizzy':
                clear()
                add_gold = int(input('How much gold would you like to add?: '))
                gold += add_gold 
                clear()
                store()
            else:
                clear()
                print('Wrong password')
                time.sleep(1)
                clear()
                store()

        elif sell_items == '':
            clear()
            store()
        
    elif purchase == '':
        clear()
        second_scene()

    else:
            clear()
            store()

def mine():

    def right_left():

        global gold
        global player_exp

        path_choice = input('Looks like the path ahead is caved in and you need to take the right path or the left path: ').lower()

        if path_choice == 'right' or '1':
            rng_enenmy = random.randint(0,2)
            if rng_enenmy == 0:
                print('You got an enemy')
    #add in combat func here -->
            else:
                print('You found 10g')
                gold += 10
            player_exp += 10

        elif path_choice == 'left' or '2':
            rng_enenmy = random.randint(0,2) 
            if rng_enenmy == 0:
                print('You got an enemy')
    #add in combat func here -->
            else:
                print('You found 10g')
                gold += 10
            player_exp += 10
    
    def forward_leave():

        global gold 
        global leave 
        global player_exp

        path_choice = input('Looks like the only path is straight ahead, do you want to turn back now?: ').lower()
        if path_choice == 'no':
            rng_enenmy = random.randint(0,2)
            if rng_enenmy == 0:
                print('You got an enemy')
    #add in combat func here -->
            else:
                print('You found 10g')
                gold += 10
            player_exp += 10

        elif path_choice == 'yes':
            leave = ''
            print('You are leaving the mines')
            print(f'You got {player_exp}')
            second_scene()

    leave = '-'

    while leave == '-':

        rng_path = random.randint(0,1)

        if rng_path == 0:
            right_left()

        elif rng_path == 1:
            forward_leave()

def blacksmith():
    global current_weapon_damage
    global weapon_value
    global weapon
    global gold
    global health_potion
    
    print('Upon arriving at the store the Blacksmith welcomes you and shows you his wares, look like he has a number of useful items;')
    purchase = input(f'Store items:                     Gold: {gold}g\n1.{weapon_damage()}\n2.{first_weapon} 15g\n3.Sell items\nPress ENTER to leave store\nINPUT: ')

    if purchase == '1':
        if gold >= weapons_list[random_weapon][2]:
            weapon = weapons_list[random_weapon][0]
            current_weapon_damage = weapons_list[random_weapon][1]
            weapon_value = weapons_list[random_weapon][2]
            gold = gold - weapons_list[random_weapon][2]
            clear()
            blacksmith()

    elif purchase == '2':
        if gold >= 15 and weapon == '':
            weapon = 'Basic Wand'
            gold -= 15
            clear()
            store()

    elif purchase == '3':
        sell_items = input(f'What items do you wish to sell?: \n1.Health Potion 40g\n2.Basic Wand 20g\nPress ENTER to go back\nINPUT: ')

        if sell_items == '2':
            if weapon != '':
                weapon = ''
                gold += 20
                clear()
                store()
            else:
                clear()
                print('You do not have a weapon to sell')
                time.sleep(2)
                clear()
                store()

        elif sell_items == '1':
            if health_potion >= 1:
                health_potion -= 1
                gold += 40
                clear()
                store()
            else:
                health_potion = 0
                clear()
                print('You have no Potions to sell')
                time.sleep(2)
                clear()
                store()
        
        elif sell_items == '.dev':
            password = input('What is the password?: ')
            if password == 'wizzy':
                add_gold = int(input('How much gold would you like to add?: '))
                gold += add_gold 
                clear()
                store()
            else:
                print('Wrong password')
                time.sleep(1)
                clear()
                store()

        elif sell_items == '':
            clear()
            store()

    elif purchase == '':
        clear()
        second_scene()

def start_game_fun():
        
        global start_game
        
        start_game = input('Press ENTER to continue')
        clear()
        if start_game == '':
            first_scene = input('You wake in a village\n\nWould you like to vist the local store or go to the mines?(store or mine): ')
            clear()

            if first_scene == 'store':
                clear()
                store()

            if first_scene == 'mine':
                clear()
                mine()
            if first_scene == '1':
                clear()
                blacksmith()
        else:
            start_game_fun()


while start_game == '-':
    start_game_fun()

    