def main():
    x = get_int('Guess a number between 45-50 :')
    print(f"Congratulation {x}")
    
    
        
def get_int(param) -> str:
    while True:
        try:
            x = int(input(param))
            if x == 50:
                return 'Winner Winner chicken dinner'
        except ValueError:
            pass

    

main()
    