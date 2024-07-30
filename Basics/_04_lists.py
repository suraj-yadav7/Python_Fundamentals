# Lists
# A list is built in datatypes that stores set of values
# It can store element of different datatypes (Int, float, strings, etc)

marks=[75,80,70,90,65]
print('List: ',marks)
print('list len: ', len(marks))
print('list indexing: ', marks[3])

# list updating
marks[2]=99
print('List after update: ', marks)

# list slicing
print("list: ",marks[:4])
print("list: ",marks[2:])
print("list: ", marks[-3:-1])

# list methods
# add element add end of list
marks.append(100)
print("after append: ", marks)
marks.insert(3,77)  #adding element at index 3
print('after insertion: ', marks)
marks.sort()
print("Sorted list: ", marks)
marks.sort(reverse=True)
print("Reverse sorted: ", marks)

# remove element
marks.pop() #remove last element
marks.pop(3) #remove given index element
marks.remove(90) #remove first occurance of element 90
print('Pop operation: ', marks)