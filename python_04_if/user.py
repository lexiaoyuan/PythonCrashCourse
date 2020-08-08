users = ['lexiaoyuan', 'admin', 'lexiaoyuanbeta',
         'adminbeta', 'benjamin', 'benjaminbeta']
users = []

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user.title() + ",thank you for logging in again.")
else:
    print("We need to find some users!")

current_users = ['lexiaoyuan', 'ADMIN', 'lexiaoyuanbeta',
                 'adminbeta', 'benjamin', 'benjaminbeta']
current_users = [w.lower() for w in current_users]
# print(current_users)
new_users = ['Admin', 'lexiaoyuan', 'test1', 'test2', 'test3']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + " is used, Please enter a different user name.")
    else:
        print(new_user + " is not used.")

ordinal_numbers = list(range(1, 10))
print(ordinal_numbers)

for number in ordinal_numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number)+"th")
