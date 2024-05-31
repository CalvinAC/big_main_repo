#CalvinAC
#5/31/24
#lists_organization

#.sort function
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #sorting permanently changes order of list
print(cars)
print("")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
print()

#.sorted function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)
print()

#reverse method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()  #changes order of list permanently
print(cars)
print()

#list length
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

#end