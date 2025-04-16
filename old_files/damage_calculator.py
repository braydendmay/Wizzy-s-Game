import time
import random
import os

clear = lambda: os.system('cls')

current_wepaon_damage = 10
elemental = .10
weapon_elemental_check = 0
critical_hit_chance = 1

def damage_calculator():
    global current_wepaon_damage
    global weapon_elemental_check
    global elemental
    global damage_output
    if weapon_elemental_check == 0:
        damage_output = current_wepaon_damage + (current_wepaon_damage * elemental)
        print(f'current damage {current_wepaon_damage}')
        crit_chance = random.randint(0, critical_hit_chance)
        if crit_chance == 1:
            damage_output += (damage_output * .30)
            print('Crit!')
    elif weapon_elemental_check == 1:
        damage_output = current_wepaon_damage
        crit_chance = random.randint(0, critical_hit_chance)
        if crit_chance == 1:
            damage_output += (damage_output * .30)
