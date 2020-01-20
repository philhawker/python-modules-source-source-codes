players = {
  'ss' : 'Correa',
  '2b' : 'Altuve',
  '3b' : 'Bregman',
  'DH' : 'Gattis',
  'OF' : 'Springer',
}

player_names = list(players.copy().values())   #this allows you to edit a dictionary "safely" without someone else changing their values

print(players.items())   #.items() returns the dictionary as a TUPLE
print(players.values())   #.values() returns viewobjects of the key's values and doesnt allow you access to the values
print(player_names)


teams = {
  'astros': ['Altuve', 'Corea', 'Bregman'],
  'angels': ['Trout', 'Pujos'],
  'yankees': ['Judge', 'Stanton'],
  'red sox': ['Price', 'Betts']
}

team_groupings = teams.items()

print(list(team_groupings)[1][1][1])   #because teams.items() above returned a tuple, list() now allows you to grab elements


