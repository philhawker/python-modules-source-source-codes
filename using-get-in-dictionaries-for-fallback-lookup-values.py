teams = {
  'astros': ['altuve', 'corea', 'bregman'],
  'angels': ['trout', 'pujos'],
  'yankees': ['judge', 'stanton'],
  'red sox': ['price', 'betts']
}

featured_team = teams.get('mets', 'no featured team')  # this prevents the program from crashing by returning a value if something doesnt exist

print(featured_team)
