# Defining python function
def airthmeticOperation(age):
    if(age>14 and age<18):
        print("You are not eligible to GYM")
    elif(age> 18 and age<50):
        print("Your most welcome")
    elif(age > 50):
        print("Need to workout in supervision")
    else:
        print("Play outdoor sports")
# callling function
airthmeticOperation(51)

# nested function
def checkPrime(num):
    # loop iterating
    if(num > 1):
        for i in range(2, num):
            if(num % i == 0):
                print("Number is not prime: ", num)
                break
        else:        
            print("Number is prime: ", num)

def numIsPrime(num):
    if(num == 0 or num ==1):
        print("Provide valid number")
    if(num>1):
        # calling main function
        checkPrime(num)
# function call
numIsPrime(7)

# Recursive function
def factorialNum(num):
    if(num == 0 or num == 1):
        return num
    else:
        return num*factorialNum(num-1)
# calling recursice function
num=5
fact = factorialNum(5)
print("Factorial of",{num} ,"is: ", fact)