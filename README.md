# My python course.

I am trying to teach my daughters how to program in python (summer vacation time, so it's time to teach something!) 
Now I am trying to prepare my notes on the subject, this is another opportunity to make things clearer to me, first of all.

My plan is to teach some basics, then doing stuff with the [turtle](https://docs.python.org/3/library/turtle.html) library, and then to do some games with the [pygames](https://www.pygame.org/wiki/GettingStarted) library (now i have to learn these libraries, to begin with...)

## Why should we learn how to program?

First of all programming is fun; it's a really enjoyable moment, when a program finally starts to work

Programming is a little bit like magic - in a sense we are creating things out of words. I think that this would also teach us about the value of words, and that their effect can be quite tangible as such.  I think that programming has some bigger lessons in life: If something doesn't work with a computer than we tend to search for work around solutions; this search for work around solution can be useful in other situations, just ask this [guy with the fire extinguisher](https://www.youtube.com/watch?v=NPW3mvAN0Rc). I think that the practice of programming is teaching us to get used to a mindset where we are more likely to look for another way of looking at the same problem.

Also: if we persist with this activity long enough then we will learn that there are a lot of trade offs involved in programming: sometimes greater speed comes with larger memory usage for example; in a sense computer programming is the land of trade offs. You get that quite a lot in life, where different choices have to be considered and evaluated with regards to their cost versus their benefit. I think it is a good idea to get some training in the art of trade offs.

Another aspect is that [software is eating the world](https://www.youtube.com/watch?v=UW5ktbit2s0), which is another incentive to learn about it all... [This article](https://daneshyari.com/article/preview/4941896.pdf) says that understanding how programs are written helps us understand the rules of how digitial systems work and helps to understand the assumptions made by the authors of the system; therefore they argue that understanding all this is required to 'fully participate in the discourse of our digital life' - so it would be somehow similar to civics. (" Metaphors of code—Structuring and broadening the discussion on teaching children to code" by Tomi Dufvaa and Mikko Dufva)

## Environment 

We are trying to use visual studio code with the microsoft python plugin.

1. To set it up: first download python from [here](https://www.python.org/downloads/), then install it.
2. Download visual studio code from [here](https://code.visualstudio.com/Download), then install it.
3. In visual studio code: press 'Extensions' button on the vertical bar (lowest icon), search for Python and install the first one in the list
4. Set autosave:
    1. in File menu: select Auto Save option, so that a checkmark appears
    2. in Code menu, select Preferences, then select settings, search for auto save, for Auto Save select afterDelay for Auto Save Delay select 1

## Which language is better for introducing programming, Python or LUA?

Python as a language for introducing programming has its weak points: it has a very confusing syntax, at least I think that the it is confusing to a learner for the following reasons:

1. The indentation business is quite confusing for a start, then some lines must end with a : symbol, followed by an increase in indentation; then watch out when indentation decreases, that means you get out of the block; that one is a too subtle cue for my liking.
2. The whole object thing - objects are already a hard thing to grasp, then why do we need the self argument in member functions?
3. Many features, sometimes more than one way to do things: functions can be called with positional argument, but also with keyword arguments [here](https://python.plainenglish.io/python-positional-arguments-vs-keyword-arguments-passing-variable-number-of-arguments-args-vs-8e1b0629828)

On the other hand python wins as a scripting language because it has a lot of libraries available, and it has descent tooling, as it is the most used scripting language.
Well, many things in the land of programming are far from ideal; Many arbitrary rules have their exceptions, take UNIX for example ('everything is a file', except for sockets; 'everything is a text file', except when it has a syntax; the unix permission thing...). On the other hand: sort of everything in programming is a kind of trade off, it's the land of trade offs.

Maybe the [LUA](https://en.wikipedia.org/wiki/Lua_(programming_language))  programming language has a less annoying syntax, but it's not used as widely as python, and it comes with less libraries, meaning that not all 'batteries are included', which means that for any given task you are more likely to find the tools for Python, [here](https://szabgab.com/batteries-included.html) they argue that this is the most important factor in programming language adoption.

However it turns out that in LUA there are good gaming libraries, like [LOEVE 2D](https://love2d.org/). This teaches us that occasionally there are lots of alternatives in software... And LUA has it's visual studio plugin [here](https://marketplace.visualstudio.com/items?itemName=trixnz.vscode-lua) In this reddit discussion ["How good is Lua as a language to teach children programming?"](https://www.reddit.com/r/lua/comments/hygw6j/how_good_is_lua_as_a_language_to_teach_children/) people argue that LUA is the better choice over python.

On the other hand: accessing a undefined variable in Lua is not an error, such variables get the nil value. I think the Python behavior of treating this as an error makes more sense.
Also Lua likes to do implicit conversion, like converting a string to a number, when used in an arithmetic operation. I think this often results in difficult situations, so that type conversion in python makes more sense, to me.

This kind of argument can go and on, so lets stick with python.
