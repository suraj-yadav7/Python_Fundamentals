# Tuples
# Tuples store different types of element in ordered sequence.
# This are immutable, means add,remove not supported.
# It allow duplicate and uses paranthesis for storing '()'
mobile=('samsung', 'oneplus', 'moto', 'realme',33, 44, 33)
earbuds=('realmepro', 'nothing1')
print('Tuples: ', mobile)

# Tuple methods
print("Tuples access: ", mobile[1])
print("tuple count: ", mobile.count(33))
print('tupled index: ', mobile.index(33))
print("Joint two tuples: ", mobile+earbuds)

# adding element tuples still though it is immutable
# using list
listTuple=list(earbuds)
listTuple.append('oneplesbuds')
earbuds=tuple(listTuple)
print("Updated tuple: ", earbuds)

#using + operator
y=('mibuds',)
earbuds +=y
print("updated using + : ", earbuds)

# removed can be done same way