#CalvinAC
#6/11/24
#list_tuples.py
# 
#==============================================================================

#tuple looks like a list but is unmutable
#works for things that should not be changed
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)