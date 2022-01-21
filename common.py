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

def input_int_in_range(inputtext:str,min:int,max:int,errortext:str="Not an integer or not in range!")->int:
    choice=0
    while True:
        input_int(inputtext,errortext)
        if choice>max and choice<min:
            print(errortext)
        else:
            break
    return choice

def repeat_string(character:str,repeat:int=60):
    return character*repeat

def encapsulate(text:str,fill_char:str="-",linelength:int=60):
    fillspace:int=linelength-len(text)
    if fillspace<=0:
        return text
    section:int=int(fillspace/2)
    odd:int=fillspace%2
    return section*fill_char+text+section*fill_char+fill_char*odd