#uppdelning
#1.funktion nummer 1 plus en input fuktion som loopar så länge inmatning inte är en int
#2.funktion nummer 2 

#Definera  minst två funktioner i denna fil

#Funktion nummer 1
#Definera in funktioner som tar in två parameterar
#funktionen ska hitta vilka generera lista med de tal som parameter talen är delbara
#med i en lista mellan 1 och 1000, denna lista ska returneras

def list_maker(div_num1:int, div_num2:int)->list[int]:
    numbers = []
    for num in range(1, 1001):
        if (num/div_num1).is_integer() and (num/div_num2).is_integer():
            numbers.append(num)
    return numbers

def input_int(inputtext:str,errortext:str="Not a integer, try again!")-> int:
    input_tmp=None
    while True:
        try:
            input_tmp=int(input(inputtext))
            break
        except ValueError:
            print(errortext)
    return input_tmp

#Funktion nummer 2
#en funktion untan parametar som ska lopa tills användaren
# ska gissat ett slumpat tal mellan 1 och 100
#ta hjälp av 
#import random
#random.randint(...)
#eller
#from random import randint
#säg åt andvändaren om gissningen är för stor eller förliten

def guess_a_number(upper_limit=100,lower_limit=1)-> None:
    from random import randint
    correct=randint(lower_limit,upper_limit)
    while True:
        guess=input_int(f"Make a guess between ({upper_limit}-{lower_limit}): ")
        if guess==correct:
            print(f"Congratulations! {guess} is correct!")
            break
        elif guess < correct:
            print(f"Wrong! {guess} is too Low!")
        else:
            print(f"Wrong! {guess} is too High!")