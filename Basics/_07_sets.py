# Sets 
# It store unique element in a unordered, unchangeable, unindexed

thisset={'testing','devops', 'cloud'}
print('Set: ', thisset)

# adding element 
thisset.add('data')
print("Adding: ", thisset)

# existing element cannot be updated
# but second set can be cominbed
set2={'frontend', 'backend'}
thisset.update(set2)
print("After updating 2ns set: ", thisset)

# removing element
thisset.remove('testing')
print("After removing: ", thisset)
thisset.pop()
print("pop remove element randomly: ", thisset)

# Accessing set is possible with forloop 