# LAMBDA allows you to wrap up a smaller function and pass it to other functions. similar to a VARIABLE
# functions are first class citizens. very mobile

full_name = lambda first, last: f'{first} {last}'    #arguments first: then there values

# This is the same as above the above LAMBDA
def full_name(first, last):
  return f'{first} {last}'


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kelsey', 'Hawker'))