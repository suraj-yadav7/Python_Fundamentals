# $$ Airthmetic operators $$
# +,-,*,/,%
a=10
b=20
print('Addition: ', a+b)
print('Substraction: ',a-b)
print('Multiplication: ', a*b)
print('Division (coefficient): ',b/a)
print("Modules (remainder): ", b%a)

# $$ Relational Operators $$
#  >,>=, <,<=, !=, ==
num1=15
num2=25
print("Greater than: ", num2>num1)
print("less than: ", num1<num2)
print("Equal to: ", num1==num2)

# Assignment Operator $$
#  =, +=, -=, /=, %=, *=
x=3
y=9
x+=4
y*=2
print('Assignment addition: ',x )
print('Assignment multiplication: ',y )

# $$ Logical Operators  $$
#  and , or , not
val1=11
val2=22
# both condition must be true
print("Logical and: ", val1>0 and val2<25)
# atleast one condition need to be true
print("logical or: ", val2>25 or val1>0)

# $$ Membership Operator $$
#  in, not in
arrEven=[2,4,6,8]
print("in operator: ", 2 in arrEven)
print('not in operator: ', 2 not in arrEven)

# $$ Identity Operator $$
# is , is not
# is -> Returns True if both objects refers to same memory location, else returns False
arr1=[1,3,5,7,9]
arr2=[1,3,5,7,9]
arr3=arr1
print('is operator: ', arr1 is arr2)
print('is not operator: ', arr1 is not arr2)
print('is operator when same memory location: ', arr1 is arr3)

# $$ Type Casting  $$
p=7
q="14"
print("P type: ", p, type(p))
print("Q type: ",q,  type(q))
q=int(q)
print("After type casting: ", q, type(q))

# $$ Type Conversion $$
n=3
m=6.0
print('conversion to float', m+n, type(m+n))

# $$ input Function $$

inVal=input("Enter your favorite number: ")
print("Input values is always: ", inVal, type(inVal))
inVal2=int(inVal)
print("Casting to ineger: ", inVal2, type(inVal2))
