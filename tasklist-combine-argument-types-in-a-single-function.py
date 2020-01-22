def greeting(time_of_day, *args, **kwargs):
  print(f"Hi {' '.join(args)}, I hope that you are having a great {time_of_day}")
  

  if kwargs:
    print('Your tasks for the day are: ')
    for key, val in kwargs.items():    #.items is used to get both key and value in a dictionary
      print(f'{key} -- {val}')


greeting('Morning', 
         'Kelsey', 'Hawker', 
         first = 'Empty dishwasher',
         second = 'Vacuum', 
         third = 'make dinner')