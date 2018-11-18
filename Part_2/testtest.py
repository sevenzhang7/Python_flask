import operator

l1 = [["1,2,3,4"],["3,2,3,4"],["2,3,3,4"]]

#i = 1 
#for i in range(len(l1)):


l1.sort(key=operator.itemgetter(0))

print(l1)


