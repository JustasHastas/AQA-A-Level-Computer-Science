# Third example
def cylinderVolume(r, len_):
	pi = 3.142
	vol = pi*r*r*len_
	return vol
# main program
print("Enter the radius of the cylinder:")
radius = float(input())
print("Enter the length of the cylinder:")
length = float(input())
volume = cylinderVolume(radius, length)
print("The volume of the cylinder is ", volume)
