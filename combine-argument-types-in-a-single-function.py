def greeting(**kwargs):  # THIS RETURNS A DICTIONARY
  print(kwargs)



greeting(first='Kristine', last='Hudgens')


def greeting(**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print('Hi Guest!')


greeting()
greeting(first='Kristine', last='Hudgens')
