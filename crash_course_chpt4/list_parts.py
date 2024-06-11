#CalvinAC
#6/11/24
#list_parts.py
# 
#==============================================================================

players = ['charles', 'martina', 'michael', 'florence']
print(players[0:3])

#defaults to beginning of list
print(players[:4])

#slicing loop
print("Here are the first three players on my team:")
for player in players [:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

#proves that lists are different
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
