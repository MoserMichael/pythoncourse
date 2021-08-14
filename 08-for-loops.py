

# another way of goint over a list of elements,

colorlist=[ "red", "orange",  "yellow", "green", "blue", "violet" ]

# we print all the colors of the rainbow as a while loop.

i=0
while i<len(colorlist):
    print(colorlist[i])
    i=i+1

# but we can also do it as a for loop - which is a shorter form for the same thing.
for color in colorlist:
    print(color)

# the for loop can also be used to show a range of numbers from 1 to 41 (not including 42)
# note that the range function returns something like a list of the number between 1 and 41
for num in range(1,42):
    print(num)

