usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

# Continue / Break

for username in usernames:
  if username == 'cersei':
    print(f'Sorry, {username}, you are not allowed')
    continue
  else:
    print(f'{username} is allowed')