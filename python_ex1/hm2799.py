import copy
list1 = [[1, 2, 3], [4, 5, 6], ['a', 'b', 'c']]
list2 = list1
list3 = copy.copy(list1)
list4 = copy.deepcopy(list1)
print('List # \tID\tEntries')
print('1\t', id(list1), '\t', list1)
print('2\t', id(list2), '\t', list2)
print('3\t', id(list3), '\t', list3)
print('4\t', id(list4), '\t', list4)
list2[2][2] = 9
print('List # \tID\tEntries')
print('1\t', id(list1), '\t', list1)
print('2\t', id(list2), '\t', list2)
print('3\t', id(list3), '\t', list3)
print('4\t', id(list4), '\t', list4)
list1.append([0, 8, 15])
print('1\t', id(list1), '\t', list1)
print('2\t', id(list2), '\t', list2)
print('3\t', id(list3), '\t', list3)
print('4\t', id(list4), '\t', list4)


# Be careful when copying and referencing data structures!
# = is referencing to the original variable
# copy.copy() is a real copy (more memory)