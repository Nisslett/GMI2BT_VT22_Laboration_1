class Person:
    def __init__(self, username:str,fname:str,sname:str,email:str):
        self.username = username
        self.firstname = fname
        self.surname = sname
        self.email = email
        
    def __init__(self, person_dict:dict):
        self.username = person_dict["användarnamn"]
        self.firstname = person_dict["förnamn"]
        self.surname = person_dict["efternamn"]
        self.email = person_dict["email"]
    
    def to_dictionary(self):
        pass
    #exportera en person till en tildicatoary