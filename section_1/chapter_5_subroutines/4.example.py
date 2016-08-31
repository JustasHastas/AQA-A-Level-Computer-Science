# Fourth example: 
def printNumbers(x):
	a = 1
	b = 2
	c = 3
	print("In the subroutine, a,b, and x have values ", a, b, c, x)
# main program
a = 4
b = 5
c = 6
x = 10
print("In the main program, a,b,c and x have values", a, b, c, x)
printNumbers(x)
print("In the main program, a,b,c and x now have values", a, b, c, x)
