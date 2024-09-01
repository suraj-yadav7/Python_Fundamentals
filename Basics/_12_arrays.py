# Arrays in python
# Python does not have built-in support for Arrays, but Python Lists can be used instead.
laptops = ['acer', 'asus', 'msi', 'hp', 'dell', 'lenovo']
print("All laptops: ", laptops)
# array length
print("length of arrays: ", len(laptops))

# accessing element of array
x=laptops[2]
print(x)
print("laptop: ", laptops[3])

# update exsiting array element
laptops[5]='infinix'
print("Modified laptops array: ", laptops)

# adding new element in array
laptops.append('xiaomi')
print("after adding: ", laptops)

# removing element from array
laptops.pop()
laptops.pop(1)
print("laptops: ", laptops)

evenNums = [4,2,8,6,12,14,10]
# sort
evenNums.sort()
print("sort: ", evenNums)
# reverse
evenNums.reverse()
print("reverse: ", evenNums)

# looping through array elements
for i in laptops:
    print("elem: ", i)


