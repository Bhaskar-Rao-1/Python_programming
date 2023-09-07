def main():
    while True:
        try:
            height=int(input("enter "))
            pyramid(height)
        except ValueError:
            print("x is not integer")
        else:
            break
def pyramid(n):
    for i in range(n):
        print ("#" * (i+1))
if __name__=="__main__":
    main()