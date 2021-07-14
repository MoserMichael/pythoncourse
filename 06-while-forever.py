import random
import time

# here the loop goes on and on, the condition True says that this loop goes on forever.
while True:

    # get a random number between zero and 80 - call randint function from the random module.
    number_of_spaces = random.randint(0, 80)


    # make a string with the number of spaces that equals to the number held in the number_of_spaces variable
    spaces_counter = 1
    spaces_string = " "

    # run the loop while spaces_counter is smaller than number_of_spaces
    while spaces_counter < number_of_spaces:
        # increase the spaces_counter by one
        spaces_counter = spaces_counter + 1
        # add another spaces to the spaces_string variable
        spaces_string = spaces_string + " "

    # print a line with the string of spaces, followed by a star character
    print(spaces_string + "*")    

    #sleep for one tenth of a second, so tht the screen will not scroll to fast
    time.sleep(0.1)
    
