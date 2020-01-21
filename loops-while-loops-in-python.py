# While loops must be told to STOP. it will become an infinite loop and will break code

nums = list(range(1, 100))

while len(nums) > 0:  # "while the length of nums is greater than 0"
  print(nums.pop())   
