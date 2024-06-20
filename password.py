import string

password = "Helloworld"

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special_case = any([1 if c in string.punctuation else 0 for c in password])
digits_case = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special_case, digits_case]

length = len(password)

score = 0

with open('10k most common.txt', 'r'):
  common = f.read().splitlines()

if password in common:
  print("password was found in a common list. score: 0/7")
  exit()

if length > 8:
  score += 1
if length > 12:
  score += 1
if length > 17:
  score += 1
  
  
  # Google: common passwords list filetype:txt