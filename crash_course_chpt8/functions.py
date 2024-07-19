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