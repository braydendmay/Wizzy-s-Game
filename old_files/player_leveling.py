import time
import random
import os

clear = lambda: os.system('cls')

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

player_level = 1
player_exp = 0
exp_progress = 235
perk_count = 0
#killing enemy gives exp, mining, exploring...

def level_increase():
    global exp_progress
    global player_exp
    global player_level
    global perk_count
    if player_exp >= exp_progress:
        exp_progress = (exp_progress + (exp_progress / 5))
        exp_progress = round(exp_progress)
        player_level += 1
        perk_count += 1
    print(f'Next level: {player_exp}/{exp_progress} Player Level: {player_level}')
    print(f'Available Skill Points: {perk_count}')

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

    apply_perk = input(f'Select a stat to improve: \nHealth: {health}\nDefense: {defense}\nWeight: {weight}\nStrength: {strength}\nIntelligence: {intelligence}\nMagic: {magic}\nStealth: {stealth}\nInput: ').lower()

    if apply_perk == 'health':
        health += 1
    elif apply_perk == 'defense':
        defense += 1
    elif apply_perk == 'weight':
        weight += 1
    elif apply_perk == 'strength':
        strength += 1
    elif apply_perk == 'intelligence':
        intelligence += 1
    elif apply_perk == 'magic':
        magic += 1
    elif apply_perk == 'stealth':
        stealth += 1
    else:
        clear()
        use_perks()
    clear()
    print(f'New stats:\nHealth: {health}\nDefense: {defense}\nWeight: {weight}\nStrength: {strength}\nIntelligence: {intelligence}\nMagic: {magic}\nStealth: {stealth}\nInput: ')
