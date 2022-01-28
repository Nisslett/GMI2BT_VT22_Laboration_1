import json
import csv
from lab2.person import Person

class BaseFile:
    def __init__(self,filename:str,encoding:str="utf-8",path="./lab2/") -> None:
        self.filename = filename
        self.encoding = encoding
        self.path = path

    def save_text(self,text:str) -> None:
        with open(self.path+self.filename,"w",encoding=self.encoding) as text_file:
            text_file.write(text)

    def load_text(self)->str:
        with open(self.path+self.filename,"r",encoding=self.encoding) as text_file:
            return text_file.read()
    
class JsonFile(BaseFile):
    def __init__(self, filename:str = "labb2_personer.json", encoding:str="utf-8") -> None:
        BaseFile.__init__(self,filename, encoding)

    def load_person_list(self) -> list[Person]:
        #temp_list:list[Person]=[]
        #json_covertion:list[dict]=json.loads(self.load_text())
        #for item in json_convertion:
        #    temp_list.append(Person(item))
        #return temp_list
        return [Person(item) for item in json.loads(self.load_text())]

    def save_person_list(self, lista:list[Person]) -> None:
        self.save_text(self.json_string(lista))

    @staticmethod
    def json_string(lista:list[Person])->str:
        #temp_list:list[dict]=[]
        #for person in lista:
        #    temp_list.append(person.to_dictionary())
        #return json.dumps(temp_list,indent=4)
        return json.dumps([person.to_dictionary() for person in lista],indent=4)


    
class CSVFile(BaseFile):
    def __init__(self, filename:str = "labb2_personer.csv", encoding:str = "utf-8") -> None:
        BaseFile.__init__(self,filename,encoding)
        
    def load_person_list(self)->list[Person]:
        """This function converts the csv-file to a list in 
        order to allow the user to work with the data"""
        #temp_list:list[Person] = []
        #with open(self.path+self.filename,"r",encoding=self.encoding) as csvfile:
        #    reader = csv.DictReader(csvfile,delimiter=";")
        #    for item in reader:
        #        temp_list.append(Person(item))
        #return temp_list
        with open(self.path+self.filename,"r",encoding=self.encoding) as csvfile:
            reader = csv.DictReader(csvfile,delimiter=";")
            return [Person(item) for item in reader]
    
    def save_person_list(self,lista:list[Person])->None:
        #generateing a list[dict] from list[Person] with list comprehension 
        #temp_list:list[dict] = [item.to_dictionary() for item in lista]
        #with open(self.path+self.filename,"w",encoding=self.encoding,newline='') as csvfile:
        #    writer = csv.DictWriter(csvfile,Person.keys(),delimiter=";")
        #    writer.writeheader()
        #    writer.writerows(temp_list)
        with open(self.path+self.filename,"w",encoding=self.encoding,newline='') as csvfile:
            writer = csv.DictWriter(csvfile,Person.keys(),delimiter=";")
            writer.writeheader()
            writer.writerows([item.to_dictionary() for item in lista])

#Explaination of list comprehension
#https://www.w3schools.com/python/python_lists_comprehension.asp
#https://www.programiz.com/python-programming/list-comprehension
#
#Examples
#num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
#print(num_list)
#Output:
#[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
#
#obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
#print(obj)
#Output:
#['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
#


