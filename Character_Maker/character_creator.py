import random
import time
import os

clear = lambda: os.system('cls')

def selection():

    global selected_class

    clear()

    selected_class = '-'

    while selected_class == '-':

        print("Choose a Class(1-9):\nOr to see the details of a class press ENTER\n1.Wizard\n2.Scorcer\n3.Knight\n4.Samurai\n5.Ninja\n6.Archer\n7.Tank\n8.Brainiac\n9.Mechanic")
        choose_class = input('Class #: ')

        if choose_class == '':
            clear()
            print('Class List:\n1.Wizard\n2.Scorcer\n3.Knight\n4.Samurai\n5.Ninja\n6.Archer\n7.Tank\n8.Brainiac\n9.Mechanic')
            view_class = input('To exit press ENTER\nWhich Class would you like to view?(1-9): ')

            if view_class == '':
                clear()
                selection()

            elif view_class == '1': #Wizard
                clear() 
                print('WIZARD CLASS:\n"Masters the use of wands and grimoires"')
                print('\nStats:\nHealth: 25\nDefense: \nStamina: \nWeight: \nStrength: \nIntelligence: \nMagic: \nStealth: \nLuck')
                go_back = input('\nPress ENTER to Exit')
                if go_back == '':
                    clear()
                    selection()
                else:
                    clear()
                    selection()
            elif view_class == '2': #Sorcerer
                clear() 
                print('SORCERER CLASS:\n"Does not need a wand or grimoire, but needs mana"')
                print('\nStats:\nHealth: \nDefense: \nStamina: \nWeight: \nStrength: \nIntelligence: \nMagic: \nStealth: \nLuck')
                go_back = input('\nPress ENTER to Exit')
                if go_back == '':
                    clear()
                    selection()
                else:
                    clear()
                    selection()
            elif view_class == '3': #Knight
                clear() 
                print('KNIGHT CLASS:\n"An Overall balanced class"')
                print('\nStats:\nHealth: 25\nDefense: \nStamina: \nWeight: \nStrength: \nIntelligence: \nMagic: \nStealth: \nLuck')
                go_back = input('\nPress ENTER to Exit')
                if go_back == '':
                    clear()
                    selection()
                else:
                    clear()
                    selection()
            elif view_class == '4': #Samurai
                clear() 
                print('SAMURAI CLASS:\n"Better with two handed weapons and has lots of stamina"')
                print('\nStats:\nHealth: 25\nDefense: \nStamina: \nWeight: \nStrength: \nIntelligence: \nMagic: \nStealth: \nLuck')
                go_back = input('\nPress ENTER to Exit')
                if go_back == '':
                    clear()
                    selection()
                else:
                    clear()
                    selection()
            elif view_class == '5': #Ninja
                clear() 
                print('NINJA CLASS:\n"Agile, fast and extreamly stealthy"')
                print('\nStats:\nHealth: 25\nDefense: \nStamina: \nWeight: \nStrength: \nIntelligence: \nMagic: \nStealth: \nLuck')
                go_back = input('\nPress ENTER to Exit')
                if go_back == '':
                    clear()
                    selection()
                else:
                    clear()
                    selection()
            elif view_class == '6': #Archer
                clear() 
                print('ARCHER CLASS:\n"Has more stamina and is harder to detect"')
                print('\nStats:\nHealth: 25\nDefense: \nStamina: \nWeight: \nStrength: \nIntelligence: \nMagic: \nStealth: \nLuck')
                go_back = input('\nPress ENTER to Exit')
                if go_back == '':
                    clear()
                    selection()
                else:
                    clear()
                    selection()
            elif view_class == '7': #Tank
                clear() 
                print('TANK CLASS:\n"Can use heavier armors and weapons"')
                print('\nStats:\nHealth: 25\nDefense: \nStamina: \nWeight: \nStrength: \nIntelligence: \nMagic: \nStealth: \nLuck')
                go_back = input('\nPress ENTER to Exit')
                if go_back == '':
                    clear()
                    selection()
                else:
                    clear()
                    selection()
            elif view_class == '8': #Brainiac
                clear() 
                print('BRAINIAC CLASS:\n"High Intelligence and charisma. Also has increased luck"')
                print('\nStats:\nHealth: 25\nDefense: \nStamina: \nWeight: \nStrength: \nIntelligence: \nMagic: \nStealth: \nLuck')
                go_back = input('\nPress ENTER to Exit')
                if go_back == '':
                    clear()
                    selection()
                else:
                    clear()
                    selection()
            elif view_class == '9': #Mechanic
                clear() 
                print('MECHANIC CLASS:\n"Makes use of sentries and golems"')
                print('\nStats:\nHealth: 25\nDefense: \nStamina: \nWeight: \nStrength: \nIntelligence: \nMagic: \nStealth: \nLuck')
                go_back = input('\nPress ENTER to Exit')
                if go_back == '':
                    clear()
                    selection()
                else:
                    clear()
                    selection()

        elif choose_class == '1':
            clear()
            print('You have choosen the WIZARD as your class.\nAre you sure you want this class?(NOTE:This cannot be changed latter!)')
            confirm_choosen_class = input('Press ENTER to confirm or type No to choose another class: ')
            if confirm_choosen_class == '':
                selected_class = 'Wizard'
                clear()
                print(f'You have choosen {selected_class}!')
                time.sleep(1)
                clear()
                return selected_class
            else:
                clear()
                selection() 
            
        elif choose_class == '2':
            print('You have choosen the Scorcerer as your class.\nAre you sure you want this class?(NOTE:This cannot be changed latter!)')
            confirm_choosen_class = input('Press ENTER to confirm or type No to choose another class: ')
            if confirm_choosen_class == '':
                selected_class = 'Scorcerer'
                clear()
                print(f'You have choosen {selected_class}!')
                time.sleep(2)
                clear()
                return selected_class
            else:
                clear()
                selection() 
            
        elif selected_class == '3':
            print('You have choosen the Knight as your class.\nAre you sure you want this class?(NOTE:This cannot be changed latter!)')
            confirm_choosen_class = input('Press ENTER to confirm or type No to choose another class: ')
            if confirm_choosen_class == '':
                selected_class = 'Knight'
                clear()
                print(f'You have choosen {selected_class}!')
                time.sleep(2)
                clear()
                return selected_class
            else:
                clear()
                selection() 
            
        elif selected_class == '4':
            print('You have choosen the Samurai as your class.\nAre you sure you want this class?(NOTE:This cannot be changed latter!)')
            confirm_choosen_class = input('Press ENTER to confirm or type No to choose another class: ')
            if confirm_choosen_class == '':
                selected_class = 'Samurai'
                clear()
                print(f'You have choosen {selected_class}!')
                time.sleep(2)
                clear()
                return selected_class
            else:
                clear()
                selection() 
            
        elif selected_class == '5':
            print('You have choosen the Ninja as your class.\nAre you sure you want this class?(NOTE:This cannot be changed latter!)')
            confirm_choosen_class = input('Press ENTER to confirm or type No to choose another class: ')
            if confirm_choosen_class == '':
                selected_class = 'Ninja'
                clear()
                print(f'You have choosen {selected_class}!')
                time.sleep(2)
                clear()
                return selected_class
            else:
                clear()
                selection() 
            
        elif selected_class == '6':
            print('You have choosen the Archer as your class.\nAre you sure you want this class?(NOTE:This cannot be changed latter!)')
            confirm_choosen_class = input('Press ENTER to confirm or type No to choose another class: ')
            if confirm_choosen_class == '':
                selected_class = 'Archer'
                clear()
                print(f'You have choosen {selected_class}!')
                time.sleep(2)
                clear()
                return selected_class
            else:
                clear()
                selection() 
            
        elif selected_class == '7':
            print('You have choosen the Tank as your class.\nAre you sure you want this class?(NOTE:This cannot be changed latter!)')
            confirm_choosen_class = input('Press ENTER to confirm or type No to choose another class: ')
            if confirm_choosen_class == '':
                selected_class = 'Tank'
                clear()
                
                print(f'You have choosen {selected_class}!')
                time.sleep(2)
                clear()
                return selected_class
            else:
                clear()
                selection() 
            
        elif selected_class == '8':
            print('You have choosen the Brainiac as your class.\nAre you sure you want this class?(NOTE:This cannot be changed latter!)')
            confirm_choosen_class = input('Press ENTER to confirm or type No to choose another class: ')
            if confirm_choosen_class == '':
                selected_class = 'Brainiac'
                clear()
                print(f'You have choosen {selected_class}!')
                time.sleep(2)
                clear()
                return selected_class
            else:
                clear()
                selection() 
            
        elif selected_class == '9':
            print('You have choosen the Mechanic as your class.\nAre you sure you want this class?(NOTE:This cannot be changed latter!)')
            confirm_choosen_class = input('Press ENTER to confirm or type No to choose another class: ')
            if confirm_choosen_class == '':
                selected_class = 'Mechanic'
                clear()
                print(f'You have choosen {selected_class}!')
                time.sleep(2)
                clear()
                return selected_class
            else:
                clear()
                selection() 

def stats():
#keeps track of individual stats for classes
    selected_class = selection()

    global health
    global defense
    global stamina
    global weight
    global strength
    global intelligence
    global magic
    global stealth
    global luck
    global elemental

    global weapon
    global first_weapon
    global weapon_value
    global current_weapon_damage
    global weapon_elemental_check

    if selected_class == 'Wizard':
        health = 25
        defense = 10
        stamina = 20
        weight = 15
        strength = 10
        intelligence = 20
        magic = 10
        elemental = .10
        stealth = 20
        luck = 1

        weapon = 'Basic Wand'
        weapon_value = 20
        current_weapon_damage = 10
        weapon_elemental_check = 0
        first_weapon = weapon
        print(weapon,weapon_value,current_weapon_damage)
        move_speed = 20
    elif selected_class == 'Sorcerer':
        health = 0
        defence = 0
        stamina = 0
        weight = 0
        strength = 0
        intelligence = 0
        magic = 0
        stealth = 0
        luck = 1
        move_speed = 0
    elif selected_class == 'Knight':
        health = 0
        defence = 0
        stamina = 0
        weight = 0
        strength = 0
        intelligence = 0
        magic = 0
        stealth = 0
        luck = 1
        move_speed = 0
    elif selected_class == 'Samurai':
        health = 0
        defence = 0
        stamina = 0
        weight = 0
        strength = 0
        intelligence = 0
        magic = 0
        stealth = 0
        luck = 1
        move_speed = 0
    elif selected_class == 'Ninja':
        health = 0
        defence = 0
        stamina = 0
        weight = 0
        strength = 0
        intelligence = 0
        magic = 0
        stealth = 0
        luck = 1
        move_speed = 0
    elif selected_class == 'Archer':
        health = 0
        defence = 0
        stamina = 0
        weight = 0
        strength = 0
        intelligence = 0
        magic = 0
        stealth = 0
        luck = 1
        move_speed = 0
    elif selected_class == 'Tank':
        health = 0
        defence = 0
        stamina = 0
        weight = 0
        strength = 0
        intelligence = 0
        magic = 0
        stealth = 0
        luck = 1
        move_speed = 0
    elif selected_class == 'Brainiac':
        health = 0
        defence = 0
        stamina = 0
        weight = 0
        strength = 0
        intelligence = 0
        magic = 0
        stealth = 0
        luck = 1
        move_speed = 0
    elif selected_class == 'Mechanic':
        health = 0
        defence = 0
        stamina = 0
        weight = 0
        strength = 0
        intelligence = 0
        magic = 0
        stealth = 0
        luck = 1
        move_speed = 0
    
def trait_selection():
    global trait 
    pick_trait = input('Choose one these choices to add to your stat points: \n1.Sneaky\n2.Quick\n3.Strong\n4.Endurance\n5.Naturalist\n6.Wise\nEnter the number of your choice: ')
    if pick_trait == '1':
        global stealth
        stealth = stealth + 5
        trait = 'Sneaky'
    elif pick_trait == '2':
        trait = 'Quick'
        print('this trait is not yet developed :( sorry )')
        pass #attack speed and extra move speed
    elif pick_trait == '3':
        global strength
        strength = strength + 5
        trait = 'Strong'
    elif pick_trait == '4': 
        global weight #max stamina and stamina regeneration
        weight = weight + 5
        trait = 'Endurance'
    elif pick_trait =='5':
        global magic
        global elemental
        magic = magic + 1
        elemental = elemental + .10
        trait = 'Naturalist'
    elif pick_trait == '6':
        global intelligence
        intelligence = intelligence + 5
        trait = 'Wise'
    clear()
    print(f'You choose the {trait} trait')
    time.sleep(1)
    clear()

def print_stats():
    global username
    username = input('What is your name?: ')
    print(f'Stats:\nHealth: {health}\nDefense: {defense}\nWeight: {weight}\nStrength: {strength}\nIntelligence: {intelligence}\nMagic: {magic}\nStealth: {stealth}')


#----inventory----#
gold = 200

weapon = ''
weapon_value = 0
current_weapon_damage = 0
weapon_elemental_check = 0

health_potion_count = 0
mana_potion_count = 0

player_level = 1
player_exp = 0
#----inventory----#


#----Stat-Tracker----#
health = 0
defense = 0
stamina = 0
weight = 0
strength = 0
intelligence = 0
magic = 0
stealth = 0
luck = 0

trait = ''
#----Stat-Tracker----#

stats()
trait_selection()
print_stats()
