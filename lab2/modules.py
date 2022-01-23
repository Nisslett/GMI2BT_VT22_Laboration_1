import csv
import json

from itsdangerous import encoding

from common import input_not_empty

def convert_file_to_list(filename:str):
    """This function converts the csv-file
    to a list in order to work with the data"""
    people_list=[]
    with open(filename, encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        print(reader)
        key=[]
        for items in reader:
            if key==[]:
                key=items
            person_dict={}
            for i in range(len(items)):
                person_dict[key[i]]=items[i]
            people_list.append(person_dict)
    return people_list

def add_person(person_list):
    user_name_input = input_not_empty('Användarnamn: ')
    firstname_input = input_not_empty('Förnamn: ')
    lastname_input = input_not_empty('Efternamn: ')
    email_input = input_not_empty('E-mail: ')
    person_list.append({'Användarnamn':user_name_input, 'Förnamn':firstname_input,'Efternamn':lastname_input,'E-mail':email_input})
    
def add_person_test(person_list):
    keys = person_list[0].keys()
    person = {}
    for key in keys:
        person[key] = input_not_empty(f"Skriv in {key.title()}: ")
    person_list.append(person) 