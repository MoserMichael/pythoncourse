
# variables come in different kinds.
# one kind is a number, you already learned this:

# an integer are the number that can be counted 0, 1, 2, 3, .... and all the negative numbers -1, -2, -3, -4 ....
# the integer value to the right hand side of = is the number 13, this value is assigned to the variable a
a = 13
# showing the value of variable a on screen
print(a)

# a floating point number is a number with a fraction
b=99.99
# showing the value of variable b on screen
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

# now in python you need to convert the text to a number. if you want to add it. lets do it for the first number
# please note: if you try to convert a text with letters, and not a number then this will give you an error.
first_number=float(text_of_first_number)

# lets covert the second text string to a number
second_number = float(text_of_second_number)

# lets add the two numbers, then put the result into the variable named result.
# please note: if you try to convert a text with letters, and not a number then this will give you an error.
result = first_number + second_number

# now something new: you can show several values on screen by separating them with a comma.
print("the result", result)


-----
# exercise: write aprogram that asks for the length of the radius of a circle, that computes the square of the circle with given radius and displays it on the screen.

# exercise: write a program that asks for the length of the two sides of a rectangle, that computes the square of the rectange, and that prints the result.
