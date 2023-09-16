email=input("enter email. ").strip()

name,domain=email.split("@")

if name and domain.endswith(".com"):
    print("valid")
else:
    print("invalid")