usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

# Continue

for username in usernames:
  if username == 'cersei':
    print(f'Sorry, {username}, you are not allowed')
    continue
  else:
    print(f'{username} is allowed')
    

# Break

actors = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

for actor in actors:
  if actor == 'cersei':
    print(f'{actor} was found at index {actors.index(actor)}')
    break
  
print(actor)
