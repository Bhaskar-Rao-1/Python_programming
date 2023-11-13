#tuple means like list but it is unchangable and in ordered

student = ("ram",21,"male")

print(student.count('bro'))

print(student.index('male'))

for i in student:
    print(i)

if "bro" in student:
    print("it is in tuple")