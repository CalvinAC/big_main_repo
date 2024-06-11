#CalvinAC
#6/11/24
#examples_pt3.py
# 
#==============================================================================

#4-10 Slices
#==============================================================================

rand_list = ['spaghetti', 'mario', 'dunk', 'trogdor', 'chungus']

print("The first three items in the list are:")
print(rand_list[:3])

print("Three items in the middle of the list are:")
print(rand_list[1:4])

print("The last three items in the list are:")
print(rand_list[2:])

#4-11 My Pizzas, Your Pizzas
#==============================================================================
pizzas = ['cheese', 'pepperoni', 'supreme']
friend_pizzas = pizzas[:]

pizzas.append('anchovie')
friend_pizzas.pop()
friend_pizzas.append('hawiian (ew)')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("MY friends favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

#4-13 Buffet
#==============================================================================
foods = ('bread', 'paste', 'shrimp', 'soup', 'onion')
#to show that tuples cannot be changed
#foods.append('sus')

for food in foods:
    print(food)

foods = ('bread', 'goolash', 'steak', 'soup', 'onion')
for food in foods:
    print(food)
