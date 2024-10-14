list1 = [1, 2, 3, 4, 5]
list2 = [11, 12, 13, 14]

list_zip = []
i = 0

while i < len(list2):
    list_zip.append(list1[i])
    list_zip.append(list2[i])
    i += 1

print(list_zip)

