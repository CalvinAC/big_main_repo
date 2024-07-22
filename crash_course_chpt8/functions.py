#CalvinAC
#7/19/24
#functions.py
# 
#==============================================================================

#name =input("what is your name?")

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
#greet_user(name)

def describe_pet(animal_type, pet_name):
    """Display informaton about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog', 'willie')

#Keyword arguements
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

def describe_pet( pet_name, animal_type='dog'):
    """Display informaton about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet(pet_name='harry', animal_type='hamster')

#A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

#A hamster named harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

#Will cause arguement error-
#describe_pet()