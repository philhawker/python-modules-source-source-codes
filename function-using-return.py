def full_name(first, last):
  return f'{first} {last}'    # Print() only returns something to the console. it doesnt "execute"


kelsey = full_name('Kelsey', 'Hawker')   # This is instantiation of the class above
phil = full_name('Phil', 'Hawker')


def greeting(name):
  print(f'Hi {name}!')


greeting(kelsey)
greeting(phil)
