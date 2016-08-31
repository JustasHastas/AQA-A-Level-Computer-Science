if 15 < 2:
	print(2)
else:
	print('netiesa')

#AND, OR, NOT, XOR
kintamas = True & True # AND
print(kintamas)
kintamas = True ^ True # XOR
print(kintamas)
kintamas = True | True # OR
print(kintamas)
kintamas = ~ True # NOT
print(kintamas)

# You can change the signs to the words.

kintamas = True and True 
print(kintamas)
kintamas = True or True
print(kintamas)
KITAMAS = not True
print(kintamas)

string = "Sieros Rugstis"
string1 = "sieros" # Pay attention to the spelling and whether there is a capital letter.
kintamas2 = string1 in string #
print(kintamas2)

string = "Sieros Rugstis"
string1 = "Sieros" # Pay attention to the spelling and whether there is a capital letter.
kintamas2 = string1 in string # Checks whether there is string1 inside the string.
print(kintamas2)

#Conditional Statement
kintamasis = 21
if kintamasis > 4:
	print("Yes, the value is more than 4")
elif kintamasis < 39:
	print("The value is more than 39 ")
else:
	print("No, the value is not more than 4")