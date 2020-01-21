username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'


if username == 'jonsnow' and password == 'thenorth':   # left and right of AND must be true
  print('Access permitted')
else:
  print('You shall not pass')
  
  
####
  
second_username = 'jonsnow'
second_email = 'jon@snow.com'
second_password = 'thenorth'

if second_username == 'jonsnow' or second_password == 'thenorth':   # OR will only need to accept one of the conditionals to be true
  print('Access permitted')
else:
  print('You shall not pass')


###

third_username = 'jonsnow'
third_email = 'jon@snow.com'
third_password = 'thenorth'

if (third_username == 'jonsnow' or third_email == 'jon@snow.com') and third_password == 'thenorth':
  print('Access permitted')
else:
  print('You shall not pass')
  
  
  ###
  
  
logged_in = True
standard_user = False

if logged_in and not standard_user:
  print('You can access the admin dashboard')
else:
  print('you can only access the standard dashboard')
