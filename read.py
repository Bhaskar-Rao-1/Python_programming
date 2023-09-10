
with open("students.txt","r") as file:
    lines=file.readlines()
for line in lines:
    print(f"hello,{line}",end="")
file.close()