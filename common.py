#Tänkte att denna fil kan innehålla metoder/funktioner som alla filer kan använda

def input_int(inputtext:str,errortext:str="Not an integer, try again!")-> int:
    """Returns a integer, This method propmts the user to input a integer,
    this will loop until a valid integer has been enterd"""
    input_tmp=None
    while True:
        try:
            input_tmp=int(input(inputtext))
            break
        except ValueError:
            print(errortext)
    return input_tmp