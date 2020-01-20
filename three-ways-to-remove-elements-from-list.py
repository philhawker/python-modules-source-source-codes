users = ['Kristine', 'Tiffany', 'Jordan', 'Lean']


print(users)

users.remove('Jordan')

print(users)

popped_users = users.pop()   #the popped user on the end will be stored in popped_user variable

print(popped_users)
print(users)

del users[0]

print(users)