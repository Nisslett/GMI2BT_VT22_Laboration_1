# This file contains methods and functions which can be used accross all files.

def input_int(inputtext:str, errortext:str = "Error! Är inte ett heltal, Försök igen!") -> int:
    """Returns a integer, This method propmts the user to input a integer,
    this will loop until a valid integer has been enterd"""
    input_tmp = None
    while True:
        try:
            input_tmp = int(input(inputtext))
            break
        except ValueError:
            print(errortext)
    return input_tmp

def input_int_in_range(inputtext:str, min:int, max:int, errortext:str = "Error! Är inte eller heltal eller är inte i spannet!") -> int:
    """This function propts the ser for input and repeats
    untill a integer that is in the specified range is provided."""
    choice:int = 0
    while True:
        choice = input_int(inputtext,errortext)
        if choice > max or choice < min:
            print(errortext)
        else:
            break
    return choice

def repeat_string(character:str, repeat:int = 60):
    """This function will repeat the provided string, by default 60 times"""
    return character * repeat

def encapsulate(text:str, fill_char:str = "-", linelength:int = 60):
    """This function will enclose the provided string with \"-\", in a span of 60 """
    fillspace:int = linelength - len(text)
    if fillspace <= 0:
        return text
    fill_section:str = int(fillspace/2) * fill_char # ---------------------
    if fillspace%2 != 0:
        return fill_section + text + fill_section + fill_char
    else:
        return fill_section + text + fill_section
    
def input_not_empty(text):
    """This function ask the user for input and loop until said input is not an empty string"""
    while True:
        input_str = input(text)
        if len(input_str.strip()) > 0:
            return input_str