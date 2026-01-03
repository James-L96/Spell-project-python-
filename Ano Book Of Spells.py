import random


# Initialize an empty dictionary to store spell names and their corresponding elements
class spell:
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
            element_data = self.valid_elements[self.element]
            self.strength = self.valid_elements[self.element]['strength']
            self.weakness = self.valid_elements[self.element]['weakness'] 
        else:
            self.strength = None
            self.weakness = None
        
    def use_spell(self):
        return f"You cast {self.name} and it is weak against {self.weakness}"

my_attack = spell("Fireball","Fire")
print(my_attack.use_spell())

class hero:
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
        'elf': {'health': (60, 80), 'speed':(90, 100), 'mana':(80,90)},
        'human':{'health': (80,90), 'speed':(75,80), 'mana':(80,100)},
        'dwarf':{'health': (90,115), 'speed':(50,70), 'mana': (50,70)}
        }

    class_stats = \
        {
        'fighter': {'health':(+25), 'speed':(+5), 'mana':(-10)},
        'ranger': {'health':(+5), 'speed':(+12), 'mana':(+5)},
        'mage': {'health':(0), 'speed':(-5), 'mana':(+20)}
        
        }
    def __init__(self, name, race, role):
            self.name = name
            self.race = race.lower()
            self.role = role.lower()
            
            self.stats = self.generate_stats()

            self.health = self.stats["health"]
            self.mana = self.stats["mana"]
            self.speed = self.stats["speed"]

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

    #seperated where stats are shown
    def show_stats(self):
        return (
            f"Health: {self.health}\n"
            f"Mana: {self.mana}\n"
            f"Speed: {self.speed}"
        )

    def new_char(self):
            return f"{self.name}. you are the {self.race.title()} people who excel in {self.role} combat!"



my_hero = hero('Draven','Human','Mage')

print(my_hero.new_char())
print(my_hero.show_stats())


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