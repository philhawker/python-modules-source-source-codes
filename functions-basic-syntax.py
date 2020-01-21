def full_name(first, last):
  print(f'{first} {last}')
# Common convention to have 2 lines between the function and the call
  
full_name('Kelsey', 'Hawker')
full_name('Phil', 'Hawker')
full_name('Rick', 'Hawker')
full_name('Cristi', 'Benedict')
  
  
def auth(email, password):
  if email == 'philhawker1211@gmail.com' and password == 'secret':
    print('Authorized')
  else:
    print('Not authorized')


auth('philhawker1211@gmail.com', 'secret')



def hundred():
  for num in range(1, 101):
    print(num)


hundred()

def counter(max_value):
  for num in range(1, max_value):
    print(num)
    

counter(51)