from bidi.algorithm import get_display


# variable length print, the string constants are adjusted for bidi.
# an unrelated editor is that vs code doesn't support bidi.
# the workaround is to put bidi text into separate string variables.

def printb(*args):
    def adjustStr(arg):
        if type(arg) == "<class 'str'>":
            return get_display(arg)
        return str(arg)

    print( get_display( ' '.join(map(adjustStr, args)) ) )
    
