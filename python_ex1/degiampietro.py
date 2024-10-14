list1 = [1, 2, 3, 4, 5]
list2 = [11, 12, 13, 14, 15]

list_zip = []
i = 0
while i < len(list1):
    list_zip.append(list1[i])
    list_zip.append(list2[i])
    i = i+1
print(f"{list_zip=}")

list_zip_reverse = []
i = 0
j = len(list1)-1
while i < len(list1):
    list_zip_reverse.append(list1[j-i])
    list_zip_reverse.append(list2[j-i])
    i = i+1
print(f"{list_zip_reverse=}")

list_odd = []
for item in list1:
    if item%2:
        list_odd.append(item)
for item in list2:
    if item%2:
        list_odd.append(item)
print(f"{list_odd=}")