# My python course.

I am trying to teach my daughters how to program in python (summer vacation time, so it's time to teach something!) 
Now I am trying to prepare my notes on the subject, this is another opportunity to make things clearer to me, first of all.

My plan is to teach some basics, then doing stuff with the [turtle](https://docs.python.org/3/library/turtle.html) library, and then to do some games with the [pygames](https://www.pygame.org/wiki/GettingStarted) library (no i have to learn these libraries, to begin with...)

## Environment 

We are trying to use visual studio code with the microsoft python plugin.

1. To set it up: first download python from [here](https://www.python.org/downloads/)
2. Download visual studio code from [here](https://code.visualstudio.com/Download)
3. In visual studio code: press 'Extensions' button on the vertical bar (lowest icon), search for Python and install the first one in the list
4. Set autosave:
    1. in File menu: select Auto Save option, so that a checkmark appears
    2. in Code menu, select Preferences, then select settings, search for auto save, for Auto Save select afterDelay for Auto Save Delay select 1

## why python?

I actually dislike python as a language for introducing programming, it has a very confusing syntax, at least I think that the it is confusing to a learner for the following reasons:
    1. The indentation business is quite confusing for a start, then some lines must end with a : symbol, followed by an increase in indentation; then watch out when indentation decreases, that means you get out of the block; that one is a too subtle cue for my liking.
    2. The whole object thing - objects are already a hard thing to grasp, then why do you need to call member functions as self.foo(), and why do they have self as first argument?
    3. The standard library is sometimes not very consistent - like ```del map[key]``` - why no parenthesis around the arguments for del?

On the other hand python wins as a scripting language because it has a lot of libraries available, and it has descent tooling, as it is the most used scripting language.
Well, many things in the land of programming are far from ideal - like UNIX for example ('everything is a file, except for sockets, everything is a text file, except when it has a syntax, the permission thing...). On the other hand: sort of everything in programming is a kind of trade off, it's the land of trade offs.
