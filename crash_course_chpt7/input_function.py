#CalvinAC
#7/5/24
#input_function.py
# 
#==============================================================================

message = input("Tell me something and I will repeat it back to you: ")
print(message)

name= input("Please enter your name:")
print(f"\nHello, {name}")

prompt = ("If you tell us who youe are we can personalize the messages you see.")
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello, {name}")

age = input('How old are you?')
age = int(age)
print(age >= 18)