#add an item in a tuple.

#create a tuple
tuple_c = (1, 2, 3, 4, 5, 6) 
print(tuple_c)
#using merge of tuples with the + operator
tuple_c = tuple_c + (9,)
print(tuple_c)
#adding item in a specific index
tuple_c = tuple_c[:6] + (15, )
print(tuple_c)
