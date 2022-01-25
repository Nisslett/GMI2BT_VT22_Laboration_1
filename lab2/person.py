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

    def nice_string(self) -> str:
        """returns a nice string of person to print"""
        ret_str = "Person: användarnamn: " + self.username,
        ret_str += ", förnamn: " + self.firstname
        ret_str += ", efternamn: " + self.surname,
        ret_str += ", epost: " + self.email
        return ret_str

    def keys() -> list[str]:
        return ["användarnamn",
                "förnamn",
                "efternamn",
                "epost"]
