
# sometimes you need to do something over and over again.
# like counting from one to ten, and summing up the square of each number.
# that's where we have while loops.


counter = 0
sum_of_squares = 1

# the statements inside the while loop is done, while the condition counter < 10 is true. 
# the while statement is completed, if counter is greater or equal to 10.
while counter < 10:
    # advance the counter value,
    counter = counter + 1
    # computing the sum of squares
    sum_of_squares = sum_of_squares + counter * counter

print("the sum of squares from one to ten is")
print(sum_of_squares)   


# exercise: write a program to compute the factorial for any given number.
# the factorial for 5 is 1 * 2 * 3 * 4 * 5
# incidentially the number of combinations of n things is the factorial of n

# here is a good video that explains the reason for this https://www.youtube.com/watch?v=elzVyTtMbiM
# that's an example of mathematical induction: where you compute the forumula for n via concluding how to extend the case of n-1 to it.

# exercise: write a program that computes the factorials for the numbers from one to 30 

# exercise: a pythagorean triple are three integer number a,b,c so that a*a = b*b + c*c.
# An example is 1,3,10 as 1*1+3*3=10   or 4,3,25  as 4*4+3*3==25
# now write a program that finds all pythagorean triples where the largest number is between 1 and 100


# --- 
# exercise: write a program that prints out the multiplication table, like this.
# 1   2   3   4   5   6 ..
# 2   4   6   8  10  12 ..
# 3   6   9  12  15  18 ..
# note: you will need a loop within a loop.
# ...


