number1 = 3 #number given to the variable
number2 = 4 # Integer
float_ = 2.35 #Float, has decimals
boolean = True # It can have two outcomes - true or false.
character = "%"
string = "qwer" #String can be anything within the quatanion marks
sudetis = number1 + number2
rounded1float = round(float_, 1) # The round function to round decimal number to specific number.
print(2**3) # Rise 2 to the power of 3
dalyba_su_liekana = 1654813 % 15427 # Print the raimainder of the divided number.
print(dalyba_su_liekana)
print(len(string)) #Prints the number of symblos in the string

# String conversion operation
string1 = "1357"
string1 = int(string1) #changes to integer
print(string1 + string1) #adds the characters of the string1 to second string1
print(str(float_) * 2) #adds exactly the same characters of the Float_
print(ord("*")) # Prints number that is allied to the character
print(chr(97)) #Shows what character is allied to that number

import datetime #Imported a module
birthday = datetime.datetime(1940,1,1,15,15,15) # Double datetime shows calendar date and hourly date.
data = datetime.date(1940, 2, 5)
laikkas = datetime.time(15, 16) #If only two numbers are written, it only shows hours and minutes
birthday1 = datetime.datetime(1999, 8, 3, 18, 30,4, 5)
print(birthday - birthday1) #Subtracts birthday1 from birthday
print(data)
print(laikkas)