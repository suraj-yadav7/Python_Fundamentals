# Dictionary 
# It stores data in key:value pair, don't allow duplicate keys
dict ={
    'name':'john doe',
    'age':25,
    'tasks':[5,10,15]
}
print('Dictionary: ', dict)
# Adding element
dict['location']='USA'
dict['work']='WFO'
print("after adding element: ", dict)
# Accessing element
x=dict.get('tasks')
print("access value using key: ", x)
# only keys
print('Dict keys: ', dict.keys())
#only values
print('Dict values: ', dict.values())

# update values
dict.update({'age':26})
print("After updation: ", dict)
dict['tasks']=[3,6,9,12]
print("after updating: ", dict)

# removing element
dict.pop('work')
del dict['location']
print("After removal: ", dict)

# copying dictionary
dict2= dict.copy()
print('Second dictionary: ', dict2)
