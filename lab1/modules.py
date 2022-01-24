from common import input_int

from random import randint

def list_maker(div_num1:int, div_num2:int,min:int=1,max:int=1001)->dict:
    """This method returns a dict of divisible numbers with a specified span."""
    numbers:list[int] = []
    for num in range(min,max+1):
        if num%div_num1==0 and num%div_num2==0:
            numbers.append(num)
    return {"numlist":numbers,"average":sum(numbers)/len(numbers)}

def choose_your_own_divisiable_numbers()->None:
    """This method prompts the user for specifications to find
    dvisiable numbers in a specifed number span"""
    print("Välj det spann av värden du vill söka inom.")
    rangemin=input_int("Värde 1: ")
    rangemax=input_int("Värde 2: ")
    if(rangemax<rangemin):
        # This code just rearranges min and max so that min is allways the first number used
        rangemax , rangemin = rangemin , rangemax
    anumber=input_int("Delbart värde 1: ")
    bnumber=input_int("Delbart värde 2: ")
    num_dict=list_maker(anumber,bnumber,rangemin,rangemax)
    print(num_dict["numlist"])
    print("Medelvärde: "+str(num_dict["average"]))

def guess_a_number(upper_limit:int=100,lower_limit:int=1)-> None:
    """This method runs a Number guessing game,
    User is propmted to guess a number in aspecified span."""
    correct=randint(lower_limit,upper_limit)
    while True:
        guess=input_int(f"Gissa på ett värde mellan ({lower_limit}-{upper_limit}): ")
        if guess==correct:
            print(f"Grattis, {guess} är rätt!")
            break
        elif guess < correct:
            print(f"Fel, {guess} är för lågt!")
        else:
            print(f"Fel, {guess} är för högt!")