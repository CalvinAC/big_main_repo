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

friends = ['phil', 'sarah']
#loops through just the keys in the dictionary
#This also works: for name in favorite_languages:
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


