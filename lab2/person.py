# A class holding functions connected to a person-object

class Person:
    def __init__(self, username: str, fname: str, sname: str, email: str):
        self.username = username
        self.firstname = fname
        self.surname = sname
        self.email = email
        # telefon nummer
        # adress
        #


    def __init__(self, person_dict: dict) -> None:
        self.username = person_dict["användarnamn"]
        self.firstname = person_dict["förnamn"]
        self.surname = person_dict["efternamn"]
        self.email = person_dict["epost"]


    def to_dictionary(self) -> dict:
        return {"användarnamn": self.username,
                "förnamn": self.firstname,
                "efternamn": self.surname,
                "epost": self.email}


    def __str__(self) -> str:
        return self.username+", "+ self.firstname+", "+ self.surname + ", " + self.email

    @staticmethod
    def keys() -> tuple[str]:
        return ("användarnamn","förnamn","efternamn","epost")
