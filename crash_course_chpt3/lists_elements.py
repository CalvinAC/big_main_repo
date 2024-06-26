
#begin

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print("")

motorcycles[0] = 'ducati'
print(motorcycles)
print("")

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.append('ducati')
print(motorcycles)
print("")

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
print("")

motorcycles.insert(0, 'ducati')
print(motorcycles)
print("")

del motorcycles[0]
print(motorcycles)
print(" ")
 
#pop function
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(" ")
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
print(" ")
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(" ")

#Removing item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
print("")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

#end