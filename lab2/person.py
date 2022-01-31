# A class holding functions connected to a person-object

class Person:
    def __init__(self, username: str, fname: str, sname: str, email: str):
        """Constructor, makes a Person object"""
        self.username = username
        self.firstname = fname
        self.surname = sname
        self.email = email

    def __init__(self, person_dict: dict) -> None:
        """Constructor, coverts a dictonry to a Person object"""
        self.username = person_dict["användarnamn"]
        self.firstname = person_dict["förnamn"]
        self.surname = person_dict["efternamn"]
        self.email = person_dict["epost"]

    def to_dictionary(self) -> dict:
        """Returns this object as a dictionry"""
        return {"användarnamn": self.username,
                "förnamn": self.firstname,
                "efternamn": self.surname,
                "epost": self.email}

    def __str__(self) -> str:
        """Returns  the Person class and contents as string"""
        return self.username + ", " + self.firstname + ", " + self.surname + ", " + self.email

    @staticmethod
    def keys() -> tuple[str]:
        """Returns the dictionary keys for the attributes in the Person class"""
        return ("användarnamn", "förnamn", "efternamn", "epost")
