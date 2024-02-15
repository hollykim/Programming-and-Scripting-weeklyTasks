# This program will ask to the user to put any positive integer and will give outpus 
# as the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one. This program end if the current value is one.
# Author: Hyojin
# ref: https://codereview.stackexchange.com/questions/285429/automate-the-boring-stuff-with-python-the-collatz-sequence#:~:text=Write%20a%20function%20named%20collatz,return%203%20*%20number%20%2B%201%20.


num = int(input ("please enter a positive integer: "))

# put condition that the user need to put a positive number
if num <= 0:
    print ("It's not a positive number")

#if the user put number 1, the while loop won't work. So I added this condition to make sure it's run 
# elif num == 1:
#     num = (num*3)+1 
#     print (num, sep=" ", end=" ")
#     while num != 1:
#         if num % 2 != 0:
#             num = (num*3)+1
#             print (num, sep=" ", end=" ")
#         else:
#             num = int(num/2)
#             print (num, sep=" ", end=" ")      
else: 
# if num is even will do num*3+1, if it's odd will do /2 and this loop will run until num is equal to 1.
    while num != 1:
        if num % 2 != 0:
            num = (num*3)+1
            print (num, sep=" ", end=" ")
        else:
            num = int(num/2)
            print (num, sep=" ", end=" ")        


# The original code I made 

num1 = int(input ("please enter a positive integer: "))

if num1 <= 0:
    print ("It's not a positive number")       
else: 
        while num1 != 1:
            if num1 % 2 != 0:
                num1 = (num1*3)+1
                print (num1, sep=" ", end=" ")
            else:
                num1 = int(num1/2)
                print (num1, sep=" ", end=" ")        


# below is some cod I have tried. I thought while the num is equal to 1, it'll running but it was my misunderstanding.
        
# while num == 1:     
#     if num % 2 == 0:
#        print (num, sep="", end="")
#        num / 2
#     else: 
#         print (num, sep="", end="")
#         num = (num * 3) + 1
    

# if num > 0:
#     while (num == 1):
        
#         if num % 2 != 0:
#             print (num)
#             while (num%2 == 0):
#                 num = (num*3)+1
#                 print (num)
#         if num % 2 == 0:
#             num = num / 2
#             print (num)   
#     print (num)


# if num % 2 != 0:
#     print (num)
#     num = (num*3)+1
#     print (num)
# else:
#     print (num)
#     num = int (num/2)
#     print (num)