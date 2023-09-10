
with open("item.txt","r") as file:
    for name in file:
        print(name.rstrip())
file.close()