teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'angels': {
      'OF': 'Trout',
      'DH': 'Pujos',
    }
  }
]

print(teams)
print(teams[0])   #grab just astros in the same way as usual by using index position

angels = teams[1].get('angels', 'Team not found')

print(angels)