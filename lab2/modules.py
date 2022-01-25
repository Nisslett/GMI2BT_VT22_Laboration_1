import csv
import json
from lab2.person import Person
from common import encapsulate, input_int_in_range

from itsdangerous import encoding

from common import input_not_empty


def convert_file_to_list(filename: str):
    """This function converts the csv-file
    to a list in order to work with the data"""
    people_list = []
    with open(filename, encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        print(reader)
        key = []
        for items in reader:
            if key == []:
                key = items
            person_dict = {}
            for i in range(len(items)):
                person_dict[key[i]] = items[i]
            people_list.append(person_dict)
    return people_list


def add_person(person_list):
    user_name_input = input_not_empty('Användarnamn: ')
    firstname_input = input_not_empty('Förnamn: ')
    lastname_input = input_not_empty('Efternamn: ')
    email_input = input_not_empty('E-mail: ')
    person_list.append({'Användarnamn': user_name_input, 'Förnamn': firstname_input,
                       'Efternamn': lastname_input, 'E-mail': email_input})


def add_person_test(person_list):
    keys = person_list[0].keys()
    person = {}
    for key in keys:
        person[key] = input_not_empty(f"Skriv in {key.title()}: ")
    person_list.append(person)


def search_person_list(personlist: list):
    keys: list[str] = Person.keys()
    # menu för attribut ,nr1 är alla atributer
    print(encapsulate("Söknings meny"))
    print("Välj den atribut av Personerna du vill söka på.")
    print("1. Alla attribut")
    for i in range(len(keys)):
        print(f"{i+2}. {keys[i]}")
    choice = input_int_in_range(
        "Välj ett av alternativen ovan: ", 1, len(keys)+1)
    if(choice == 1):
        chosen_search_attribute = keys
    else:
        chosen_search_attribute = [keys[choice-2]]
    # type serch term
    search_text: str = input("Skriv in den text du vill söka på: ")
    result_list: list = []
    for person in personlist:
        for attribute in chosen_search_attribute:
            #try:
                if person[attribute].lower().find(search_text.lower())!=-1:
                    result_list.append(person)
                    break
            #except KeyError:
                # Raden nedan användes under utveckling för manuell debugging
                #print(f"key not found {attribute} i {person}")
                
    return result_list
