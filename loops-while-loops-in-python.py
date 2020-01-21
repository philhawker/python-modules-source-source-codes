# While loops must be told to STOP. it will become an infinite loop and will break code

nums = list(range(1, 100))

while len(nums) > 0:  # "while the length of nums is greater than 0"
  print(nums.pop())   


def guessing_game():
  while True:       # While True is useful when you dont know how many times you want your code to loop
    print('what is your guess?')
    guess = input()

    if guess == '42':
      print('your guess is correct')
      return False     # False is to stop the loop
    else:
      print(f'no, {guess} is not the answer, please try again')
      
      
