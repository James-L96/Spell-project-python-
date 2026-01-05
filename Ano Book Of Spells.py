import random

class MonsterDB:
    orcs = {
        'Kid Orc': {
            'health': 9, 'speed': 7, 'atk': 7,
            'mana': 20, 'def': 5, 'eva': 7
        },
        'Orc Warrior': {
            'health': 15, 'speed': 5, 'atk': 12,
            'mana': 5, 'def': 8, 'eva': 4
        }
    }

    bandits = {
        'Bandit Thug': {
            'health': 10, 'speed': 8, 'atk': 6,
            'def': 4, 'eva': 6
        }
    }

    dryads = {
        'Forest Dryad': {
            'health': 12, 'speed': 9, 'atk': 5,
            'mana': 30, 'def': 3, 'eva': 9
        }
    }

def spawn_monster(species):
    pool = getattr(MonsterDB, species)   # orcs, bandits, etc.
    if pool is None:
            print("Unknown Species")
    name, stats = random.choice(list(pool.items()))
    return Monster(name, species, stats)

class Monster:
    def __init__(self, name, stats):
        self.name = name
        self.max_health = stats['health']
        self.health = stats['health']
        self.stats = stats

    def __repr__(self):
        return f"{self.name} (HP: {self.health}/{self.max_health})"

#Items Database
class ItemDB:
    weapons = {'swords': {'Wood Sword': 
            {'atk': 9, 'spd':7}},
    'mace': {'Rusted Morning Star':
            {'atk': 10, 'spd':7}},
    'hammer': {'Old Harold': 
            {'atk':15, 'spd':4}},
    'bows':{'Swan Song': 
            {'atk':10, 'spd':10  } },
    'wands': {'Tissle': 
            {'atk':9, 'spd': 9}},
    }
    
    armor = {
    'helmets': {'basic helm':{'def':5}},
    'chest': {'basic chest':{'def':7}},
    'arms': {'basic gloves':{'def':4, 'spd':4,'eva':3}},
    'feet': {'leath boots':{'def':3, 'spd':6, 'eva':5}},
    'shield':{'wooden shield':{'def':6}},
    'ring': {'fire ring':{'fire damage': 7}}
    }

#class to hold a item
class Item:
    def __init__(self, name, slot, stats):
        self.name = name
        self.slot = slot   # helmet, weapon, etc.
        self.stats = stats

    def __repr__(self):
        return f"{self.name} ({self.stats})"
class Inventory:
    invetory_slots = {}
    def __init__(self):
        self.slots ={
        'helmet' == None,
        'chest' == None,
        'arms' == None,
        'feet' == None,
        'shield' == None,
        'ring' == None
    }
    
    def equip(self, item):
        if item.slot in self.slots:
            self.slots[item.slot] = item
        else:
            print("Invalid slot")
    
    def show_equipment(self):
        for slot, item in self.slots.items():
            print(f"{slot}: {item}")


# Initialize an empty dictionary to store spell names and their corresponding elements
class Spell:
    valid_elements = \
    {
        'fire': {'strength': 'ice', 'weakness': 'earth'},
        'ice': {'strength': 'earth', 'weakness': 'fire'},
        'earth': {'strength': 'fire', 'weakness': 'ice'},
    }
    def __init__(self,name,element):
        self.name = name
        self.element = element.lower() 
        if self.element.lower() in self.valid_elements.keys():
            self.element_data = self.valid_elements[self.element]
            self.strength = self.valid_elements[self.element]['strength']
            self.weakness = self.valid_elements[self.element]['weakness'] 
        else:
            self.strength = None
            self.weakness = None
        
    def use_spell(self):
        return f"You cast {self.name} and it is weak against {self.weakness}"

my_attack = Spell("Fireball","Fire")
print(my_attack.use_spell())

class Hero:
    legend = \
    {
        'elf': {'strength': 'ice', 'weakness': 'fire'},
        'human': {'strength': 'fire', 'weakness': 'ice'},
        'dwarf': {'strength': 'earth', 'weakness': 'ice'}
    }
#classes
    hero_lineage = \
    {
            'fighter': {'speciality': 'fire', 'bonus':'health'},
            'ranger': {'speciality': 'ice', 'bonus': 'speed'},
            'mage': {'speciality':'earth', 'bonus': 'mana'}
    }

    #bonus stats
    base_stats = \
        {
        'elf': {'health': (60, 80), 'attack':(25,40),'speed':(50, 65), 'mana':(80,90),'defense':(20,40),'evasion':(0,0)},
        'human':{'health': (80,90), 'attack':(25,40),'speed':(45,60), 'mana':(80,100),'defense':(30,50),'evasion':(0,0)},
        'dwarf':{'health': (90,115),'attack':(25,40), 'speed':(30,50), 'mana': (50,70),'defense':(40,60),'evasion':(0,0)}
        }

    class_stats = \
        {
        'fighter': {'health':(.15),'attack':(.15), 'speed':(.05), 'mana':(-.05),'defense':(.10),'evasion':(.2)},
        'ranger': {'health':(.05),'attack':(.15), 'speed':(.01), 'mana':(.05),'defense':(.05),'evasion':(.3)},
        'mage': {'health':(0),'attack':(.15), 'speed':(-.05), 'mana':(.20),'defense':(0),'evasion':(.1)}
        
        }
    def __init__(self, name, race, role):
            self.name = name
            self.race = race.lower()
            self.role = role.lower()
            
            self.stats = self.generate_stats()

            self.health = self.stats["health"]
            self.attack = self.stats["attack"]
            self.mana = self.stats["mana"]
            self.speed = self.stats["speed"]
            base_evasion = self.stats["evasion"]   # like 0.005 = 0.5%
            speed_bonus = self.speed * 0.002

            self.evasion = min(round(base_evasion + speed_bonus, 2), 0.35)
            

    def generate_stats(self):  
        hero_stats = {}
        if self.race in self.base_stats:
            stats_range = self.base_stats[self.race]
            
            for stat,range_tuple in stats_range.items():
                hero_stats[stat] = random.randint(range_tuple[0], range_tuple[1])
        else:
            return(f'Race {self.race} not found!')
            
        role_bonus = self.class_stats.get(self.role, {})
        for stat, bonus in role_bonus.items():
            hero_stats[stat] += bonus
        return hero_stats #change stats to be returned as a dictionary not a string

    def cast_spell(self, spell,target): 
        self.spell = spell
        self.target = target
        pass

    def damage_reduction(self, enemy):
        self.damage_taken = min(1,self.stats['defense'] /100 )
        pass

    def take_damge(self,amount):
        self.health = max(0, self.health - amount)
        return self.health

    #seperated where stats are shown
    def __str__(self):
        return (
            f"Health: {self.health}\n"
            f"Attack: {self.attack}\n"
            f"Mana: {self.mana}\n"
            f"Speed: {self.speed}\n"
            f"Evasion: {self.evasion}"
        )

    def new_char(self):
            return f"{self.name}. you are the {self.race.title()} people who excel in {self.role} combat!"
    
    def __repr__(self):
            return f"Hero(name='{self.name}', race='{self.race}', role='{self.role}')"
    



my_hero = Hero('Draven','Human','Mage')

print(my_hero.new_char())
repr(my_hero)
print(my_hero)

class Enemy:
    def __init__(self, monster,):
        pass

# while True:
    # Prompt the user to input a spell name
    #userInput = input("Input the spell name (or type 'end ritual' to finish): ")
    #spell = userInput.lower()

    # Check if the ritual is complete
    #if spell == "end ritual":
        #break
    
    # Ask for the spell's element
    #element = input(f"Input the element for the spell '{spell}': ").lower()

    # Check if the element is valid, if not, assign 'buff'
    #if element in valid_elements:
        #spell_list[spell] = element
    #else:
        #spell_list[spell] = "buff"  # Assign 'buff' if the element isn't valid

# Print out the list of spells and their corresponding elements
#print("\nThe completed ritual:")
#for spell, element in spell_list.items():
    #print(f"Spell: {spell}, Element: {element}")