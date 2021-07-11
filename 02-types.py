
# variables come in different kinds.
# one kind is a number, you already learned this:

# an integer are the number that can be counted 0, 1, 2, 3, .... and all the negative numbers -1, -2, -3, -4 ....
# the integer value to the right hand side of = is the number 13, this value is assigned to the variable a
a = 13
print(a)

# a floating point number is a number with a fraction
b=99.99
print(b)


# the value to the right hand side of = is a text, this type of value is a string.
# the string value to the right of = is the the string between the " signs (the " signs are not part of the string value)
c = "this is a text"    

# this displays the string value which is: this is a text (see that the " sign is not part of the string value)
print(c)


# lets make a calculator that knows how to add things;


# the fuction input display the text string that is passed to it as arguments between the ( and ) signs. it then asks for a value.
text_of_first_number=input("enter the first number: ")

# read the string value of the second variable.
text_of_second_number=input("enter the second number: ")

# now in python you can't add two text string values, you need to convert the text to a number. lets do it for the first number
first_number=float(text_of_first_number)
# lets covert the second text string to a number
# please note: if you try to convert a text with letters, and not a number then this will give you an error.
second_number = float(text_of_second_number)

# lets add the two numbers, then put the result into the variable named result.
result = first_number + second_number

print("the result")
print(result)