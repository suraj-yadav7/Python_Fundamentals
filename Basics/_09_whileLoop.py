# While loops
num=7
i=0
while i<num:
    print("Num: ", i)
    i +=1

# break statement in while
# break the entire loop 
num2=8
j=0
while j<num2:
    print("i val: ", j)
    if j==4:
        break
    j+=1

# continue statement in while
# With the continue statement we can stop the current iteration, 
# and continue with the next:
num3=1
k=10
while k>num3:
    k-=1
    if k==5:
        continue
    print("K is : ", k)

# else in while
# it runs only at once when condition is not true
num4=5
l=0
while l<num4:
    print('L : ', l)
    l+=1
else:
    print("L is no longer lesser than num4", l)
