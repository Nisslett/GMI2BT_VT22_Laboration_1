import json
import csv
from lab2.person import Person

class BaseFile:
    def __init__(self,filename:str,encoding:str="utf-8",path="./lab2/") -> None:
        self.filename = filename
        self.encoding = encoding
        self.path = path
    
class JsonFile(BaseFile):
    def __init__(self, filename:str = "labb2_personer.json", encoding:str="utf-8") -> None:
        BaseFile.__init__(self,filename, encoding)

    def load_person_list(self) -> list[Person]:
        pass

    def save_person_list(self, lista:list[Person]) -> None:
        pass
    
class CSVFile(BaseFile):
    def __init__(self, filename:str = "labb2_personer.csv", encoding:str = "utf-8") -> None:
        BaseFile.__init__(self,filename,encoding)
        
    def load_person_list(self)->list[Person]:
        """This function converts the csv-file to a list in 
        order to allow the user to work with the data"""
        person_list = []
        with open(self.path+self.filename,"r",encoding=self.encoding) as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            keys=[]
            for items in reader:
                if keys == []:
                    keys = items
                    continue
                person_dict = {}
                for i in range(len(items)):
                    person_dict[keys[i]] = items[i]
                person_list.append(Person(person_dict))
        return person_list
    
    def save_person_list(self,lista:list[Person])->None:
        pass