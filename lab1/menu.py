from lab1.modules import choose_your_own_divisiable_numbers,guess_a_number
from common import input_int_in_range

# This file contains the sub-menu for lab 1

def menu() -> None:
    """Menu for Laboration 1"""
    errortext = "\nFelaktig inmatning, välj ett av ovanstående alternativ."
    while True:
        print("\n---- Laboration 1 ----\n")
        print("Välj ett av alternativen listade nedan.")
        print("1. Dividerbara nummer")
        print("2. Gissa numret!")
        print("3. Återgå till huvudmeny")
        menu_input = input_int_in_range("Välj ett meny alternativ: ", 1, 3, errortext)
        if menu_input == 1:
            choose_your_own_divisiable_numbers()
            
        elif menu_input == 2:
            guess_a_number()
        
        elif menu_input == 3:
            break