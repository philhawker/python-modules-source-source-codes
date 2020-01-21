players = ['Altuve', 'Bregman', 'Correa', 'Gattis']


for player in players:   #player can be any word. playerS is refrencing the original variable
  print(player)
  
stars = {
  '2b' : 'Altuve',
  '3b' : 'Bregman',
  'ss' : 'Correa',
  'dh' : 'Gattis',
}

for position, star in stars.items():   # position, star will cascade the dictionary in the same format as indexes (0, 1)(position, star)
  print('Position', position)
  print('Player Name', star)