import re

email=input("enter email")
if re.search(".+@.+", email):
    print("valid")
else:
    print("invalid")