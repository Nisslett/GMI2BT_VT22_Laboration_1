
from lab1.menu import menu as lab1_menu
from lab2.menu import menu as lab2_menu
from common import repeat_string, encapsulate, input_int_in_range


def menu() -> None:
    """Main Menu"""
    #en meny som användaren ska välja mellan lab 1 eller lab2
    #eller att avsluta programmet.
    #typ så här 
    # 1.Laboration 1
    # 2.Laboration 2
    # 3.Exit
    errortext="\nFelaktig inmatning, välj ett av ovanstående alternativ."
    while True:
        #print("\n--------------------------------------------\n") 
        print("\n"+repeat_string("-"))
        print("\nVälkommen till vår redovisning av labb 1 & 2\n")
        print("Nils Borberg (h19nilbr) och Edvin Owetz (h20edvow)\n")
        #print("-------Huvudmeny-------")
        print(encapsulate(" Huvudmeny "))
        print("1. Laboration 1")
        print("2. Laboration 2")
        print("3. Avsluta programmet\n")
        menu_input=input_int_in_range("Välj ett meny alternativ:",1,3,errortext)
        if menu_input == 1:
            lab1_menu()
            
        elif menu_input == 2:
            lab2_menu()
        
        elif menu_input == 3:
            break
