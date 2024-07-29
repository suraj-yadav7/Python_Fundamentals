# Printing Different values
print('Hello World')
print(2024)
print(True)
print([2,4,6,8])
print({'name':'suraj'})

# $$$$$ Datatypes in python  $$$$$$
#$$ Numeric $$
#Integer
num=46
print("Integer: ",num)

#Float
pi=3.14
print("float", pi)

#Complex
com_num = 3+5J
print("Complex number: ", com_num)
print("Complex number: ", type(com_num))

#$$ Sequence $$
#String
str="Engineer"
str2='''Code
        Everyday'''
print("String: ",str)
print("MutliLine String: ",str2)

#List
#List is similar to array but items can be different types
list_bike=['pulsar', 'royal', 'duke']
print("List items:",list_bike[1])
print("type of:", type(list_bike))

#Tuple
#tuple is ordered collection and immutable
tuple_mobile=("samsung","oneplus","moto")
tuple_odd =(1,3,5,7,9)
print("tuples: ", tuple_mobile)
print('tuple num: ', tuple_odd)
print("Tuples access: ", tuple_mobile[2])

# $$ Boolean $$
present = True
absent = False
print("Student Present: ", present)
print("Student absent: ", absent)

# $$ Set $$
#It is unodered, iterable, mutable  and no duplicate element
unique_str=set("programming")
uniqu_num = set([2,3,3,5,7,7,9,1])
print("Set number: ", uniqu_num)
print("Set string: ", unique_str)
unique_str.add("life")
print("Set after adding element: ", unique_str)

# $$ Dictionary $$
my_dict={'earbud':'oneplus', 'laptop':'acer', 'model':'2023'}
print("Dictionary: ", my_dict)
print("access dict: ", my_dict['laptop'])
my_dict['amount']=20000
print("after adding element: ", my_dict)

