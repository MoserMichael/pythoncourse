

# Our programs were a sequence of sequence of statements, what would happen if we have two sequences of identical statements in the program that are used twice? 
# Correct - we would have two copies of these sequences. This approach comes with its problems; if we find a bug in one instance, 
# then we have to fix it in the other one too, this means we have to remember where these identical sequence of statements are in the program. 
# All this gets very difficult to handle, as our programs grow larger.

# The solution to this problem are functions, a function is a grouping of a common sequence of statements, that can be used from any point in the program. 
#  We are actualy using functions already, when we print something on the screen - in this case the print function is called. 
# In this lesson we are learning, how to define our own functions.

import math

# now this defines a function that computes the length of the third side (hypotenuse) in a square triangle.

# a function definition starts with def,followed by the name of the function.
# the list of arguments that the function receives is listed between the ( and ) signs
def square_triangle(side_a, side_b):
    # the code that is run when the funcion square_triangle is being called, again it is indented (like with if and while statements)
    # here we define a variable square_of_third_side that is only visible in the function square_triangle
    square_of_third_side = side_a*side_a+side_b*side_b
    return math.sqrt(square_of_third_side)


# calling the function that we have just defined!
side_c = square_triangle(2,3)
print("the hypotenuse of the square triangle:", side_c)
