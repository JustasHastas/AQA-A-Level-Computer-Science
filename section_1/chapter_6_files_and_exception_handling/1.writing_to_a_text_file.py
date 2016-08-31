tekstas = b'''pirma eilute, antra eilute
asdfasdf Z
agsdgad Z
asdgasd'''
o = open("newlist.txt", 'wb') # 'wb' to write binary data.
o.write(tekstas)
o.close()
s