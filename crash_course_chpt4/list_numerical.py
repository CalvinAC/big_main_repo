#CalvinAC
#6/4/24
#list_numerical.py

#==============================================================================

#range() function
for value in range(1,5):
    print(value)

numbers =list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares =[]
for value in range(1,11):
    squares.append(value ** 2)

print(squares)

#statistics
digits = [1,2,3,4,5,6,7,8,9,10]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)


