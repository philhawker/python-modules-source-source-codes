num_list = range(1, 11)
cubed_nums = []

# for num in num_list:
#   cubed_nums.append(num ** 3)

cubed_nums = [num ** 3 for num in num_list]   #first item in [] is the desired action. The name of"num" can be anything i want

print(cubed_nums)