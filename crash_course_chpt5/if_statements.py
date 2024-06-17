#CalvinAC
#6/17/24
#if_statements.py
# 
#==============================================================================

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we are out of green peppers rn RIP")
        else:
            print(f"Adding {requested_topping}.")

    print("Finished making da pizza pie")
else:
    print('You sure you want just bread?')