#CalvinAC
#6/17/24
#examples_pt2.py
# 
#==============================================================================

# 5-8 Hello Admin
#==============================================================================

user_names = ['admin', 'david', 'joe', 'sam', 'bill']

for username in user_names:
    if username == 'admin':
        print('Hello Mr. Bond')
    else:
        print(f"Welcome back {username}")


# 5-9 No Users
#==============================================================================
user_names = []

if user_names:
    for username in user_names:
        if 'admin 'in user_names == True:
            print('Hello Mr. Bond')
        else:
            print(f"Welcome back {username}")
else:
    print('We need to find some users!')

# 5-10 Checking Usernames
#==============================================================================
current_users =['JonTron', 'epicWinner47', 'Sussybaka', 'McCringleberry', 
                'JoeShmo13']
new_users= ['JonTron', 'Megatron', 'LinusTT', 'McCringleberry', 
                'hurB']

for newuser in new_users:
    if newuser in current_users:
        print(f'{newuser} is not available')
    else:
        print(f'{newuser} is available')

# 5-11 Ordinal Numbers
#==============================================================================
ordinal_num = [1,2,3,4,5,6,7,8,9]

for num in ordinal_num:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num ==3:
        print(f"{num}rd")
    else:
        print(f"{num}th")

