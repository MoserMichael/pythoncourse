from bidi.algorithm import get_display


# variable length print, the string constants are adjusted for bidi.
# an unrelated editor is that vs code doesn't support bidi.
# the workaround is to put bidi text into separate string variables.

def printb(*args):
    print( get_display( ' '.join(map(str, args)) ) )
