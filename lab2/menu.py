from common import input_int_in_range,encapsulate
import lab2.modules

def menu() -> None:
    """Menu Laboration 2"""
    errortext="\nFelaktig inmatning, välj ett av ovanstående alternativ."
    while True:
        print(encapsulate(" Laboration 2 "))
        print("Välj ett av alternativen listade nedan.")
        print("1. Läs in CSV-fil")
        print("2. Visa JSON-data")
        print("3. Lägg till person")
        print("4. Ta bort person")
        print("5. Spara fil")
        print("6. Återgå till huvudmeny")
        menu_input=input_int_in_range("Välj ett meny alternativ:",1,3,errortext)
        if menu_input == 1:
            pass
        elif menu_input == 2:
            pass
        elif menu_input == 3:
            pass
        elif menu_input == 4:
            pass
        elif menu_input == 5:
            pass
        elif menu_input == 6:
            break
