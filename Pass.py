def main():
    x=get_number()
    print(f"{x}")
    
def get_number():
    while True:
        try:
            return int(input ("enter"))
            
        except ValueError:
            pass
    
main()
