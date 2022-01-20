def list_maker(div_num1:int, div_num2:int,min:int=1,max:int=1001)->list[int]:
    """This method returns a list"""
    numbers = []
    for num in range(min,max+1):
        #if (num/div_num1).is_integer() and (num/div_num2).is_integer():
        if num%div_num1==0 and num%div_num2==0:
            numbers.append(num)
    return numbers

def choose_your_own_numbers()->None:
    print("Input your number span that you wish to search in by inputing two values.")
    rangemin=input_int("Value 1:")
    rangemax=input_int("Value 2:")
    if(rangemax<rangemin):
        #tmp=rangemax
        #rangemax=rangemin
        #rangemin=tmp
        #Detta är gör det samma som ovan, källor:
        # https://www.geeksforgeeks.org/python-program-to-swap-two-variables/
        # https://www.programiz.com/python-programming/examples/swap-variables
        rangemax , rangemin = rangemin , rangemax
    anumber=input_int("Divisible number 1:")
    bnumber=input_int("Divisible number 2:")
    print(list_maker(anumber,bnumber,rangemin,rangemax))  

def input_int(inputtext:str,errortext:str="Not an integer, try again!")-> int:
    input_tmp=None
    while True:
        try:
            input_tmp=int(input(inputtext))
            break
        except ValueError:
            print(errortext)
    return input_tmp

def guess_a_number(upper_limit:int=100,lower_limit:int=1)-> None:
    from random import randint
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