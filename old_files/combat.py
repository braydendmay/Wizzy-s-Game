import random
import time
import os

clear = lambda: os.system('cls')

def combat_level_one():
    global monster
    #enemy - damage per hit - exp given upon defeat
    monsters = ['Slime', 'Zombie', 'Mimic']
    monster_number = random.randint(0,len(monsters)+1)
    monster = monsters[monster_number]


def fight_sequence_one():
    global monster
    global health
    damage_per_hit = 5
    exp_dropped = 50
    monster_health = 35
    combat_level_one()
    def player_attack():
        damage_calculator()
        monster_health = monster_health - damage_output
        print(f'You dealt {damage_output} damage to the {monster}!')
        time.sleep(1)
        clear()
    def monster_attack():
        health -= damage_per_hit
        print(f'The {monster} dealt {damage_per_hit} damage to you!')
    while health >= 1 and monster_health >= 1:
        player_attack()
        monster_attack()
fight_sequence_one()