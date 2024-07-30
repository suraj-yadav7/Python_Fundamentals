# STRING 
# string is datatype that stores a sequence of characters
str='programming'
print("string: ", str)

# concatenation
str1='Code'
str2='Everyday'
print("string concatenation: ", str1+str2)
print("string concatenation: ", len(str1+str2))

# Indexing
str3='python code'
print('Indexing: ', str3[5])

# slicing
print("slicing: ", str3[:4])
print("slicing: ", str3[0:])
print("slicing: ", str3[2:6])

# String Methods
print("Ends With: ",str3.endswith('def'))
print("Capitalize: ",str.capitalize())
print("Count: ", str3.count('o'))
print("find: ", str3.find('o'))