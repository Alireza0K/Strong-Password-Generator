import os

from random import shuffle

print("""
      Hello there, welcome to first Alireza0K python console app. \n
      this is strong password generator, this console app can make best password for you.\n
      in the below i describe how you can use this app but let me to
      say thank you for useing this app. \n
      
      \t1. if you wana to make a normal password, first enter the 'N' and second
           enter the limit you want. ^Attention! normal password created just with alphabets and numbers.^\n
      \t2. if you wana to make a Strong password, first enter the 'S' and second
           enter the limit you want. ^Attention! strong password created with alphabets, symbols and numbers.^\n
      """)

upperCaseAlphabet = "abcdefghijklmnopqrstuvwxyz" # list of Elements

lowerCaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

numbers = "1234567890"

symbols = "?><}{:!@#$%^&*()_+=-|\\/"

userChose = str(input("Enter wich type of password you want: ")) # user choose the wich kind of password want

passwordLimit = int(input("Enter the limit: ")) # password limit 'user given'

# shuffled creator
def ShuffleJoiner(thingList):
    
    thingList = list(thingList)
    
    shuffle(thingList)
    
    thing = "".join(thingList)
    
    return thing

# limiter make a priod of a string
def Limiter(limit, stringOfThings):
    
    result = stringOfThings[0:limit]
    
    return result

# normal password creator
def NormalPassword(limit, elements):
    
    rowPassword = ""
    
    for element in elements:
        
        rowPassword += element
        
        if "1" in element:
            
           rowPassword += element 
           
    rowPassword = ShuffleJoiner(rowPassword)
    
    lastResult = Limiter(limit, rowPassword)
    
    return lastResult

# normal password creator
def StrongPassword(limit, elements):
    
    rowPassword = ""
    
    for element in elements:
        
        rowPassword += element
        
        if "1" in element:
            
           rowPassword += element 
           
    rowPassword = ShuffleJoiner(rowPassword)
    
    lastResult = Limiter(limit, rowPassword)
    
    return lastResult

# conditions for recognise to create which type password
if userChose == "N":
    
    print("you're password is:",NormalPassword(passwordLimit, [upperCaseAlphabet,numbers]))

elif userChose == "S":
    
    print("you're password is:",NormalPassword(passwordLimit, [upperCaseAlphabet,numbers,symbols,lowerCaseAlphabet]))