#import the sys module, that tells us that we can use all functions defined in the sys module.
import sys

# the fuction input display the text string that is passed to it as arguments between the ( and ) signs. it then asks for a value.
text_of_first_number=input("enter the first number: ")

# lets read the operation
oper = input("operation: ")

# read the string value of the second variable.
text_of_second_number=input("enter the second number: ")

# now in python you can't add two text string values, you need to convert the text to a number. lets do it for the first number
first_number=float(text_of_first_number)
# lets covert the second text string to a number
# please note: if you try to convert a text with letters, and not a number then this will give you an error.
second_number = float(text_of_second_number)


if oper == "*":
    # What is run if the condition is true: see that the line is indented. 
    # That's a feature of the python programming language ;-(
    result = first_number * second_number

# now something new: elif - if oper is not "*" then it runs the next if condition: if oper == "/" - 
# this makes it much easier to chain a bunch of if confitions to test out all cases.
elif oper == "/":
    result = first_number / second_number
elif oper == "+":
     result = first_number + second_number
elif oper == "-":
     result = first_number - second_number
else:
    # if the variable oper is not equal to any of the handled operations, then print an error message
    print("error: illegal operand!")    
    # exit the program. (we are calling the function exit from the sys module)
    # please note that we have the name of the module sys, followed by a . sign, then the name of the function followed by ()
    # every function call has the argument passed within ( and ) - just like with the print function
    sys.exit(1)

print("the result:") 
print(result)               

  

