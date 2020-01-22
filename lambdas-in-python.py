# LAMBDA allows you to wrap up a smaller function and pass it to other functions. similar to a VARIABLE
# functions are first class citizens. very mobile

full_name = lambda first, last: f'{first} {last}'


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kelsey', 'Hawker'))