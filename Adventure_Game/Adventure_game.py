import random
import time
import pygame
#import game1 
from mini_game import *
import os

clear = lambda: os.system('cls')

random_weapon = 0

#----inventory----#

gold = 200

off_hand_list = []
owned_off_hand = []
weapons_owned = [['No Weapon', 10, 0, 1]]
weapons_list = [] 

weapon = 'Basic Wand'
first_weapon = ''

off_hand = 'Basic Katana'
single_wield = True

weapon_value = 0
first_weapon_value = 0
off_hand_value = 0

off_hand_multiplier = 0

current_weapon_damage = 0  
weapon_elemental_check = 0
critical_hit_chance = 0

health_potion_count = 0
mana_potion_count = 0

#----inventory----#


#----Stat-Tracker----# 
username = ''.capitalize()
selected_class = ''

starting_health = 0
health = 0
defense = 0
stamina = 0
weight = 0
strength = 0
intelligence = 0
magic = 0
elemental = .10
stealth = 0
luck = 0

trait = ''

player_level = 1
player_exp = 0
exp_progress = 235
perk_count = 0
#----Stat-Tracker----#


#----Monster-Stats----#
damage_per_hit = 0
exp_dropped = 0
monster_health = 0
max_monster_health = 0
monster_lvl = 0
#----Monster-Stats----#


#----Is-Game-Running----#
running = True
#----Is-Game-Running----#

#----Settings----#
text_timer = 2
#----Settings----#

def settings():

    global text_timer
    global running

    settings_ui = input(f'Settings:\n1.Time Between text\n2.Use Perks\n3.View xp Progress\n4.Swap Weapons\n5.Toggle Two Hand Weilding: {single_wield}\n6.Tutorial\n7.Leave Game\nInput: ')

    if settings_ui == '1':
        time_between_text = (input('How long would you like the time between text to be? (in seoonds): '))
        time_between_text = int(time_between_text)
        text_timer = time_between_text
        print(f'Time set to: {text_timer}(s)')
        time.sleep(text_timer)
        clear()
        second_scene()
    
    elif settings_ui == '2':
        clear()
        use_perks()

    elif settings_ui == '3':
        clear()
        view_level()
    
    elif settings_ui == '4':
        clear()
        weapons_purchased()
    
    elif settings_ui == '5':
        clear()
        two_hand_toggle()

    elif settings_ui == '6':
        clear()
        tutorial()

    elif settings_ui == '7':
        running = False

    else:
        clear()
        settings()

def two_hand_toggle():
    global single_wield
    if single_wield == True:
        single_wield = False
    elif single_wield == False:
        single_wield = True

def selection():

    global selected_class

    clear()

    selected_class = '-'

    while selected_class == '-':

        print("Choose a Class(1-9):\nOr to see the details of a class press ENTER\n---------------------------------------\n1.Wizard\n2.Scorcer\n3.Knight\n4.Samurai\n5.Ninja\n6.Archer\n7.Tank\n8.Brainiac\n9.Mechanic\n---------------------------------------")
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
                clear()
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
                clear()
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
                clear()
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
                clear()
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
                clear()
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
                clear()
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
                clear()
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
                clear()
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
                clear() 
                if go_back == '':
                    clear()
                    selection()
                else:
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
        
        else:
            clear()
            selection

def stats():
#keeps track of individual stats for classes
    selected_class = selection()

    global starting_health
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

    global first_weapon_value
    global weapon
    global first_weapon
    global weapon_value
    global current_weapon_damage
    global weapon_elemental_check

    if selected_class == 'Wizard':

#starting stat points is 75 points per class
        starting_health = 25
        health = 25
        defense = 10
        #stamina = 20
        #weight = 15
        strength = 5
        intelligence = 20
        magic = 15

        elemental = .10
        #stealth = 20
        luck = 10

        weapon = 'Basic Wand'
        weapon_value = 20
        current_weapon_damage = 10
        weapon_elemental_check = 0
        first_weapon = weapon
        first_weapon_value = weapon_value
        #move_speed = 20

    elif selected_class == 'Sorcerer':
        #same as wizard
        starting_health = 25
        health = 25
        defense = 10
        #stamina = 20
        #weight = 15
        strength = 10
        intelligence = 20
        magic = 10
        
        elemental = .10
        #stealth = 20
        luck = 10

        weapon = 'Basic Attunement'
        weapon_value = 20
        current_weapon_damage = 10
        weapon_elemental_check = 0
        first_weapon = weapon
        first_weapon_value = weapon_value
        ##move_speed = 20

    elif selected_class == 'Knight':
        
        starting_health = 25
        health = 25
        defense = 10
        #stamina = 20
        #weight = 15
        strength = 10
        intelligence = 20
        magic = 10
        
        elemental = .10
        #stealth = 20
        luck = 10

        weapon = 'Basic Sword'
        weapon_value = 20
        current_weapon_damage = 10
        weapon_elemental_check = 1
        first_weapon = weapon
        first_weapon_value = weapon_value
        #move_speed = 20
        
    elif selected_class == 'Samurai':
        
        starting_health = 25
        health = 25
        defense = 10
        #stamina = 20
        #weight = 15
        strength = 10
        intelligence = 20
        magic = 10
        
        elemental = .10
        #stealth = 20
        luck = 10

        weapon = 'Basic Katana'
        weapon_value = 20
        current_weapon_damage = 10
        weapon_elemental_check = 1
        first_weapon = weapon
        first_weapon_value = weapon_value
        #move_speed = 20
        
    elif selected_class == 'Ninja':
        
        starting_health = 25
        health = 25
        defense = 10
        #stamina = 20
        #weight = 15
        strength = 10
        intelligence = 20
        magic = 10
        
        elemental = .10
        #stealth = 20
        luck = 10

        weapon = 'Basic Kunai'
       #ammo = 'Basic Kunai'
        weapon_value = 20
        current_weapon_damage = 10
        weapon_elemental_check = 1
        first_weapon = weapon
        first_weapon_value = weapon_value
        #move_speed = 20
        
    elif selected_class == 'Archer':
        
        starting_health = 25
        health = 25
        defense = 10
        #stamina = 20
        #weight = 15
        strength = 10
        intelligence = 20
        magic = 10
        
        elemental = .10
        #stealth = 20
        luck = 10

        weapon = 'Basic Bow'
        #ammo = 'Basic Arrow'
        weapon_value = 20
        current_weapon_damage = 10
        weapon_elemental_check = 1
        first_weapon = weapon
        first_weapon_value = weapon_value
        #move_speed = 20
        
    elif selected_class == 'Tank':
        
        starting_health = 25
        health = 25
        defense = 10
        #stamina = 20
        #weight = 15
        strength = 10
        intelligence = 20
        magic = 10
        
        elemental = .10
        #stealth = 20
        luck = 10

        weapon = 'Basic Shield'
        weapon_value = 20
        current_weapon_damage = 10
        weapon_elemental_check = 1
        first_weapon = weapon
        first_weapon_value = weapon_value
        #move_speed = 20
        
    elif selected_class == 'Brainiac':
        
        starting_health = 25
        health = 25
        defense = 10
        #stamina = 20
        #weight = 15
        strength = 10
        intelligence = 20
        magic = 10
        
        elemental = .10
        #stealth = 20
        luck = 10

        weapon = 'Telekinesis'
        weapon_value = 20
        current_weapon_damage = 10
        weapon_elemental_check = 1
        first_weapon = weapon
        first_weapon_value = weapon_value
        #move_speed = 20
        
    elif selected_class == 'Mechanic':
        
        starting_health = 25
        health = 25
        defense = 10
        #stamina = 20
        #weight = 15
        strength = 10
        intelligence = 20
        magic = 10
        
        elemental = .10
        #stealth = 20
        luck = 10

        weapon = 'Copper Turret'
        weapon_value = 20
        current_weapon_damage = 10
        weapon_elemental_check = 1
        first_weapon = weapon
        first_weapon_value = weapon_value
        #move_speed = 20
        
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
        time.sleep(text_timer)
        clear()
        trait_selection()
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
    else:
        clear()
        trait_selection()
    clear()
    print(f'You choose the {trait} trait')
    __continue__ = input('Press ENTER to continue: ')
    clear()

def print_stats():
    global username
    username = input('--------------------\nWhat is your name?: ')
    print(f'---------------------\nStats:\nHealth: {health}\nDefense: {defense}\nWeight: {weight}\nStrength: {strength}\nIntelligence: {intelligence}\nMagic: {magic}\nStealth: {stealth}\n---------------------')
    __continue__ = input('Press ENTER to continue: ')
    clear()

def tutorial():
    player_tutorial = input('Would you like to take the tutorial explaing how to play the game or would you like to skip it? \nPress ENTER to take tutorial, or enter SKIP to skip: ').lower()
    if player_tutorial == '':
        clear()
        first_tutorial = input('When given a promp it is important if there is a list of options with numbers adjacent, for example: \n1.option one\n2.option two\n3.option three\nIf the menu looks like this you enter the coressponding number you want and press ENTER.\nPress ENTER to continue: ')
        clear()
        second_tutorial = input('If the menu gives you a list like this: (Option One, Option Two, Option Three): \ntype out the action you want and press enter. For example: option one\nPress ENTER to continue: ')
        clear()
        third_tutorial = input('In the mines you are given 4 actions: straight(w), left(a), right(d), and leave(s)\nType the letter next to the action you want and press enter.\nPress ENTER to continue: ')
        clear()
        fourth_tutorial = input('Thats everything you need to know for now, Good luck!\nPress ENTER to continue: ')
    elif player_tutorial == 'skip':
        clear()
        skip_tutorial = input('You can always access the tutorial in the settings menu later\n--------------------------------------------------------------\nPress ENTER to continue: ')
        clear()
    else:
        clear()
        tutorial()

def damage_calculator():
    
    global single_wield
    global off_hand
    global current_weapon_damage
    global weapon_elemental_check
    global elemental
    global damage_output

    global monster_health
    if off_hand != '':
        if weapon_elemental_check == 0:
            damage_output = current_weapon_damage + (current_weapon_damage * elemental) + (current_weapon_damage * off_hand)
            #print(f'current damage {current_weapon_damage}')
            crit_chance = random.randint(0, critical_hit_chance)
            if crit_chance == 1:
                damage_output += (damage_output * .30)
                print('Crit!')
        elif weapon_elemental_check == 1:
            damage_output = current_weapon_damage + (current_weapon_damage * off_hand)
            crit_chance = random.randint(0, critical_hit_chance)
            if crit_chance == 1:
                damage_output += (damage_output * .30)
    elif off_hand == '' and single_wield == True:
        if weapon_elemental_check == 0:
            damage_output = current_weapon_damage + (current_weapon_damage * elemental) + (current_weapon_damage * 0.8)
            #print(f'current damage {current_weapon_damage}')
            crit_chance = random.randint(0, critical_hit_chance)
            if crit_chance == 1:
                damage_output += (damage_output * .30)
                print('Crit!')
        elif weapon_elemental_check == 1:
            damage_output = current_weapon_damage + (current_weapon_damage * 0.8)
            crit_chance = random.randint(0, critical_hit_chance)
            if crit_chance == 1:
                damage_output += (damage_output * .30)

def view_level():
    global exp_progress
    global player_exp
    global player_level
    global perk_count
    if player_exp >= exp_progress:
        exp_progress = (exp_progress + (exp_progress / 5))
        exp_progress = round(exp_progress)
        player_level += 1
        perk_count += 1
    print(f'Player Level: {player_level}\nNext level: {player_exp}/{exp_progress}')
    print(f'Available Perk Points: {perk_count}')
    __continue__ = input('Press ENTER to continue: ')
    clear()
    second_scene()

def level_increase():
    
    global gold
    global exp_progress
    global player_exp
    global player_level
    global perk_count
    if player_exp >= exp_progress:
        exp_progress = (exp_progress + (exp_progress / 5))
        exp_progress = round(exp_progress)
        player_level += 1
        perk_count += 1
    print(f'---------------------------\nPlayer Level: {player_level}  Gold: {gold}g\nNext level: {player_exp}/{exp_progress}')
    print(f'Available Perk Points: {perk_count}\n---------------------------')

def stat_view():
    global username
    global gold
    global exp_progress
    global player_exp
    global player_level
    global health
    global starting_health
    global perk_count
    if player_exp >= exp_progress:
        exp_progress = (exp_progress + (exp_progress / 5))
        exp_progress = round(exp_progress)
        player_level += 1
        perk_count += 1
    print(f'---------------------------\nPlayer Level: {player_level}  Gold: {gold}g\nNext level: {player_exp}/{exp_progress}')
    print(f"Available Perk Points: {perk_count}\n{username}'s Health: {health}/{starting_health}\n---------------------------")

def use_perks():
    global perk_count

    global health
    global defense
    global stamina
    global weight
    global strength
    global intelligence
    global magic
    global stealth

    apply_perk = input(f'Select a stat to improve: \nHealth: {health}\nDefense: {defense}\nWeight: {weight}\nStrength: {strength}\nIntelligence: {intelligence}\nMagic: {magic}\nStealth: {stealth}\n------------\nPoints: {perk_count}\nPress ENTER to go back\nInput: ').lower()
    if perk_count >= 1:
        if apply_perk == 'health':
            health += 1
            starting_health += 1
            perk_count -= 1
        elif apply_perk == 'defense':
            defense += 1
            perk_count -= 1
        elif apply_perk == 'weight':
            weight += 1
            perk_count -= 1
        elif apply_perk == 'strength':
            strength += 1
            perk_count -= 1
        elif apply_perk == 'intelligence':
            intelligence += 1
            perk_count -= 1
        elif apply_perk == 'magic':
            magic += 1
            perk_count -= 1
        elif apply_perk == 'stealth':
            stealth += 1
            perk_count -= 1
        elif apply_perk == '':
            clear()
            print('leaving in 3...')
            time.sleep(1)
            clear()
            print('leaving in 2...')
            time.sleep(1)
            clear()
            print('leaving in 1...')
            time.sleep(1)
            clear()
            second_scene()
        else:
            clear()
            use_perks()

    elif apply_perk == '':
            clear()
            print('leaving in 3...')
            time.sleep(1)
            clear()
            print('leaving in 2...')
            time.sleep(1)
            clear()
            print('leaving in 1...')
            time.sleep(1)
            clear()
            second_scene()
    else:
        clear()
        print('You have no Perk Points right now')
        time.sleep(text_timer)
        clear()
        second_scene()

    clear()
    print(f'New stats:\nHealth: {health}\nDefense: {defense}\nWeight: {weight}\nStrength: {strength}\nIntelligence: {intelligence}\nMagic: {magic}\nStealth: {stealth}\nInput: ')

def weapon_list_function():

    global weapons_list
    global random_weapon_choosen
    global random_weapon

#copy and paste list#
#    ['Basic', 10, 15, 1],['Common', 15, 25, 1],['Uncommon', 20, 40, 1],['Rare', 25, 55, 1],['Ultra Rare', 30, 70, 1],['Legendary', 40, 90, 1],['Mythical', 50, 150, 1],    #
    def closing_tab():
        #    Rarity  | Damage | Value | Elemental |  
        #  ----------|--------|-------|-----------|
        # Basic      |   10   |  15   |    n/a    |    
        # Common     |   15   |  25   |    n/a    |         
        # Uncommon   |   20   |  40   |    n/a    |
        # Rare       |   25   |  55   |    n/a    |        
        # Ultra Rare |   30   |  70   |    n/a    |        
        # Legendary  |   40   |  90   |    n/a    |        
        # Mythical   |   50   |  150  |    n/a    |        
        # *Unique*   |   65   |   ?   |    n/a    |        
        #============|========|=======|===========|
        # Weapon types: main hand: Wand, Attunement, Sword, Katana, Kunai, Bow, Shield, Telekinesis, Golem
        # Weapon Types: off Hand:  grimoire, None, shield, katana, shuriken, arrow, shield, none, support golem(might change this one)  
        # Unique's:     
        pass
#weapon - damage - value - elemental check(0 = yes, 1 = no)       ------LIST OF ALL WEAPONS EXCEPT FOR UNIQUES------
    weapons_list = [['Basic Wand', 10, 15, 1],['Common Wand', 15, 25, 1],['Uncomon Wand', 20, 40, 1],['Rare Wand', 25, 55, 0],['Ultra Rare Wand', 30, 70, 0],['Legendary Wand', 40, 90, 0],['Mythical Wand', 50, 150, 0],['Basic Attunement', 10, 15, 1],['Common Attunement', 15, 25, 1],['Uncommon Attunement', 20, 40, 1],['Rare Attunement', 25, 55, 1],['Ultra Rare Attunement', 30, 70, 1],['Legendary Attunement', 40, 90, 1],['Mythical Attunement', 50, 150, 1],['Basic Sword', 10, 15, 1],['Common Sword', 0, 25, 1],['Uncommon Sword', 0, 40, 1],['Rare Sword', 0, 55, 1],['Ultra Rare Sword', 0, 70, 1],['Legendary Sword', 0, 90, 1],['Mythical Sword', 0, 150, 1],['Basic Katana', 10, 15, 1],['Common Katana', 15, 25, 1],['Uncommon Katana', 20, 40, 1],['Rare Katana', 25, 55, 1],['Ultra Rare Katana', 30, 70, 1],['Legendary Katana', 40, 90, 1],['Mythical Katana', 50, 150, 1],['Basic Kunai', 10, 15, 1],['Common Kunai', 15, 25, 1],['Uncommon Kunai', 20, 40, 1],['Rare Kunai', 25, 55, 1],['Ultra Rare Kunai', 30, 70, 1],['Legendary Kunai', 40, 90, 1],['Mythical Kunai', 50, 150, 1],['Basic Bow', 10, 15, 1],['Common Bow', 15, 25, 1],['Uncommon Bow', 20, 40, 1],['Rare Bow', 25, 55, 1],['Ultra Rare Bow', 30, 70, 1],['Legendary Bow', 40, 90, 1],['Mythical Bow', 50, 150, 1],['Basic Shield', 10, 15, 1],['Common Shield', 15, 25, 1],['Uncommon Shield', 20, 40, 1],['Rare Shield', 25, 55, 1],['Ultra Rare Shield', 30, 70, 1],['Legendary Shield', 40, 90, 1],['Mythical Shield', 50, 150, 1]]

    random_weapon = random.randint(0,len(weapons_list)-1)

    random_weapon_choosen = weapons_list[random_weapon][0] + ' | ' + 'Damage: ' + str(weapons_list[random_weapon][1]) + ' | ' + str(weapons_list[random_weapon][2]) + ''
    random_weapon = weapons_list[random_weapon]
    return random_weapon_choosen

def off_hand_weapon():

    global off_hand_list
    global off_hand_chosen
    global random_off_hand
    
    # weapon -- damage multiplier -- value
    off_hand_list = [['Basic Katana', .05, 15],['Common Katana', .06, 25],['Uncommon Katana', .07, 40],['Rare Katana', .08, 55],['Ultra Rare Katana', .09, 70],['Legendary Katana', .10, 90],['Mythical Katana', .11, 150]]

    random_off_hand = random.randint(0,len(off_hand_list)-1)

    off_hand_chosen = 'Off Hand ' + off_hand_list[random_off_hand][0] + ' | ' + 'Damage: ' + str(off_hand_list[random_off_hand][1]) + ' | ' + str(off_hand_list[random_off_hand][2]) + 'g'
    
    return off_hand_chosen

def weapons_purchased():

    global off_hand
    global owned_off_hand
    global off_hand_list
    global off_hand_value
    global off_hand_multiplier

    global weapons_list
    global weapon
    global weapon_value
    global current_weapon_damage
    global weapon_elemental_check
    global weapons_owned

    level_increase()
    if weapon == '':
        weapon_list_function() 
        for i in range(0,len(weapons_owned)):
            print(f'{i+1}.{weapons_owned[i][0]}')
        swap_to_weapon = int(input('What weapon would you like to select?: '))
        try:
            swap_to_weapon = int(swap_to_weapon)
            if swap_to_weapon > len(weapons_owned) or swap_to_weapon < 1:
                print('That is not an available option')
                time.sleep(text_timer)
                clear()
                weapons_purchased() 
            else:   
                for i in range(0,len(weapons_list)-1):
                    if weapons_list[i][0] == weapon:
                        weapons_owned.append(weapons_list[i])
                        weapon = ''
                        print(f'You have changed your weapon to: {weapon}')        
                weapon = weapons_owned[swap_to_weapon-1][0]
                current_weapon_damage = weapons_owned[swap_to_weapon-1][1]
                weapon_value = weapons_owned[swap_to_weapon-1][2]
                weapon_elemental_check = weapons_owned[swap_to_weapon-1][3]
                for i in range(0,len(weapons_owned)):
                    if weapons_owned[i][0] == weapon:
                        print('yay')
                        weapons_owned.remove(weapons_owned[i])
                    else:
                        print('error')
        except ValueError:
            print('Please enter a number')
            time.sleep(text_timer)
            clear()
    else:
        off_or_main = input('Would you like to store an\n1.Main Hand Weapon\n2.Off Hand Item\nINPUT: ')
        if off_or_main == '1':
#storing weapon
            store_weapon = input(f'Whould you like to store current weapon ({weapon})?: ').lower()
            if store_weapon == 'yes':
                weapon_list_function()
                for i in range(0,len(weapons_list)-1):
                    if weapons_list[i][0] == weapon:
                        weapons_owned.append(weapons_list[i])
                        weapon = ''
#sawpping weapon
            elif store_weapon == 'no':
                weapon_list_function() 
                swap_weapon = input('Would you like to swap weapons?: ')
                if swap_weapon == 'yes':
                    for i in range(0,len(weapons_owned)):
                        print(f'{i+1}.{weapons_owned[i][0]}')
                    swap_to_weapon = (input('What weapon would you like to swap to?: '))
                    try:
                        swap_to_weapon = int(swap_to_weapon)
                        if swap_to_weapon > len(weapons_owned) or swap_to_weapon < 1:
                            print('That is not an available option')
                            time.sleep(text_timer)
                            clear()
                            weapons_purchased()
                        else:   
                            for i in range(0,len(weapons_list)-1):
                                if weapons_list[i][0] == weapon:
                                    weapons_owned.append(weapons_list[i])
                                    weapon = ''       
                            weapon = weapons_owned[swap_to_weapon-1][0]
                            current_weapon_damage = weapons_owned[swap_to_weapon-1][1]
                            weapon_value = weapons_owned[swap_to_weapon-1][2]
                            weapon_elemental_check = weapons_owned[swap_to_weapon-1][3]
                            for i in range(0,len(weapons_owned)-1):
                                if weapons_owned[i][0] == weapon:
                                    weapons_owned.remove(weapons_owned[i])
                            print(f'You have changed your weapon to: {weapon}') 
                            time.sleep(text_timer)
                            clear()
                    except ValueError:
                        clear()
                        print('Please enter the number listed next to your desired weapon')
                        time.sleep(text_timer)
                        clear()
                        weapons_purchased()
#storing off hand                       
        elif off_or_main == '2':
            if off_hand != '':
                store_off_hand = input('Would you like to store off hand item?: ').lower()
                if store_off_hand == 'yes':
                    off_hand_weapon()
                    for i in range(len(off_hand_list)-1):
                        if off_hand_list[i][0] == off_hand:
                            owned_off_hand.append(off_hand_list[i])
                            off_hand = ''
                            off_hand_value = 0
                            off_hand_multiplier = 0
#swapping off hand                            
                elif store_off_hand == 'no':
                    swap_off_hand = input('Would you like to swap to a different off hand item?: ').lower()
                    if swap_off_hand == 'yes':
                        off_hand_weapon()
                        for i in range(len(owned_off_hand)):
                            print(f'{i+1}.{owned_off_hand[i][0]}')
                        swap_off_hand = input('Which item would you like to equip?: ')
                        try: 
                            swap_off_hand = int(swap_off_hand)
                            if swap_off_hand > len(owned_off_hand) or swap_off_hand < 1:
                                print('That is not an available option')
                                time.sleep(text_timer)
                                clear()
                                weapons_purchased()
                            else:
                                for i in range(len(off_hand_list)-1):
                                    if off_hand_list[i][0] == off_hand:
                                        owned_off_hand.append(off_hand_list[i])
                                    off_hand = owned_off_hand[swap_off_hand-1][0]
                                    off_hand_value = owned_off_hand[swap_off_hand-1][1]
                                    off_hand_multiplier = owned_off_hand[swap_off_hand-1][2]
                                    for i in range(len(owned_off_hand)-1):
                                        if owned_off_hand[i][0] == off_hand:
                                            owned_off_hand.remove(owned_off_hand[i])
                                print(f'You have changed your off hand to: {off_hand}')
                                time.sleep(text_timer)
                                clear()
                        except ValueError:
                            clear()
                            print('Please enter the number listed next to your desired weapon')
                            time.sleep(text_timer)
                            clear()
                            weapons_purchased()

        else:
            clear()  

def store():

    global weapons_owned
    global weapons_list 
    global first_weapon
    global first_weapon_value
    global weapon_value
    global current_weapon_damage
    global weapon_elemental_check
    global weapon
    global gold
    global health_potion_count

    clear()
    level_increase()

#prints UI for Buying items
    print('Upon arriving at the store the clerk welcomes you and shows you his wares, look like he has a number of useful items;')
    print('------------------------------------------------------')
    purchase = input(f'Store items:                     Gold: {gold}g\n1.Health Potion 40g | Health Potions Owned: {health_potion_count}\n2.{first_weapon} {first_weapon_value}g\n3.Sell items\n------------------------------------------------------\nPress ENTER to leave store\nINPUT: ')

    if purchase == '1':
        if gold >= 40:
            health_potion_count += 1
            gold = gold - 40
            clear()
            level_increase()
            store()

    elif purchase == '2':
        if gold >= 15 and weapon == '':
            for i in range(0,len(weapons_list)-1):
                if weapons_list[i][0] == first_weapon:
                    weapons_owned.append(weapons_list[i])
            gold -= 15 # All first weapons will have value of 15g
            print(f'You bought {first_weapon}')
            time.sleep(text_timer)
            clear()
            level_increase()
            store()

    elif purchase == '3':

        clear()
        weapon_list_function()
        level_increase()
#prints UI for selling items
        print(f'What items do you wish to sell?: \n---------------------------------\n1.Health Potion 40g | Owned: {health_potion_count}')
        for i in range(0,len(weapons_owned)):
            print(f'{i+2}.{weapons_owned[i][0]} {weapons_owned[i][2]}g')
        print(f'{len(weapons_owned)+2}.{weapon} {weapon_value}g')
        sell_items = input('---------------------------------\nPress ENTER to go back\nINPUT: ')

        if sell_items == '1':
            if health_potion_count >= 1:
                health_potion_count -= 1
                gold += 40
                clear()
                level_increase()
                store()
            else:
                health_potion_count = 0
                clear()
                print('You have no Potions to sell')
                time.sleep(2)
                clear()
                level_increase()
                store()
#-----CHEAT COMMAND-----#
        elif sell_items == '.dev':
            clear()
            password = input('What is the password?: ')
            if password == 'wizzy':
                clear()
                add_gold = int(input('How much gold would you like to add?: '))
                gold += add_gold 
                clear()
                level_increase()
                store()
            else:
                clear()
                print('Wrong password')
                time.sleep(text_timer)
                clear()
                level_increase()
                store()

        elif sell_items == '':
            clear()
            level_increase()
            store()
#Sell weapons from inventory
        else:
            try:
                sell_items = int(sell_items)
                if len(weapons_owned)+1 < sell_items:
                    gold += weapon_value
                    weapon = ''
                    current_weapon_damage = 0
                    weapon_value = 0
                    weapon_elemental_check = 1
                    clear()
                    level_increase()
                    print(f'Weapon: {weapon}')
                    time.sleep(text_timer)
                    clear()
                elif len(weapons_owned)+1 <= sell_items:
                    gold += weapons_owned[sell_items-2][2]
                    weapons_owned.remove(weapons_owned[sell_items-2])
                    print(weapons_owned)
                else:
                    print('You do not have a weapon to sell!')
                    time.sleep(2)
                    clear()
                    level_increase()
                    store()
            except ValueError:
                print('Not a number')
#------CHEAT COMMAND------#                
    elif purchase == '.dev':
        clear()
        password = input('What is the password?: ')
        if password == 'wizzy':
            clear()
            weapon_list_function()
            add_weapon = (input('What weapon would you like?: '))
            for c in range(0,len(weapons_list)-1):
                if weapons_list[c][0] == add_weapon:
                    weapons_owned.append(weapons_list[c])
            print(f'Weapon added to inventory')
            for i in range(0,len(weapons_owned)):
                print(f'{i+1}.{weapons_owned[i][0]}')
            time.sleep(text_timer)
            clear()
            level_increase()
            store()
        else:
            print('Wrong password')
            time.sleep(text_timer)
            clear()
            level_increase()
            store()
#exit button 
    elif purchase == '':
        clear()
        level_increase()
        second_scene()

    else:
            clear()
            level_increase()
            store()

def mine():

    global health_potion_count
    global luck
    global exp_dropped
    global killed_monster_count

    def right_left():

        global health_potion_count
        global gold
        global player_exp

        if time_in_mine >= 20: # add express pass in future to get there faster
            next_floor = input('Do you want to go to the next floor?: ')

        else:
            path_choice = input('\nLooks like the path ahead is caved in and you need to take the right(d) path or the left(a) path: ').lower()

            if path_choice == 'right' or path_choice == 'd':
                rng_enenmy = random.randint(0,15)
                if rng_enenmy >= 0 and rng_enenmy <= 3:
                    print('You got an enemy')
                    time.sleep(1)
                    clear()
                    fight_sequence_one()

                elif rng_enenmy >= 4 and rng_enenmy <= 6:
                    rng_loot = random.randint(10,50)
                    print(f'You found {rng_loot}g')
                    gold += rng_loot

                elif rng_enenmy >= 7 and rng_enenmy <= 8:
                    rng_loot = random.randint(0,luck)
                    if rng_loot == 0:
                        print('You found two health potions!')
                        health_potion_count += 2
                    else:
                        print('You found a health potion!')
                        health_potion_count += 1
                elif rng_enenmy == 9:
                    mini_game_func()
                else:
                    print('There was nothing in this room')

                player_exp += 10
                time.sleep(2)
                clear()

            elif path_choice == 'left' or path_choice == 'a':
                rng_enenmy = random.randint(0,15)
                if rng_enenmy >= 0 and rng_enenmy <= 3:
                    print('You got an enemy')
                    time.sleep(1)
                    clear()
                    fight_sequence_one()

                elif rng_enenmy >= 4 and rng_enenmy <= 6:
                    rng_loot = random.randint(10,50)
                    print(f'You found {rng_loot}g')
                    gold += rng_loot

                elif rng_enenmy >= 7 and rng_enenmy <= 8:
                    rng_loot = random.randint(0,luck)
                    if rng_loot == 0:
                        print('You found two health potions!')
                        health_potion_count += 2
                    else:
                        print('You found a health potion!')
                        health_potion_count += 1
                else:
                    print('There was nothing in this room')
            else:
                clear()
                stat_view()
                print('Not a valid move, enter: (a) to move right or (d) to move left')
                time.sleep(text_timer)
                clear()
                stat_view()
                right_left()

            player_exp += 10
            time.sleep(2)
            clear()
            
        
    def forward_leave():

        global health_potion_count
        global gold 
        global leave 
        global player_exp

        if time_in_mine >= 20: # add express pass in future to get there faster
            next_floor = input('Do you want to go to the next floor?: ')
            
        else:
            path_choice = input('\nLooks like the only path is straight(w) ahead, do you want to turn back now?: ').lower()
            if path_choice == 'no' or path_choice == 'w':
                rng_enenmy = random.randint(0,15)
                if rng_enenmy >= 0 and rng_enenmy <= 3:
                    print('You got an enemy')
                    time.sleep(1)
                    clear()
                    fight_sequence_one()

                elif rng_enenmy >= 4 and rng_enenmy <= 8:
                    rng_loot = random.randint(0,50)
                    print(f'You found {rng_loot}g')
                    gold += rng_loot

                elif rng_enenmy >= 9 and rng_enenmy <= 12:
                    rng_loot = random.randint(0,luck)
                    if rng_loot == 0:
                        print('You found two health potions!')
                        health_potion_count += 2
                    else:
                        print('You found a health potion!')
                        health_potion_count += 1
                else:
                    print('There was nothing in this room') 

                player_exp += 10
                time.sleep(2)
                clear()

            elif path_choice == 'yes' or path_choice == 's':
                leave = ''
                print('You are leaving the mines')
                print(f'You got {gained_exp}xp')
                second_scene()
            else:
                clear()
                stat_view()
                print('Not a valid move, enter: (w) to move forward or (s) to leave')
                time.sleep(text_timer)
                clear()
                stat_view()
                forward_leave()

    leave = '-'

    time_in_mine = 0 #if this number reaches a certain number ask user if they want to go down a floor
    killed_monster_count = 0

    while leave == '-':
        
        stat_view()

        rng_path = random.randint(0,1)

        if rng_path == 0:
            right_left()

        elif rng_path == 1:
            forward_leave()

        time_in_mine += 1
        gained_exp = (time_in_mine * 10) + (killed_monster_count * exp_dropped)

        if time_in_mine == 20: # add express pass in future to get there faster
            print('20')
            pass

def blacksmith():

    global owned_off_hand
    global weapons_owned
    global first_weapon
    global current_weapon_damage
    global weapon_value
    global weapon
    global gold
    global health_potion_count

    level_increase()
    print('Upon arriving at the store the Blacksmith welcomes you and shows you his wares, look like he has a number of useful items;')
    purchase = input(f'Store items:                     Gold: {gold}g\n1.{weapon_list_function()}\n2.{off_hand_weapon()}\n3.{first_weapon} | {current_weapon_damage} | {weapon_value}g\n4.Sell items\n------------------------------\nPress ENTER to leave store\nINPUT: ')

    if purchase == '1':
        if gold >= weapons_list[random_weapon][2]:
            weapons_owned.append(weapons_list[random_weapon])
            gold = gold - weapons_list[random_weapon][2]
            clear()
            print(f'You have purchased {weapons_list[random_weapon][0]}')
            time.sleep(text_timer)
            clear()
            level_increase()
            blacksmith()
    
    elif purchase == '2':
        if gold >= off_hand_list[random_off_hand][2]:
            owned_off_hand.append(off_hand_list[random_off_hand])
            gold -= off_hand_list[random_off_hand][2]
            print(f'You have purchased {off_hand_list[random_off_hand][0]}')
            time.sleep(text_timer)
            clear()
            level_increase()
            blacksmith()

    elif purchase == '3':
        if gold >= 15 and weapon == '':
            weapon = first_weapon
            gold -= 15
            clear()
            level_increase()
            blacksmith()

    elif purchase == '4':
        clear()
        weapon_list_function()
        level_increase()
#prints UI for selling items
        print(f'What items do you wish to sell?: \n---------------------------------\n1.Health Potion 40g | Owned: {health_potion_count}')
        for i in range(0,len(weapons_owned)):
            print(f'{i+2}.{weapons_owned[i][0]} {weapons_owned[i][2]}g')
        print(f'{len(weapons_owned)+2}.{weapon} {weapon_value}g')
        sell_items = input('---------------------------------\nPress ENTER to go back\nINPUT: ')
        if sell_items == '1':
            if health_potion_count >= 1:
                health_potion_count -= 1
                gold += 40
                clear()
                level_increase()
                store()
            else:
                health_potion_count = 0
                clear()
                print('You have no Potions to sell')
                time.sleep(2)
                clear()
                level_increase()
                store()
#-----CHEAT COMMAND-----#
        elif sell_items == '.dev':
            clear()
            password = input('What is the password?: ')
            if password == 'wizzy':
                clear()
                add_gold = int(input('How much gold would you like to add?: '))
                gold += add_gold 
                clear()
                level_increase()
                store()
            else:
                clear()
                print('Wrong password')
                time.sleep(text_timer)
                clear()
                level_increase()
                store()

        elif sell_items == '':
            clear()
            level_increase()
            store()
#Sell weapons from inventory
        else:
            try:
                sell_items = int(sell_items)
                if len(weapons_owned)+1 < sell_items:
                    gold += weapon_value
                    weapon = ''
                    current_weapon_damage = 0
                    weapon_value = 0
                    weapon_elemental_check = 1
                    clear()
                    level_increase()
                    print(f'Weapon: {weapon}')
                    time.sleep(text_timer)
                    clear()
                elif len(weapons_owned)+1 <= sell_items:
                    gold += weapons_owned[sell_items-2][2]
                    weapons_owned.remove(weapons_owned[sell_items-2])
                    print(weapons_owned)
                else:
                    print('You do not have a weapon to sell!')
                    time.sleep(2)
                    clear()
                    level_increase()
                    store()
            except ValueError:
                print('Not a number')
#------CHEAT COMMAND------#                
    elif purchase == '.dev':
        clear()
        password = input('What is the password?: ')
        if password == 'wizzy':
            clear()
            weapon_list_function()
            add_weapon = (input('What weapon would you like?: '))
            for c in range(0,len(weapons_list)-1):
                if weapons_list[c][0] == add_weapon:
                    weapons_owned.append(weapons_list[c])
            print(f'Weapon added to inventory')
            for i in range(0,len(weapons_owned)):
                print(f'{i+1}.{weapons_owned[i][0]}')
            time.sleep(text_timer)
            clear()
            level_increase()
            store()
        else: 
            print('Wrong password')
            time.sleep(text_timer)
            clear()
            level_increase()
            store()

    elif purchase == '':
        clear()
        level_increase()
        second_scene()

def second_scene():
    global weapons_list
    global health
    if health == 0:
        health = starting_health

    level_increase()
    browse = input('Would you like to visit the Store, Mines, Blacksmith, or Settings? (store, mine, blacksmith, settings): ').lower()
    clear()
    
    if browse == 'store':
        clear()
        store()
        
    elif browse == 'mine':
        clear()
        mine()
    
    elif browse == 'blacksmith':
        clear()
        blacksmith()
    
    elif browse == 'settings':
        clear()
        settings()
    
    elif browse == 'pack':
        clear()
        weapons_purchased()
    
    elif browse == '.dev':
        clear()
        weapon_list_function()
        print('--LIST of WEAPONS--')
        for i in range(0,len(weapons_list)):
            print(f'{i+1}.{weapons_list[i][0]}')
        x = input('Press ENTER to continue: ')
        
    else:
        clear()
        second_scene()

def combat_level_one():

    global max_monster_health
    global monster
    global monster_lvl
    global exp_dropped
    global gold
    global monster_health
    global damage_per_hit

    monsters = ['Slime', 'Zombie', 'Mimic', 'Nymph', 'Dark Elf', 'Ent', 'Skeleton', 'Spider']
    monster_number = random.randint(0,len(monsters))
    monster = monsters[monster_number]
    if monster == 'Mimic':
        damage_per_hit = 7
        gold += 50
        monster_health = 30
        max_monster_health = monster_health
        monster_lvl = 1
    else:
        damage_per_hit = 7
        exp_dropped = 50
        monster_health = 30
        max_monster_health = monster_health
        monster_lvl = 1
# Random drop for loot, implement this so it is given upon monster defeat    
    drop_loot = random.randint(0,20)
    if drop_loot == 0:
        weapons_list()
        random_drop = random.randint(0,len(weapons_list)-1)
        weapons_owned.append(weapons_list[random_drop])

def fight_sequence_one():
    global monster_health
    global health
   
    combat_level_one()

    while health >= 1 and monster_health >= 1:
        player_attack()
        monster_attack() 

def player_attack():

    global text_timer

    global monster
    global monster_health
    global damage_output
    global player_exp
    global exp_dropped
    global health
    global gold
    global killed_monster_count

    damage_calculator() 
    
    monster_health -= damage_output
    display_monster_stats()
    print(f'You dealt {damage_output} damage to the {monster}!')
    
    
    if monster_health <= 0:
        monster_health = 0
        clear()
        player_exp += exp_dropped
        display_monster_stats()
        __continue__ = input(f'\nYou have slain {monster} +{exp_dropped}xp\n\nPress ENTER to continue: ')
        killed_monster_count += 1
        clear()
    else:
        time.sleep(text_timer)
        clear()

def monster_attack():

    global text_timer
    
    global gold
    global health
    global health_potion_count
    global damage_per_hit
    global monster
    global monster_health
    global defense

    if monster_health <= 0:
        clear()
    else:
        health -= (damage_per_hit - (defense / 5))
        display_monster_stats()
        print(f'The {monster} dealt {damage_per_hit} damage to you!')
        time.sleep(text_timer)
        clear()

        if health <= 0:
            display_monster_stats()
            if health_potion_count <= 0:
                print(f'You have died to {monster}! -10g')
                gold -= 10
                time.sleep(text_timer)
                clear()
                second_scene()
            else:
                print(f'Health Potions: {health_potion_count}')
                drink_potion = input('Your health has reached zero, would you like to drink a potion?: ')
                if drink_potion == 'yes':
                    health = starting_health
                    print(f'Your health is full now')
                    health_potion_count -= 1
                    print(f'Health Potions: {health_potion_count}')
                    time.sleep(text_timer)
                    clear()
                    mine()
                else:
                    print(f'You did not drink a potion and died to {monster}')
                    gold -= 10
                    time.sleep(text_timer)
                    clear()
                    second_scene()

def display_monster_stats():
    global monster_health
    global max_monster_health
    global monster
    global monster_lvl
    global gold
    global health
    global starting_health
    global exp_progress
    global player_exp
    global player_level
    global perk_count
    if player_exp >= exp_progress:
        exp_progress = (exp_progress + (exp_progress / 5))
        exp_progress = round(exp_progress)
        player_level += 1
        perk_count += 1
    print(f'----------------------------------------------------------------------------------\nPlayer Level: {player_level}  Gold: {gold}g        {monster} level: {monster_lvl} Health: {monster_health}/{max_monster_health}\nNext level: {player_exp}/{exp_progress}')
    print(f"Available Perk Points: {perk_count}           {username}'s Health: {health}/{starting_health}\n----------------------------------------------------------------------------------")


    global weapons_list
    global random_weapon_choosen
    global random_weapon

#copy and paste list#
#    ['Basic', 10, 15, 1],['Common', 15, 25, 1],['Uncommon', 20, 40, 1],['Rare', 25, 55, 1],['Ultra Rare', 30, 70, 1],['Legendary', 40, 90, 1],['Mythical', 50, 150, 1],    #
    def closing_tab():
        #    Rarity  | Damage | Value | Elemental |  
        #  ----------|--------|-------|-----------|
        # Basic      |   10   |  15   |    n/a    |    
        # Common     |   15   |  25   |    n/a    |         
        # Uncommon   |   20   |  40   |    n/a    |
        # Rare       |   25   |  55   |    n/a    |        
        # Ultra Rare |   30   |  70   |    n/a    |        
        # Legendary  |   40   |  90   |    n/a    |        
        # Mythical   |   50   |  150  |    n/a    |        
        # *Unique*   |   65   |   ?   |    n/a    |        
        #============|========|=======|===========|
        # Weapon types: main hand: Wand, Attunement, Sword, Katana, Kunai, Bow, Shield, Telekinesis, Golem
        # Weapon Types: off Hand:  grimoire, None, shield, katana, shuriken, arrow, shield, none, support golem(might change this one)  
        # Unique's:     
        pass
#weapon - damage - value - elemental check(0 = yes, 1 = no)       ------LIST OF ALL WEAPONS EXCEPT FOR UNIQUES------
    weapons_list = [['Basic Wand', 10, 15, 1],['Common Wand', 15, 25, 1],['Uncomon Wand', 20, 40, 1],['Rare Wand', 25, 55, 0],['Ultra Rare Wand', 30, 70, 0],['Legendary Wand', 40, 90, 0],['Mythical Wand', 50, 150, 0],['Basic Attunement', 10, 15, 1],['Common Attunement', 15, 25, 1],['Uncommon Attunement', 20, 40, 1],['Rare Attunement', 25, 55, 1],['Ultra Rare Attunement', 30, 70, 1],['Legendary Attunement', 40, 90, 1],['Mythical Attunement', 50, 150, 1],['Basic Sword', 10, 15, 1],['Common Sword', 0, 25, 1],['Uncommon Sword', 0, 40, 1],['Rare Sword', 0, 55, 1],['Ultra Rare Sword', 0, 70, 1],['Legendary Sword', 0, 90, 1],['Mythical Sword', 0, 150, 1],['Basic Katana', 10, 15, 1],['Common Katana', 15, 25, 1],['Uncommon Katana', 20, 40, 1],['Rare Katana', 25, 55, 1],['Ultra Rare Katana', 30, 70, 1],['Legendary Katana', 40, 90, 1],['Mythical Katana', 50, 150, 1],['Basic Kunai', 10, 15, 1],['Common Kunai', 15, 25, 1],['Uncommon Kunai', 20, 40, 1],['Rare Kunai', 25, 55, 1],['Ultra Rare Kunai', 30, 70, 1],['Legendary Kunai', 40, 90, 1],['Mythical Kunai', 50, 150, 1],['Basic Bow', 10, 15, 1],['Common Bow', 15, 25, 1],['Uncommon Bow', 20, 40, 1],['Rare Bow', 25, 55, 1],['Ultra Rare Bow', 30, 70, 1],['Legendary Bow', 40, 90, 1],['Mythical Bow', 50, 150, 1],['Basic Shield', 10, 15, 1],['Common Shield', 15, 25, 1],['Uncommon Shield', 20, 40, 1],['Rare Shield', 25, 55, 1],['Ultra Rare Shield', 30, 70, 1],['Legendary Shield', 40, 90, 1],['Mythical Shield', 50, 150, 1]]

    random_weapon = random.randint(0,len(weapons_list)-1)

    random_weapon_choosen = weapons_list[random_weapon][0] + ' | ' + 'Damage: ' + str(weapons_list[random_weapon][1]) + ' | ' + str(weapons_list[random_weapon][2]) + ''
    if gold >= weapons_list[random_weapon][2]:
        weapons_owned.append(weapons_list[random_weapon])
        gold = gold - weapons_list[random_weapon][2]
        clear()
        print(f'You have purchased {weapons_list[random_weapon][0]}')
        time.sleep(text_timer)
        clear()
    return random_weapon_choosen
mini_game_func()
clear()
print('Welcome to my game! To play just type your actions unless there is a number is listed. Then afterwards just press the ENTER key to submit your choice')
__continue__ = input('-------------------------\nPress ENTER to continue: ')
clear()

#tutorial()
#stats()
#trait_selection()
#print_stats()

while running == True:
    second_scene()



