list1 =[1, 2, 3, 4, 5]
list2=[11, 12, 13, 14, 15]
list_zip = []

for i in list1:
  list_zip.append(list1[i - 1])
  list_zip.append(list2[i - 1])
print(list_zip)

list_zip_reverse = []
for i in list1:
  list_zip_reverse.append(list1[0 - i])
  list_zip_reverse.append(list2[0 - i])
print(list_zip_reverse)

list_odd = []

for i in list1:
  if i % 2 != 0:
    list_odd.append(i)
for i in list2:
  if i % 2 != 0:
    list_odd.append(i)
print(list_odd)