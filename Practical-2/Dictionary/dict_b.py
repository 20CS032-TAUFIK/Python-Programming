#merge two Python dictionaries.

#dictionary b1
b1 = {'a': 50, 'b':100 }

#dictionary b2
b2 = {'x': 150, 'y': 200}

#making new dictionary copy of b1
b = b1.copy()

#merge b2 dictionary in  b dictionary
b.update(b2)

#print b dictionary
print(b)
