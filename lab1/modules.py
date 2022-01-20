from common import input_int

from random import randint

def list_maker(div_num1:int, div_num2:int,min:int=1,max:int=1001)->list[int]:
    """This method returns a list of divisible numbers with a specified span."""
    numbers = []
    for num in range(min,max+1):
        if num%div_num1==0 and num%div_num2==0:
            numbers.append(num)
    return numbers

def choose_your_own_numbers()->None:
    """This method prompts the user for specifications to find
    dvisiable numbers in a specifed number span"""
    print("Input your number span that you wish to search in by inputing two values.")
    rangemin=input_int("Value 1:")
    rangemax=input_int("Value 2:")
    if(rangemax<rangemin):
        #detta kastar värderna i rangmax och rangemin
        rangemax , rangemin = rangemin , rangemax
    anumber=input_int("Divisible number 1:")
    bnumber=input_int("Divisible number 2:")
    print(list_maker(anumber,bnumber,rangemin,rangemax))  

def guess_a_number(upper_limit:int=100,lower_limit:int=1)-> None:
    """This method runs a Number guessing game,
    User is propmted to guess a number in aspecified span."""
    correct=randint(lower_limit,upper_limit)
    while True:
        guess=input_int(f"Make a guess between ({lower_limit}-{upper_limit}): ")
        if guess==correct:
            print(f"Congratulations! {guess} is correct!")
            break
        elif guess < correct:
            print(f"Wrong! {guess} is too Low!")
        else:
            print(f"Wrong! {guess} is too High!")