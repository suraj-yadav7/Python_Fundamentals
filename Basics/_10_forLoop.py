# For loop
# A for loop is used to iterate over the string, lists, tuples, dicitonay, set

# looping through string
str='coding'
for i in str:
    print('str: ', i)

# looping through list
football_goal=[2,5,4,7,3]
for i in football_goal:
    print('Goals: ', i)

# Range function
# range function specifiy the range to iterate
for i in range(7):
    print("range: ",i)
# range from 3 t0 7
for i in range(3,7):
    print(i)
# range function increment by 3 from 1 to 10
for i in range(1, 10, 3):
    print("increment rnage: ", i)


# nested for loop
for i in range(3):
    for j in range(2):
        print(j)

# else in for loop
for i in range(5):
    print("j: ", i)
else:
    print("Finally iteration completed")

