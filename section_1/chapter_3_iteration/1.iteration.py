# Types of Iterative statement WHILE REPEAT and FOR

# All of these variables/data structures are iterable
string = "Mouse 1"
list_ = [555, 7289357] # It can be fully edited
tuple_ = (55, 555.58) # The advantages of this is that it functions faster, requires less memory. 
dictionary = {
	'mouse':{'definition':'Mouse is an animal very small and fast', 'weight': '10-100g'},   # Consists of two things - key and value, e.g. 'mouse' and 'cat'
	'car': {'definition':'A means of transporation', 'weight': '10-100t'}, 
	'marsas':{'definition':'A big body of universe', 'weight': '10-100ttttt'}}

#The FOR  loop
for raide in string:
	print('kazkokia raide:' + raide)

skaiciai = [1, 2, 5]
for skaicius in skaiciai:
	print(skaicius * 100)

duomenu_baze = [
	['bmw', 'raudona'],
	['mercedes', 'juoda']]

for marke, spalva  in duomenu_baze:
	print('Marke: ', marke)
	print('Spalva: ', spalva)

import justo_dictionary_programa

x = 1
while x < 10:
	print(x)
	x += 1 # tas pats kas x = x + 1
else:
	print('pabaiga')



for number in [10, 20, 50]:
	print(number)
	if number == 20:
		break

print('continue')
for number in [10, 20, 50]:
	print(number)
	if number == 10:
		continue


# Indefinite iteration
# Definite iteration

#The WHILE ... ENDWHILE loop
#The REPEAT ... UNTIL loop

#NESTED loops
