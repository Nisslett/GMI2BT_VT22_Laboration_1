import csv
import json

from itsdangerous import encoding

def convert_file_to_dictionary(filename = './lab2/labb2_personer_vt22.csv'):
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

