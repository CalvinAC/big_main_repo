#CalvinAC
#6/20/24
#loop_dictionaries.py
# 
#==============================================================================

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

#can create mulitple variable names for loops
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

#loops through just the keys in the dictionary
for name in favorite_languages.keys():
    print(name.title())