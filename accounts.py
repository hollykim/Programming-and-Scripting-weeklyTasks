# Weekly task 03: This program will store bank account numbers as 10 character strings
# then display the last 4 digits only (first 6 digits replaced with Xs)
# If the user puts more or less than 10 digits, it won't run 
# I will improve this once I learn the loop so I can ask again until the user puts correct digits and account number 
# Author: Hyojin Kim


accountNum = str(input ("Please enter your 10 digits account numbers: "))
print (accountNum)
lenghtOfAcoount  = len(accountNum)

# Make condition that account number need to be 10 digits. 
if lenghtOfAcoount != 10:
    print ("Error! The account number has to be 10 digits")
if lenghtOfAcoount == 10:
    print(f"The lenght of {accountNum} is {lenghtOfAcoount}".format(accountNum,lenghtOfAcoount))
    # Get last 4 digits of account and Frist 6 digits then print it for checking
    first6Digits = accountNum[:6]
    print ("Frist 6 digit is " + first6Digits)
    last4Digits = accountNum[-4:]
    print ("Last 4 digit is " + last4Digits)

    # Change the first digit to Xs
    first6Digits = "xxxxxx"

    # Print the result
    print (f"Your account number is {first6Digits}{last4Digits}".format(first6Digits,last4Digits))



# Below part is what I have used for practice and a source I found about the slice.
    
# Get account number except last 4 digits and change to Xs
#print ("First 6 digits of your account is: " + accountNum[numOfLastDigit + 4])

# Source from: https://www.geeksforgeeks.org/python-get-last-n-characters-of-a-string/
# get input 
# Str = "Geeks For Geeks!"
# N = 4
 
# # print the string
# print(Str)
 
# # get length of string
# length = len(Str)
 
# # create a new string of last N characters
# Str2 = Str[length - N:]
 
# # print Last N characters
# print(Str2)

