#CalvinAC
#5/31/24
#examples_pt2.py

#begin

#3-4 Guest List
guests = ['plato', 'lincoln', 'biden','obamna']
print(f"Please come to dinner {guests[0].title()}.")
print(f"Won't you have a meal {guests[1].title()}?")
print(f"Join me for supper {guests[2].title()}.")
print(f"Eat up chonk {guests[3].title()}.")
print("")

#3-5 Changing Guest List
print(f"{guests[1]} will be unable to attend")
loser = 'lincoln'
guests.remove(loser)

guests=['plato', 'wall-e', 'biden','obamna']
print(f"Please come to dinner {guests[0].title()}.")
print(f"Won't you have a meal {guests[1].title()}?")
print(f"Join me for supper {guests[2].title()}.")
print(f"Eat up chonk {guests[3].title()}.")
print("")

#3-6 More Guests
print("I found a bigger table for us boy-o's")
guests.insert(0, 'crimson chin')
guests.insert(2, 'eminem')
guests.append('lejon brames')
print(f"Please come to dinner {guests[0].title()}.")
print(f"Won't you have a meal {guests[1].title()}?")
print(f"Join me for supper {guests[2].title()}.")
print(f"Eat up chonk {guests[3].title()}.")
print(f"Food is the sustenance of life, indulge us {guests[4].title()}.")
print(f"You hungry {guests[5].title()}?")
print(f"Bamsketball but it's food {guests[6].title()}?")

#3-7 Shrinking Guest List:
print("The council has spoken, only two of you will be fortunate enough to dine with me.")
removed = guests.pop()
print(f"You cannot sit with us {removed}")
removed = guests.pop()
print(f"You cannot sit with us {removed}")
removed = guests.pop()
print(f"You cannot sit with us {removed}")
removed = guests.pop()
print(f"You cannot sit with us {removed}")
removed = guests.pop()
print(f"You cannot sit with us {removed}")
print(f"congratulations {guests[0]} and {guests[1]}, you made the final cut.")

del guests[0]
del guests[0]
print(guests)



#end