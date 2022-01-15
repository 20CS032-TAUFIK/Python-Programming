#concatenate dictionaries and create a new one.

#dictionaries
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}

#update dic4 dictionary
for e in (dic1, dic2, dic3): dic4.update(e)
#print dic4 dictionary
print(dic4)

