#Password strength checker
import re

#Password must contain 8 characters
password = input("Enter Your Password: ")
if len(password) < 8:
  print("Password must be at least 8 characters long.")
  
  #password contains a uppercase letter
elif not re.search("[A-Z]", password):
  print("Password must contain at least one Uppercase letter.")
   #password contains a lowercase letter
elif not re.search("[a-z]", password):
  print("Password must contain at least one lowercase letter.")
   #password contains a number
elif not re.search("[0-9]", password):
  print("Password must contain at least one number.")
elif not re.search("[!-*]", password):
  print("Password must contain at least one special character.")
else:
  print("Password is strong!")