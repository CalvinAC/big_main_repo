#CalvinAC
#7/25/24
#functions_lists.py
# 
#==============================================================================

def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f'Hello, {name.title()}!'
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# Start with some designs that need to be printed.

def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
     Move each design to completed_models after printing."""

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all teh models that were printed."""
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


def make_pizza(size, *toppings):
    """"Summarize the pizza we are about to make."""
    print(f"\nMaking a {size} - inch pizza with the following toppings:")
    for topping in toppings:
        print(f'- {topping}')

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')


def build_profile(first, last, **user_info):
    """Build a ditionary containing everything we know about a user."""
    user_info['first name'] = first
    user_info['last name']  = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location= 'princeton',
                             field= 'physics')
print(user_profile)

