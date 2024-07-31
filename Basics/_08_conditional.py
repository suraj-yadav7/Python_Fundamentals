# Conditional Statement
# if-else statement
score=300
if (score>400):
    print("Score is higest")
else:
    print("Score is lowest")

# if-elif statement
marks=85
if(marks > 70 and marks<80):
    print("Good marks grade A")
elif(marks >80 and marks<90):
    print("Very good marks grade A+")
elif(marks>90 and marks<=100):
    print("Excellent marks grade O")
else:
    print("Need to improve marks")

# Nested if-else statement
salary=1600
if salary>500:
    if(salary<1500):
        print('Need increment')
    else:
        print('Dont need increment')
else:
    print('Salary is very less')

# Short hand of if
a=10
b=5
if a>b : print("a is : ", a)

# Short hand of id-else
print("A value: ", a) if a<b else print('B value: ',b)

# Ternary operator
min = 'a is minimum' if b>a else 'b is minimum'
print("Ternary operator: ", min)