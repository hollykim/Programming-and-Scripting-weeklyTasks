# This program will ask to the user to put any positive integer and will give outpus 
# as the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one.
# This program end if the current value is one.
# Author: Hyojin

num = int(input ("please enter a positive integer: "))

if num <= 0:
    print ("It's not a positive number")
else: 
    if num % 2 == 0:
        while num == 1:
            print (num, sep="", end="")
    else:
        while num == 1:
           print (num, sep="", end="")


print ("Done!") 