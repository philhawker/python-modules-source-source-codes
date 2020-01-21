legacy_customers = ['Alice' 'Bob']
new_customers = ['Tiffany', 'Kristine']

raw_db = [legacy_customers, new_customers]   #not what we want

print(raw_db)   #not what we want

for legacy_customer in legacy_customers:
  new_customers.append(legacy_customer)

print(new_customers)