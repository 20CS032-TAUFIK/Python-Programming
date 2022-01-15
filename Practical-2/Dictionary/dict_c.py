#Sum of values of a dictionary

#function
def Sum(dic):
    sum=0
    #sum of values
    for i in dic.values():
        sum=sum+i
    return sum

#simple dictionary
c={ 'x':50, 'y':100, 'z':150}

#print dictionary
print('Dictionary : ', c)

#print sum
print('Sum : ',Sum(c)) 
