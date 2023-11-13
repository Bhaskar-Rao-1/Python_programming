rows=int(input("Enter "))
columns=int(input("Enter"))

symbol=input("enter")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()