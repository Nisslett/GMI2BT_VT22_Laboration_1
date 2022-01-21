import modules
from common import input_int_in_range

def menu() -> None:
    """Menu for Laboration 1"""
    #en meny som användaren ska välja mellan 
    #de två funktinoerna i labb 1
    #gissnings leken och dividerabara nummer funktionen
    #eller att eller att gå tillbaka.
    #typ så här 
    # 1.Divisable numbers
    # 2.Number Guessing Game
    # 3.Back / Return , or similar
    errortext="\nFelaktig inmatning, välj ett av ovanstående alternativ."
    while True:
        print("\n---- Laboration 1 ----\n")
        print("Välj ett av alternativen listade nedan.")
        print("1. Dividerbara nummer")
        print("2. Gissa numret!")
        print("3. Återgå till huvudmeny")
        menu_input=input_int_in_range("Välj ett meny alternativ:",1,3,errortext)
        if menu_input == 1:
            lab1.modules.choose_your_own_numbers()
            
        elif menu_input == 2:
            lab1.modules.guess_a_number()
        
        elif menu_input == 3:
            break

menu()