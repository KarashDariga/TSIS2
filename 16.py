list1 = [11, 24, 8, 14, 5 ] #list  #el it's element
# list2 = []
#for el in list1:
#    if el % 2  == 0:
#        list2.append(el)
list2 = [x for x in list1 if x % 2 == 0]
print(list2) 