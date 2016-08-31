import datetime #Imported a module
birthday = datetime.datetime(1940, 1, 1, 15, 15, 15) # Double datetime shows calendar date and hourly date.
data = datetime.date(1940, 2, 5)
laikkas = datetime.time(15, 16) #If only two numbers are written, it only shows hours and minutes
birthday1 = datetime.datetime(1999, 8, 3, 18, 30, 4, 5)
print(birthday - birthday1) #Subtracts birthday1 from birthday
print(data)
print(laikkas)
