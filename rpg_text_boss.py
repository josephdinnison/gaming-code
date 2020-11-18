
## import libraries ##
import random
import termcolor


## set variables ##
boss_health = 50
player_health = 50
player_laser = 8
player_bigblast = 14
boss_punch = 6
boss_shock = 14
turn_counter = 1
turn_switch = True
bossmove_list = [boss_punch, boss_shock]
miss = 1
hit = 0
weakmiss_list_player = [hit, hit, hit, hit, miss]
strongmiss_list_player = [hit, hit, miss]
weakmiss_list_boss = [hit, hit, hit, hit, miss]
strongmiss_list_boss = [hit, hit, miss]


## Fight introduction ##
termcolor.cprint('\nYou have encountered the X-RS12! There is no choice but to fight!', 'green')


## Gameplay loop begins: Turn display and move selection ##
while turn_switch == True:
    termcolor.cprint('\n----------Turn ' + str(turn_counter) + '----------', 'green')
    termcolor.cprint('\nPlayer health = ' + str(player_health), 'blue')
    termcolor.cprint('\nBoss health = ' + str(boss_health), 'red')
    user_input = input('\nWhich attack will you use?\nType laser or big blast: ')


## When player selects laser attack ##
    if user_input == 'laser':
        turn_counter += 1
        player_miss_chance = random.choice(weakmiss_list_player)
        if player_miss_chance == 0:
            boss_health = boss_health - player_laser
            termcolor.cprint('\n---You used---', 'blue')
            print('Laser! Boss took 8 damage.')
            if boss_health <= 0:
                termcolor.cprint('\n---You have defeated the boss!---', 'green')
                turn_switch = False
        elif player_miss_chance == 1:
            termcolor.cprint('\n---You used---', 'blue')
            print('\nLaser - but it missed! Boss took 0 damage.')
## Boss Turn ##
        if turn_switch == True:
            boss_attack = random.choice(bossmove_list)
            if boss_attack == 6:
                boss_miss_chance = random.choice(weakmiss_list_boss)
                if boss_miss_chance == 0:
                    player_health = player_health - 6
                    termcolor.cprint('\n---Boss uses---', 'red')
                print('Punch! Player took 6 damage.')
                if player_health <= 0:
                    termcolor.cprint('\n---You have been defeated.---', 'green')
                    turn_switch = False
                elif boss_miss_chance == 1:
                    termcolor.cprint('\n---Boss uses---', 'red')
                    print('Punch - but it missed! Player took 0 damage.')
            elif boss_attack == 14:
                boss_miss_chance = random.choice(strongmiss_list_boss)
                if boss_miss_chance == 1:
                    player_health = player_health - 14
                    termcolor.cprint('\n---Boss uses---', 'red')
                    print('Shock! Player took 14 damage.')
                    if player_health <= 0:
                        termcolor.cprint('\n---You have been defeated.---', 'green')
                        turn_switch = False
                elif boss_miss_chance == 0:
                    termcolor.cprint('\n---Boss uses---', 'red')
                    print('Shock - but it missed! Player took 0 damage.')


## When player selects big blast attack ##
    elif user_input == 'big blast':
        turn_counter += 1
        miss_chance = random.choice(strongmiss_list_player)
        if miss_chance == 0:
            boss_health = boss_health - player_bigblast
            termcolor.cprint('\n---You used---', 'blue')
            print('Big blast! Boss took 14 damage')
            if boss_health <= 0:
                termcolor.cprint('\n---You have defeated the boss!---', 'green')
                turn_switch = False
        elif miss_chance == 1:
            termcolor.cprint('\n---You used---', 'blue')
            print('Big blast - but it missed! Boss took 0 damage')

## Boss turn ##
        if turn_switch == True:
            boss_attack = random.choice(bossmove_list)
            if boss_attack == 6:
                boss_miss_chance = random.choice(weakmiss_list_boss)
                if boss_miss_chance == 0:
                    player_health = player_health - 6
                    termcolor.cprint('\n---Boss uses---', 'red')
                    print('Punch! Player took 6 damage.')
                    if player_health <= 0:
                        termcolor.cprint('\n---You have been defeated.---', 'green')
                        turn_switch = False
                elif boss_miss_chance == 1:
                    termcolor.cprint('\n---Boss uses---', 'red')
                    print('Punch - but it missed! Player took 0 damage.')
            elif boss_attack == 14:
                boss_miss_chance = random.choice(strongmiss_list_boss)
                if boss_miss_chance == 1:
                    player_health = player_health - 14
                    termcolor.cprint('\n---Boss uses---', 'red')
                    print('Shock! Player took 14 damage.')
                    if player_health <= 0:
                        termcolor.cprint('\n---You have been defeated.---', 'green')
                        turn_switch = False
                elif boss_miss_chance == 0:
                    termcolor.cprint('\n---Boss uses---', 'red')
                    print('Shock - but it missed! Player took 0 damage.')


## If the player enters an invalid attack ##
    else:
        print('\nYou must enter the name of the attack you wish to use.')


## When the player or boss reaches 0 health ##




#robot_image = print('            __          ')
#print('           |**|         ')
#print('	       |__|         ')
#print('            ||          ')
#print('       ------------     ')
#print('       |          |     ')
#print('       |          |     ')
#print('   ----|  X-RS12  |---- ')
#print('       |          |     ')
#print('       |          |     ')
#print('       |          |     ')
#print('       |          |     ')
#print('       ------------     ')
#print('         ||    ||       ')
#print('         ||    ||       ')
#print('        ----  ----      ')







