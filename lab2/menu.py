#if __name__ == "__main__":
from common import input_int_in_range, encapsulate
from lab2.modules import add_person_test,search_person_list,delete_person,edit_person,print_list
import json
from lab2.files import CSVFile,JsonFile


def menu() -> None:
    """Menu Laboration 2"""
    klasslista = []
    errortext = "\nFelaktig inmatning, välj ett av ovanstående alternativ."
    while True:
        print(encapsulate(" Laboration 2 "))
        print("Välj ett av alternativen listade nedan.")
        print("1. Läs in fil, meny")
        print("2. Spara fil, meny")
        print("3. Visa JSON-data")
        print("4. Visa Lista")
        print("5. Lägg till person")
        print("6. Ta bort person")
        print("7. Sök person")
        print("8. Redigera person")
        print("9. Återgå till huvudmeny")
        menu_input = input_int_in_range(
            "Välj ett meny alternativ: ", 1, 8, errortext)
        if menu_input == 1:
            klasslista = menu_read_file()
        elif menu_input == 2:
            menu_save_file(klasslista)
        elif menu_input == 3:
            print(json.dumps(klasslista))
        elif menu_input == 4:
            print_list(klasslista)
        elif menu_input == 5:
            add_person_test(klasslista)
        elif menu_input == 6:
            delete_person(klasslista)
        elif menu_input == 7:
            print_list(search_person_list(klasslista))
        elif menu_input == 8:
            edit_person(klasslista)
        elif menu_input == 9:
            break


def menu_read_file() -> list:
    errortext = "\nFelaktig inmatning, välj ett av ovanstående alternativ."
    filename:str = "labb2_personer_vt22.csv"
    returnlista = []
    while True:
        print(encapsulate(" Filhantering - läs in filer "))
        print("Välj ett av alternativen listade nedan.")
        print("1. Läs in Orginal CSV filen.")
        print("2. Läs in sparad CSV fil.")
        print("3. Läs in sparad json fil.")
        print("4. Återgå till föregående meny.")
        menu_input = input_int_in_range(
            "Välj ett meny alternativ: ", 1, 4, errortext)
        if menu_input == 1:
            returnlista = CSVFile(filename,"utf-8-sig").load_person_list()
        elif menu_input == 2:
            returnlista = CSVFile().load_person_list()
        elif menu_input == 3:
            returnlista = JsonFile().load_person_list()
        elif menu_input == 4:
            break
    return returnlista


def menu_save_file(peoplelist: list) -> None:
    errortext = "\nFelaktig inmatning, välj ett av ovanstående alternativ."
    filename = "./lab2/labb2_personer_vt22.csv"
    returnlista = []
    while True:
        print(encapsulate(" Filhantering - spara filer "))
        print("Välj ett av alternativen listade nedan.")
        print("1. Spara listan som en CSV fil.")
        print("2. Spara listan som en JSON fil.")
        print("3. Återgå till föregående meny.")
        menu_input = input_int_in_range(
            "Välj ett meny alternativ: ", 1, 3, errortext)
        if menu_input == 1:
            CSVFile().save_person_list(peoplelist)
        elif menu_input == 2:
            JsonFile().save_person_list(peoplelist)
        elif menu_input == 3:
            break


# funktin  för att :
# 1 visa listan i bättre format
# 2 söka i listan
# 3 läsa in från json
# 4 lägg till ett alternativ för att redigera en användare
# 5 undermenyer för att bättre organisera alternativen