list1 = [1, 2, 3, 4, 5]
list2 = [11, 12, 13, 14, 15]

i=0
list_zip=[]
while i<len(list1):
	list_zip.append(list1[i])
	list_zip.append(list2[i])
	i+=1
print(list_zip)

list_odd=[]
for i in list1:
	if i % 2 == 1:
		list_odd.append(i)
for i in list2:
	if i % 2 == 1:
		list_odd.append(i)
print(list_odd)

list_zip_reverse=list_zip
list_zip_reverse.reverse()
i=0
while i < len(list_zip_reverse)-1:
	temp=list_zip_reverse[i]
	list_zip_reverse[i]=list_zip_reverse[i+1]
	list_zip_reverse[i+1]=temp
	i+=2
print(list_zip_reverse)
