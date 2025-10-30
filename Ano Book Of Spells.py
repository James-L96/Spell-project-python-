import random
import pandas as pd



#Create heroes and classes
legend = {
    'elf': {'strength': 'ice', 'weakness': 'fire'},
    'human': {'strength': 'fire', 'weakness': 'ice'},
    'dwarf': {'strength': 'earth', 'weakness': 'ice'}
}

#classes
hero_lineage = {
    'fighter': {'specialty': 'fire', 'bounus':'health'},
    'ranger': {'specialty': 'ice', 'bonus': 'speed'},
    'mage': {'speciality':'earth', 'bonus': 'mana'}
}

# Define valid elements
valid_elements = {
    'fire': {'strength': 'ice', 'weakness': 'earth'},
    'ice': {'strength': 'earth', 'weakness': 'fire'},
    'earth': {'strength': 'fire', 'weakness': 'ice'},
}

# Initialize an empty dictionary to store spell names and their corresponding elements
class spell:
        def __init__(self,name,element):
            self.name = name
            self.element = element

class hero:
        def __init__(self,name,race,role):
            self.name
            self.race
            self.role
            self.name


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