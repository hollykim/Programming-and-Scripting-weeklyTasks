# this program takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Hyojin Kim
# resource: https://www.learndatasci.com/solutions/python-square-root/#:~:text=of%20each%20option.-,Option%201%3A%20The%20Exponentiation%20Operator%20**0.5,as%20shown%20in%20the%20introduction.
# resource: https://realpython.com/python-square-root-function/, https://docs.python.org/3/library/functions.html#round
# resource: https://stackoverflow.com/questions/3047012/how-to-perform-square-root-without-using-math-module


inputNum = float (input ("Please enter a positive number: ")) # get input from the user
def sqrt(a): # will find the input's square root by power 0.5
    inputSquare = a ** 0.5
    print (round(inputSquare,1)) # Return number rounded after the 1 decimal point.
    return inputSquare

sqrt(inputNum)

