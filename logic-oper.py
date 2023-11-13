temp = int(input("Enter :"))

if not(temp >= 0 and temp <= 30):
    print('the temperature is not good today')
    print('stay inside')
elif not(temp<0 or temp>30):
    print("the temperature is good today")
    print("Go outside")
