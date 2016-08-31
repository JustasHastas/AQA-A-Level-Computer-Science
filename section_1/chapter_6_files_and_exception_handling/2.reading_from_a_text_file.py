o = open("newlist.txt", 'r') # 'rb' for reading binary data
knyga = o.read()
print(knyga)
o.close()
