from common import input_int_in_range,encapsulate
from lab2.modules import add_person_test, convert_file_to_list
import json

def menu() -> None:
    """Menu Laboration 2"""
    filename="./lab2/labb2_personer_vt22.csv"
    klasslista=[]
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
        menu_input=input_int_in_range("Välj ett meny alternativ:",1,6,errortext)
        if menu_input == 1:
            klasslista=convert_file_to_list(filename)
        elif menu_input == 2:
            print(json.dumps(klasslista))
        elif menu_input == 3:
            add_person_test(klasslista)
        elif menu_input == 4:
            pass
        elif menu_input == 5:
            pass
        elif menu_input == 6:
            break

#funktin  för att :
# 1 visa listan i bättre format
# 2 söka i listan
# 3 läsa in från json
# 4 alternativt sorta listan
# 5 lägg till ett alternativ för att redigera en användare