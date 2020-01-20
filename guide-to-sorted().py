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

sorted_list = sorted(sale_prices)   # As opposed to .sort(), sorted() is used by placing the list INSIDE the ()   .sort() permanetaley changes the list
reversed_sorted_list = sorted(sale_prices, reverse=True)   # To reverse, add a second argument


print(sale_prices)
print(sorted_list)
print(reversed_sorted_list)