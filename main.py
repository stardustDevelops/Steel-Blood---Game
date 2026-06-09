#===== Welcome to Steel & Blood =====#

#===== Imports =====#

from pprint import pprint
import random

#===== Main Title =====#

Title = '''
-----------------------
|    Steel & Blood    |
-----------------------
'''

#===== Main Data Collection =====#

#Player
player_data = {

    'player_class':{

        'knight':{
            'base_health':100,
            'base_stamina':100,
            'base_mana':0,
            'base_attack':5,
            'base_defence':10,
            'base_attribute':'STR',
            'amount_of_attribute':5,
    },

        'berserker':{
            'base_health':100,
            'base_stamina':100,
            'base_mana':0,
            'base_attack':10,
            'base_defence':5,
            'base_attribute':'DEX',
            'amount_of_attribute':5,
    },

        'mage':{
            'base_health':100,
            'base_stamina':0,
            'base_mana':100,
            'base_attack':15,
            'base_defence':0,
            'base_attribute':'INT',
            'amount_of_attribute':5,
    },
},
}

#Enemy
enemy_data = {

    'enemy_class':{

        'bandit':{
            'base_health':80,
            'base_stamina':100,
            'base_mana':0,
            'base_attack':5,
            'base_defence':0,
            'base_attribute':'DEX',
            'amount_of_attribute':5,
        },

        'raider': {
            'base_health':90,
            'base_stamina':100,
            'base_mana':0,
            'base_attack':7,
            'base_defence':5,
            'base_attribute':'DEX',
            'amount_of_attribute':5
    },

        'guard':{
            'base_health':120,
            'base_stamina':100,
            'base_mana':0,
            'base_attack':5,
            'base_defence':10,
            'base_attribute':'STR',
            'amount_of_attribute':5,
        },
},
}


#Gear
gear_data = {

    #Player
    'player_armour':{

        'heavy':{
            'defence':10,
            'stamina_cost':10,
            'damage_boost':0,
            'required_attribute':'STR',
            'amount_of_attribute':5,
    },

        'light':{
            'defence':5,
            'stamina_cost':5,
            'damage_boost':5,
            'required_attribute':'DEX',
            'amount_of_attribute':5,
    },

        'robe':{
            'defence':0,
            'stamina_cost':0,
            'damage_boost':10,
            'required_attribute':'INT',
            'amount_of_attribute':5,
        },
    },

    #Enemy
    'enemy_armour':{

        'torn_leather': {
            'defence': 3,
            'stamina_cost': 0,
            'damage_boost': 5,
            'required_attribute': 'DEX',
            'amount_of_attribute': 5,
    },

        'quality_leather': {
            'defence': 5,
            'stamina_cost': 0,
            'damage_boost': 10,
            'required_attribute': 'DEX',
            'amount_of_attribute': 5,
    },

        'iron_armour': {
            'defence': 10,
            'stamina_cost': 5,
            'damage_boost': 0,
            'required_attribute': 'STR',
            'amount_of_attribute': 5,
    },
},
}

#Weapons
weapon_data = {

    #Player
    'player_weapons':{

        'sword':{
            'weapon_damage':5,
            'stamina_cost':5,
            'mana_cost':0,
            'required_attribute':'STR',
            'amount_of_attribute':5
        },

        'axe':{
            'weapon_damage':10,
            'stamina_cost':10,
            'mana_cost':0,
            'required_attribute':'DEX',
            'amount_of_attribute':5
        },

        'staff':{
            'weapon_damage':15,
            'stamina_cost':0,
            'mana_cost':10,
            'required_attribute':'INT',
            'amount_of_attribute':5
        },

    },

    #Enemy
    'enemy_weapons':{

        'rusty_sword': {
            'weapon_damage': 3,
            'stamina_cost': 0,
            'mana_cost': 0,
            'required_attribute': 'DEX',
            'amount_of_attribute': 5,
        },

        'iron_lance': {
            'weapon_damage': 7,
            'stamina_cost': 5,
            'mana_cost': 0,
            'required_attribute': 'DEX',
            'amount_of_attribute': 5,
    },

        'iron_sword': {
            'weapon_damage': 5,
            'stamina_cost': 0,
            'mana_cost': 0,
            'required_attribute': 'STR',
            'amount_of_attribute': 5,
    },
},
}

#Dice Amplifier
dice_amplifier_data = {
    1:1.00,
    2:1.05,
    3:1.10,
    4:1.15,
    5:1.20,
    6:1.25,
}

#===== Welcome =====#

print('\nWelcome to')
print(Title)
print('\n')

#===== Classes =====#

#Character Creation
class Character:
    def __init__(self,name,health,stamina,mana,attack,defence,attribute_requirements,attribute_amount,character_weapon,character_armour):
        self.name = name
        self.health = health
        self.stamina = stamina
        self.mana = mana
        self.attack = attack
        self.defence = defence
        self.attribute_requirements = attribute_requirements
        self.attribute_amount = attribute_amount
        self.character_weapon = character_weapon
        self.character_armour = character_armour

#Gear Creation
class Gear:
    def __init__(self,name,defence,stamina_cost,damage_boost,attribute_requirements,attribute_amount):
        self.name = name
        self.defence = defence
        self.stamina_cost = stamina_cost
        self.damage_boost = damage_boost
        self.attribute_requirements = attribute_requirements
        self.attribute_amount = attribute_amount

#Weapons Creation
class Weapon:
    def __init__(self,name,damage,stamina_cost,mana_cost,attribute_requirements,attribute_amount):
        self.name = name
        self.weapon_damage = damage
        self.stamina_cost = stamina_cost
        self.mana_cost = mana_cost
        self.attribute_requirements = attribute_requirements
        self.attribute_amount = attribute_amount

#===== Object Creators =====#

#Weapon Creator
def create_weapon(weapon_name,category = 'player_weapons'):
    data = weapon_data[category][weapon_name]

    return Weapon(
        weapon_name,
        data['weapon_damage'],
        data['stamina_cost'],
        data['mana_cost'],
        data['required_attribute'],
        data['amount_of_attribute']
    )

#Gear Creator
def create_armour(armour_name,category = 'player_armour'):
    data = gear_data[category][armour_name]

    return Gear(
        armour_name,
        data['defence'],
        data['stamina_cost'],
        data['damage_boost'],
        data['required_attribute'],
        data['amount_of_attribute']

)

#Character Creator
def create_character(character_name,weapon,armour,statistics,category):
    data = statistics[category][character_name]

    return Character(
        character_name,
        data['base_health'],
        data['base_stamina'],
        data['base_mana'],
        data['base_attack'],
        data['base_defence'],
        data['base_attribute'],
        data['amount_of_attribute'],
        weapon,
        armour,
    )

#===== Objects =====#

#===== Weapon Objects =====#

#Player
sword = create_weapon('sword')
axe = create_weapon('axe')
staff = create_weapon('staff')

#Enemy
rusty_sword = create_weapon('rusty_sword', 'enemy_weapons')
iron_lance = create_weapon('iron_lance','enemy_weapons')
iron_sword = create_weapon('iron_sword','enemy_weapons')

#-------------------------------------------------------------------------------------#

#===== Gear Objects =====#

#Player
heavy_armour = create_armour('heavy', 'player_armour')
light_armour = create_armour('light', 'player_armour')
robe = create_armour('robe', 'player_armour')

#Enemy
torn_leather = create_armour('torn_leather', 'enemy_armour')
quality_leather = create_armour('quality_leather','enemy_armour')
iron_armour = create_armour ('iron_armour','enemy_armour')

#-------------------------------------------------------------------------------------#

#===== Class Objects =====#

#Player
knight = create_character(
    'knight',
    sword,
    heavy_armour,
    player_data,
    'player_class'
)

berserker = create_character(
    'berserker',
    axe,
    light_armour,
    player_data,
    'player_class'
)

mage = create_character(
    'mage',
    staff,
    robe,
    player_data,
    'player_class'
)

#Enemy
bandit = create_character(
    'bandit',
    rusty_sword,
    torn_leather,
    enemy_data,
    'enemy_class'
)

raider = create_character(
    'raider',
    iron_lance,
    quality_leather,
    enemy_data,
    'enemy_class'

)

guard = create_character(
    'guard',
    iron_sword,
    iron_armour,
    enemy_data,
    'enemy_class'
)

#-------------------------------------------------------------------------------------#

#===== Validations =====#

#Gear & Weapon Validation
def can_equip(character,item):
    if character.attribute_requirements == item.attribute_requirements and character.attribute_amount >= item.attribute_amount:
        return True
    else:
        return False

#===== Gearing Up =====#

def equip_weapon(character,weapon):
    if can_equip(character,weapon):
        return True
    else:
        return False

def equip_armour(character,armour):
    if can_equip(character,armour):
        return True
    else:
        return False

#===== User Input =====#

#Character Creation
def choose_character():
    while True:
        print('Choose your character: ')
        print('1. Knight')
        print('2. Berserker')
        print('3. Mage')

        character_choice = input('Choose your character: ')
        print('\n')

        if character_choice == '1':
            print('You have chosen: "Knight"')
            return create_character('knight', sword, heavy_armour, player_data, 'player_class')
        elif character_choice == '2':
            print('You have chosen: "Berserker"')
            return create_character('berserker', axe, light_armour, player_data, 'player_class')
        elif character_choice == '3':
            print('You have chosen: "Mage"')
            return create_character('mage', staff, robe, player_data, 'player_class')
        else:
            print('Invalid choice. Try again.')


#Character Summary
def show_character_summary(character):
    print("\n===== Character Summary =====\n")
    print("Name:", character.name)
    print("Health:", character.health)
    print("Stamina:", character.stamina)
    print("Mana:", character.mana)
    print("Attack:", character.attack)
    print("Defence:", character.defence)
    print("Weapon:", character.character_weapon.name)
    print("Armour:", character.character_armour.name)
    print('\n')

#Enemy Choices
def choose_enemy():
    while True:
        print('Choose your enemy: ')
        print('1. Bandit')
        print('2. Raider')
        print('3. Guard')

        enemy_choice = input('Choose your enemy: ')
        print('\n')

        if enemy_choice == '1':
            print('You have chosen "Bandit" as your enemy.')
            return create_character('bandit', rusty_sword, torn_leather, enemy_data, 'enemy_class')
        elif enemy_choice == '2':
            print('You have chosen "Raider" as your enemy.')
            return create_character('raider', iron_lance, quality_leather, enemy_data, 'enemy_class')
        elif enemy_choice == '3':
            print('You have chosen "Guard" as your enemy.')
            return create_character('guard', iron_sword, iron_armour, enemy_data, 'enemy_class')
        else:
            print('Invalid choice. Try again.')

#Start the Fight
def start_the_fight(player, enemy):
    while True:
        print('Press "1" if you are ready to fight.')
        print('Press "2" if you want to change character.')
        print('Press "3" if you want to change enemy.')

        fight_choice = input('Choose: ')
        print('\n')

        if fight_choice == '1':
            print('The fight begins!')
            return player, enemy
        elif fight_choice == '2':
            player = choose_character()
            show_character_summary(player)
        elif fight_choice == '3':
            enemy = choose_enemy()
            show_character_summary(enemy)
        else:
            print('Invalid choice. Try again.')

#=== Combat Systems ===#

#===== Dice Combat Amplifier =====#

#Roll Dice
def roll_dice():
    return random.randint(1,6)

def apply_dice_amplifier(damage):
    dice_roll = roll_dice()
    amplifier = dice_amplifier_data[dice_roll]
    final_damage = int(damage * amplifier)

    return final_damage,dice_roll

#Player Roll Dice
def player_roll_dice():
    while True:
        print('Press "1" to throw dice for damage boost.')
        print('Press "2" if you don\'t want a chance for damage boost')

        choice = input('Choice: ')
        print('\n')

        if choice == '1':
            return roll_dice()
        elif choice == '2':
            print('You received 0 bonus damage.')
            return None
        else:
            print('Invalid choice. Try again.')

#Damage System
def create_damage (attacker, defender, dice_roll = None):
    attacker_damage = attacker.attack + attacker.character_weapon.weapon_damage + attacker.character_armour.damage_boost
    defender_defence = defender.defence + defender.character_armour.defence

    base_damage = attacker_damage - defender_defence

    if base_damage <1:
        base_damage = 1

    if dice_roll:
        amplifier = dice_amplifier_data[dice_roll]
        final_damage = int(base_damage * amplifier)
    else:
        final_damage  = base_damage

    return final_damage

#Apply Damage
def apply_damage(target, damage):
    target.health = target.health - damage

    if target.health <0:
        target.health =0

    return target.health

#Alive Validation
def is_alive(character):
    if character.health <=0:
        return False
    else:
        return True

#Combat Round
#Player
def player_attack(player,enemy):
    dice_roll = player_roll_dice()
    damage = create_damage(player,enemy, dice_roll)
    apply_damage(enemy, damage)

    if dice_roll:
        print(f'{player.name} rolled a {dice_roll}.')
    else:
        print(f'{player.name} attacked without a dice roll.')

    print(f'{player.name} has dealt {damage} damage to {enemy.name}.')
    print(f'{enemy.name} has {enemy.health} health left.')

    return damage, enemy.health

#Combat Round
#Enemy
def enemy_attack(enemy,player):
    dice_roll = roll_dice()

    damage = create_damage(enemy, player, dice_roll)
    apply_damage(player, damage)

    print(f'{enemy.name} rolled a {dice_roll}.')
    print(f'\n{enemy.name} has dealt {damage} damage to {player.name}.')
    print(f'\n{player.name} has {player.health} health left.')

    return damage, player.health

#Combat Loop
def combat_loop(player,enemy):
    while is_alive(player) and is_alive(enemy):
        player_attack(player,enemy)

        if is_alive(enemy):
            enemy_attack(enemy,player)

    if is_alive(player) and not is_alive(enemy):
        print('\nPlayer wins!\n')
        return player
    elif not is_alive(player) and is_alive(enemy):
        print('\nEnemy wins!\n')
        return enemy
    else:
        return None



#===== Play the Game =====#

def play_game():
    while True:
        player = choose_character()
        show_character_summary(player)

        enemy = choose_enemy()
        show_character_summary(enemy)

        player, enemy = start_the_fight(player, enemy)

        winner = combat_loop(player, enemy)

        if winner:
            print(f'{winner.name} has won the fight!')
        else:
            print('The battle ended in a draw!')

        play_again = input('Would you like to play again? Press "1" for "Yes" or "2" for "No": ')

        if play_again == '1':
            print('Starting a new fight...\n')
        elif play_again == '2':
            print('Thank you for playing "Steel & Blood"!')
            break
        else:
            print('Invalid choice.')
play_game()

#---------------------------------------
#===== The End =====#