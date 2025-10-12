import math

list1=range(1,6)
list2=range(11,16)

list_zip = []
for i in range(len(list1)):
    list_zip.append(list1[i])
    list_zip.append(list2[i])

print(list_zip)

list_odd = []
for x in list1:
    if x % 2 != 0:
        list_odd.append(x)

for x in list2:
    if x % 2 != 0:
        list_odd.append(x)

print(list_odd)

list_zip_copy = list_zip.copy()
list_zip_copy.reverse()
list_zip_reverse = list_zip_copy


print(list_zip_reverse)

        