import math

list1 = [1, 2, 3, 4, 5]
list2 = [11, 12, 13, 14, 15]
list_zip = []

i = 0
while i<5:
    i = i+1 
    list_zip.append(list1[i -1])
    list_zip.append(list2[i -1])

print(list_zip)
