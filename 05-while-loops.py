
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
