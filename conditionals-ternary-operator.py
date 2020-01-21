role = 'admin'


auth = 'can access' if role == 'admin' else 'cannot access'

print(auth)


#this is the same as above, but the long way

"""
 if role == 'admin':
   auth = 'can access'
 else:
   auth = 'cannot access'

print(auth)

"""