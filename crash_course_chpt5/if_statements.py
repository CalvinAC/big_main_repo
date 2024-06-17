#CalvinAC
#6/17/24
#if_statements.py
# 
#==============================================================================

requested_toppings = ["mushrooms", 'onioins', 'pineapple']
print('mushrooms' in requested_toppings)

print('pepperoni' in requested_toppings)


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
