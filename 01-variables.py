# programming is the art of telling the computer how to do stuff.
# We need to learn the rules of a programming language for that, a programming language is what the computer can understand.
# here we are learning the python programming language.

# a programming language is much much simpler then learning a real language; it has less rules and less words in it.
# however one has to keep the rules.

# in python: everthing you put after the # is a comment; this is an explanations, the computer ignores this text
# a comment is written for a human to read, not for the computer to do work with.   


# a variable is like a drawer: you can put some data in it.
# each variable has a name

# variable a: if the name of the variable is on the left of the = sign, then you put something in the drawer,
#  you put a value in the variable

a = 3

b = 40

# if you put the variable on the right of the = sign, then you pull the value out of the drawer in order to use it, you look up the value of the variable.
# here you first get the value of a, that is 3
# then you get the value of b, that is 40
# then you add these numbers up (40 + 3)
# finally: the result 43 is put into the variable c
c = a + b

# This is a function call, functions do things.
# Here we tell the function print to get the value of variable c from the drawer, and to print it on the screen
# Note that first you see the name of the function - print, then you get the ( sign followed by the name of the variable 
# That is to be printed, then all this is closed with the ) sign.
#
print(c)

# other things you can do with variables; you can multiply them
# the * sign says: take the value of variable a, the value of variable b and multiply them.
# The result is then assigned to the new variable d/
d = a * b
print(d)

# and you can divide them
# the / sign says: take the value of variable a, the value of variable b and divide a by b.

e = a / b
print(e)

# variable names can consists of letter, digits and the underscore sign _
variable_name2 = 1234567

# another important rule:
# if you try to use a variable that has not been asigned an value, then this is an error.

# this is an error, the variable variable_name3 has never been assigned a value, so i put the next line in a comment.
# print(variable_name3)