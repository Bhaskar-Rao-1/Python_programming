while True:
    try:
        x=int(input("enter value "))
    except ValueError:
        print ("entered value is not integer")
    else:
        break 
