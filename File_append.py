
name=input("enter your data ")
file=open("names.txt","a")
file.write(f"{name}\n")
file.close()
