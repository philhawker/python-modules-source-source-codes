teams = {
  'astros': ['Altuve', 'Corea', 'Bregman'],
  'angels': ['Trout', 'Pujos'],
  'yankees': ['Judge', 'Stanton'],
  'red sox': ['Price', 'Betts']
}


del teams['angels']

removed_teams = teams.pop('red sox', 'Team not found')[0]

print(teams)
print(removed_teams)