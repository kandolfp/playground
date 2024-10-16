

list1 = [1, 2, 3, 4, 5]
list2 = [11, 12, 13, 14, 15]

list_zip2 = []
i= 0
while i<5:
    i = i+1
    list_zip2.append(list1[i - 1])
    list_zip2.append(list2[i - 1])

print(list_zip2)


list_odd= []
i2 = 0

while i2 < 10:
    
    # checking condition
    if list_zip2[i2] % 2 != 0:
        list_odd.append(list_zip2[i2])
        
    i2 += 1 
print(sorted(list_odd))



list_zip_reverse = []
i= 0
while i<5:
    i = i+1
    list_zip_reverse.append(list1[-i ])
    list_zip_reverse.append(list2[-i ])

print(list_zip_reverse)
