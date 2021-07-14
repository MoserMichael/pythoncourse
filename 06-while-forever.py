import random
import time

while True:
    number_of_spaces = random.randint(0, 80)
    spaces = 1
    spaces_string = " "
    while spaces < number_of_spaces:
        spaces = spaces + 1
        spaces_string = spaces_string + " "

    print(spaces_string + "*")    
    time.sleep(0.1)
    
