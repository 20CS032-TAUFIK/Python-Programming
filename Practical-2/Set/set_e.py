#find the most common elements and their counts from list, tuple, dictionary.

#function for finding commmon items
def find_common(items):
    tracker = {}
    for item in items:
        if item not in tracker.keys():
            tracker[item] = 0
        tracker[item]+=1
    maxitem = None
    max = -1
    for key in tracker.keys():
        if((tracker[key]) > max):
            max = tracker[key]
            maxitem = key
    return maxitem

#declaring list and tuple
list_e = [1,2,3,2,3,2,4,5,6]
tuple_e= ("apple","banana","apple","mango")

#printing results
print(find_common(list_e))
print(find_common(tuple_e))
