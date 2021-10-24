# define player stats
score = 0
Time_strt = 0
inventory = []
inventorydmg = []
health = 30
difficulty = 1
speed = 1
import time

# import all functions
from Encryption_function import encoder
from Random_number_generator import rng

# define function for input confirmation
def confirm_input(property:str):
    answer = input('Enter Yes or No: ').lower()
    while answer not in 'yesno':
        answer = input('Invalid response, please enter Yes or No: ')
    while answer in 'no':
        name = input(f'Please enter your {property}: ')
        answer = input(f'Is your {property} {name}? Enter Yes or No: ')

# define function for new items
def new_weapon(item:str, dmg:int):
    inventory.append(item)
    inventorydmg.append(dmg)

# name confirmation
name = input('Welcome to Generic Dungeon Crawler, please enter your name: ')
print(f'Is your name {name}?')
confirm_input(property='name')

# add the player name to a text file, encoding the name and printing the key so that it is more secure
with open('database', 'a')as file:
    key = rng(1, 26)
    file.write(f"Player name is {encoder(key, name)}, with key {key} \n")

# difficulty confirmation
difficulty_ask = input('Easy, Medium or Hard difficulty? (This modifies the strength of your opponents): ').lower()
while difficulty_ask not in 'easymediumhard':
    print('Invalid response, choose your difficulty: ')
    difficulty_ask = input('Easy, Medium or Hard difficulty? (This modifies the strength of your opponents): ').lower()
else:
    if difficulty_ask in 'easy':
        difficulty = 0.75
    elif difficulty_ask in 'medium':
        difficulty = 1
    elif difficulty_ask in 'hard':
        difficulty = 1.25

# add option for "speed running" the game, removing the time delay for the text so the game will happen faster
speedrun = input('Do you want to speedrun this game? (Will turn off text delay) Yes or No: ').lower()
while speedrun not in 'yesno':
    print('Invalid response, do you want to speedrun this game?')
    speedrun = input('Yes or No: ').lower()
else:
    if speedrun in 'yes':
        speed = 0
    elif speedrun in 'no':
        speed = 2

# define function for fighting enemies
def fight(enemy:str, ehealth:int, damage:int, weapon:str, etype:str):
    global health
    global score
    print(f'\x1B[3mThe {enemy} approaches you, wielding a {weapon}.\x1B[0m')
    time.sleep(speed)
    pweapon = input('Pick your weapon: ').title()
    pdamage = 0 # define player damage (based on the weapon that is in the inventory)
    edamage = damage * difficulty # define enemy damage, including difficulty multiplier

    # check if the weapon of choice is in the player's inventory, then find the corresponding damage of that weapon
    while pweapon not in inventory:
        if pweapon.lower() in 'check inventory':
            print(inventory)
            pweapon = input('Pick your weapon: ')
        else:
            print('Invalid weapon')
            pweapon = input('Pick your weapon: ')
    else:
        for n in range(len(inventory)):
            if pweapon == inventory[n]:
                pdamage = inventorydmg[n]

    # While both the enemy and the player are alive, cycle through fight sequences until one's health is diminished
    while ehealth > 0 and health > 0:
        time.sleep(speed)
        if etype == 'melee':
            atk = rng(1, 4)
            if atk == 1:
                print(f'The {enemy} swings his {weapon} in a wide arc, aimed straight for your head.')
                response = input('- ').lower()
                if 'dodge' in response:
                    print(f'You try to jump to the side, but the {weapon} continues, colliding with your head. You lose {edamage} health')
                    health -= edamage
                elif 'duck' in response:
                    print(f'The {weapon} glides over your head, exposing the side of the {enemy}')
                    response2 = input('- ').lower()
                    if 'stab' in response2 or 'strike' in response2 or 'cut' in response2 or 'slash' in response2 or 'slice' in response2 or 'attack' in response2:
                        print(f'Your {pweapon} sinks into the {enemy}, dealing {pdamage} damage.')
                        ehealth -= pdamage
                    else:
                        print(f'Invalid action, the {enemy} smashes you with his {weapon}, dealing {edamage} damage.')
                        health -= edamage
                elif 'block' in response:
                    print(f'You block the {weapon} with your {pweapon}, negating some of the damage.e You lose {(edamage)//2} health.')
                    health -= edamage
                else:
                    print(f'Invalid action, the {weapon} connects with your head, dealing {edamage}.')
                    health -= edamage
            elif atk == 2:
                print(f'The {enemy} thrusts his {weapon} foward, aimed at your chest.')
                response = input('- ').lower()
                if 'dodge' in response:
                    print(f'You move out of the way, and the {enemy} stumbles forward, losing his balance.')
                    response2 = input('- ').lower()
                    if 'stab' in response2 or 'strike' in response2 or 'cut' in response2 or 'slash' in response2 or 'slice' in response2 or 'attack' in response2:
                        print(f'Your land a critical hit, dealing {pdamage * 2} damage.')
                        ehealth -= pdamage * 2
                    else:
                        print(f'Invalid action, the {enemy} regains his balance.')
                elif 'duck' in response:
                    print(f'You duck under the {weapon}, but the {enemy} follows up with a kick, dealing {edamage} damage')
                    health -= edamage
                elif 'block' in response:
                    print(f'The weight of the {enemy} pushes through your defenses, leaving you open to the swing of the {weapon}. You take {edamage} damage.')
                    health -= edamage
                else:
                    print(f'Invalid action, the {weapon} strikes you in the chest, dealing {edamage} damage.')
                    health -= edamage
            elif atk == 3:
                print(f'The {enemy} charges forward in a rage, wildly swinging his {weapon}.')
                response = input('- ').lower()
                if 'dodge' in response or 'duck' in response:
                    print(f"Your attempt to evade the {enemy}'s wild charge is futile, and the barrage of strikes is super effective, dealing {edamage * 2} damage.")
                    health -= edamage * 2
                elif 'block' in response:
                    print(f"The {enemy}'s wild charge barely breaks through your defenses, dealing {edamage - 3} damage.")
                    health -= edamage - 3
                else:
                    print(f"Invalid action, the {enemy}'s barrage of strikes is super effective, dealing {edamage * 2} damage")
                    health -= edamage * 2
            elif atk == 4:
                print(f'The {enemy} leaps high into the air')
                response = input('- ').lower()
                if 'dodge' in response:
                    print(f"You jump out of the way as the {enemy} lands, giving you an opening to attack")
                    response2 = input('- ').lower()
                    if 'stab' in response2 or 'strike' in response2 or 'cut' in response2 or 'slash' in response2 or 'slice' in response2 or 'attack' in response2:
                        print(f'Your attack is successful, dealing {pdamage} damage to the {enemy}.')
                        ehealth -= pdamage
                    else:
                        print(f'Invalid action, the {enemy} recovers, preparing for another attack.')
                elif 'duck' in response:
                    print(f'You try to duck, but the {enemy} lands right on top of you, dealing {edamage * 2} damage.')
                    health -= edamage * 2
                elif 'block' in response:
                    print(f"The {enemy}'s {weapon} crashes through your defenses, dealing {edamage} damage.")
                    health -= edamage
    else:
        if ehealth <= 0:
            print('\n')
            print(f'Victory! You have successfully defeated the {enemy}.')
            score += 1
        elif health <= 0:
            print('\n')
            print(f'You have been defeated by the {enemy}. You lose! ')
            Time_end = Time_strt - time.process_time()//1
            print(f'You finished with a score of {score}, and a time of {Time_end} seconds.')
            exit()

# tutorial/introduction
# print lore text
Time_strt = time.time() # Time.strt - time.process_time()//1 to record end time
print('\x1B[3mYou sit up, dizzy. The rough, grey walls of what seems to be a prison cell feel claustrophobic, reminding you of how you got here.\x1B[0m')
print('\x1B[3mYou look around the room, relieved at the sight of your friend Aup, the merchant you were traveling with when the goblins ambushed you.\x1B[0m')
time.sleep(6)
print(f'Aup: Hey {name}, look what I found!')
time.sleep(speed)
print('\x1B[3mAup reaches into the revolting prison toilet, and pulls out a battered sword.\x1B[0m')
time.sleep(speed)
print('Aup: Here, take this sword, maybe we can use it to get out of here?\n')
time.sleep(speed)
print('~ New item: Battered Sword ~')
print(f"\x1B[3mA rusted blade found in the prison toilet. Does {3} damage.\x1B[0m\n")
new_weapon('Battered Sword', 3)
time.sleep(speed)
print('The flimsy iron door of your cell rattles, and a goblin guard throws in your meal.\n')
time.sleep(speed)
print('~ New item: Bread ~')
print(f'\x1B[3mA stale loaf of bread. Grants {5} health when eaten.\x1B[0m\n')
new_weapon('Bread', 1)
time.sleep(speed)
Speak1 = input('Action - ').lower()
while Speak1 not in 'eat bread':
    print('Aup: what are you doing? Eat your food before the rats get to it')
    Speak1 = input('- ').lower()
else:
    inventory.remove('Bread')
    print('The dry, stale bread does little to replenish your health. You gain 5 health.')
    health += 5

time.sleep(speed)
print('Aup: Look, the guard just fell asleep, lets get out of here!')
Speak2 = input('Action - ').lower()
while Speak2 not in 'kick door break door':
    print('Aup: Hurry up and break the door!')
    Speak2 = input('- ').lower()
else:
    print('\x1B[3mThe flimsy door gives way, startling the guard\x1B[0m')
    time.sleep(speed)
    print('Aup: Oh no, he woke up, prepare to fight!')
    print('Aup: Remember, when he attacks you have three options: dodge, duck or block. Choose the right one and you might have a change to counter attack.')
time.sleep(speed)
fight('Guard', 15, 5, 'Club', 'melee')
time.sleep(speed)
Time_end = (time.time() - Time_strt)//1
print(f'This is the end of the game so far, you end up with a score of {score} and a time of {Time_end} seconds')

# append the score and time to the database
with open('database', 'a') as file:
    file.write(f'Time = {Time_end}, Score = {score}\n')


