# lets say you want to work with multiple variables of the same kind; like with a set of colors
# you could have multiple variables

color1="red"
color2="green"
color3="blue"

# now it is a bit hard to work with that: if you want to deal with related information that you can make a list of it in python.

colors = [ "red", "green", "blue" ]  # this makes a list of the  three strings, the first element of the list is "red", the second element is "green", and the third one is "blue"

# how you can access he elements of the list conveniently like this:

print(colors[0]) # color[0] gives you he first element, which is the string "red". the  index of the first element is 0 that's a bit confusing,
                 # but it is possible to get used to that.  note that you have the index of the accessed element surrounded by [ and ] characters.

print(colors[1]) # color[1] gives you the second element, with the value "green"
print(colors[2]) # this one gives the third element, with the value "blue"

#print(colors[3]) # - in python this would give an error, you can't access the fourth element in the list, it has not been set, we got only three elements in the list.
                  # the errro is: "IndxError: list index out of range"

# you can also change an elment of a list like this.
colors[1] = "Green" # now the second element starts with a capital letter, instead of a lower case letter.

# you can add another element on top of the colors in an existing list by calling the append function.

# now this is something new: the name of the variable that holds the list is followed by a dot (.) that is followed by the function name append.
# this means that you are calling the function append to modify the list variable colors.

colors.append("yellow")

# this now displays the full list: ['red', 'green', 'blue', 'yellow']
print(colors)


# there are many other function that can be called with with lists, see the "methods" in this link https://python-reference.readthedocs.io/en/latest/docs/list/pop.html

# for example you can sort the list and print it out, this prints a sorted list of the colors: [ "blue", "green", "red", "yellow" ]
print(colors.sort()) 

# one thing you can do is to get a list of hundred elements with the value 0
numbers = [0] * 100


# ---
# Exercise: make a list of the numbers between 1 and 100 and print the square of each number. us a loop to make this list.
# hint: you can either call the append function to add new elements, or make a large enough list and change the values.
# you will get a list that looks like [1, 4, 9, 16, 25 ]
# remember that the first element of the list is accessed by the 0 index (colors[0], the second oen as colors[1], etc)
# ---

#---
# exercise:
# make a program that shows the sums of the squares between 1 and 100
# for the first number, it shows    1
# for the second number, it shows   5 = 1 + 4
# for the third number, it shows   14 = 1 + 4 + 9
# for the fourth number, it shows  30 = 1 + 4 + 9 + 16
#---

#----
# big exercise: find the prime numbers between one and 100; 
# prime numbers are the number that can only be divided by one and themselves, 
#   - 4 is not a prime number, as it can be divided by 2
#   - 7 is a prime number, it can be divided by itself.
# how to do that?
# you can make a list of all numbers between 1 and 100 
# make a loop that goes over all numbers between one and 100, for each of them mark the multiple of that number
# by putting a one in the array slow.
# like for two, mark 4, mark 8, mark 16, up to 100
# then add a second loop that goes over all numbers, and show the numbers that were not marked.
# ---


