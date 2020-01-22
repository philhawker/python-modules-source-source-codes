def greeting(*args):   # *args This allows you to have as many arguments as you want
  print(args)              # *args can be named anything, but this is unconventional)


greeting('Kelsey', 'R', 'Sadie')


def greeting(time_of_day, *args):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
greeting('Morning', 'Tiffany', 'Hudgens')
