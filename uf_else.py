''' Demonstrating how a conditional statemtn (if/else) works it asks for the user for a
password and then checks if it is correct'''

# Ask for password and store in variable
password = input("Enter your password")

# Check if it is correct
if password == "carrott" : 
    print ("Well done, you entered the correct password!!")
else :
    print ("Invalid password, please re-enter correct password!!")