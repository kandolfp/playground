list1 = [1, 2, 3, 4, 5]
list2 = [11, 12, 13, 14, 15]

# list_zip: abwechselnd Elemente aus list1 und list2
list_zip = []
for i in range(len(list1)):
    list_zip.append(list1[i])
    list_zip.append(list2[i])

# list_odd: ungerade Zahlen aus list1 und list2
list_odd = []
for x in list1:
    if x % 2 != 0:
        list_odd.append(x)
for y in list2:
    if y % 2 != 0:
        list_odd.append(y)

# list_zip_reverse: wie list_zip, aber rückwärts
list_zip_reverse = []
for i in range(len(list1)-1, -1, -1):
    list_zip_reverse.append(list1[i])
    list_zip_reverse.append(list2[i])

print("list_zip =", list_zip)
print("list_odd =", list_odd)
print("list_zip_reverse =", list_zip_reverse)