num_list = range(1, 11)
cubed_nums = []

# for num in num_list:
#   cubed_nums.append(num ** 3)


# this will generate the same result as above
cubed_nums = [num ** 3 for num in num_list]   #first item in [] is the desired action. The name of"num" can be anything i want

print(cubed_nums)


###


new_range = range(1, 21)

even_numbers = []

for num in new_range:
  if num % 2 == 0:   #this is calling all even numbers. if 0 was 1 then it would return odd nums
    even_numbers.append(num)
    
    
# This is the same as above
even_numbers = [num for num in new_range if num % 2 == 0]
    
print(even_numbers)