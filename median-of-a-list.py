"""
Tools:
- math library
- sorted function
- list slicing
- computations

need to sort the list, then split the list in 2 in order to find the median

"""
import math

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)
