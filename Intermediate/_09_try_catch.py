# Try- Except
# the try-except block is used to handle exceptions and errors gracefully,
# ensuring that your program can continue running even when something goes wrong.

def numDivision(denom):
    try:
        result =10/denom
        return result
    except ZeroDivisionError:
        print("Got division error")
    except ValueError:
        print("Error: Invalid input. please enter a valid number.")
    finally:
        print("It alway run in function")
denominator = 3
div = numDivision(denominator)
print("Division: ", div)

# Nested try_catch
def numMul(num):
    try:
        two_num = num*2
        try:
            square=two_num*num
            return square
        except ValueError:
            print("Error: Invalid input. please enter a valid number")
        finally:
            print("Multiplication is performed")
    except Exception as excp:
        print("Function got error", excp)

num=25
mul = numMul(num)
print("Multiplication: ", mul)