import util

# visual studio code is a bit messad up with bidi support. 
# open issue since 2016 https://github.com/microsoft/vscode/issues/11770
# a workaround is to put bidi text into separate variables

heb="שלום לכולם"
heb2="שלום world"

util.printb( heb, 42 )
util.printb( heb2, 42 )

heb3="""הרבה many
שורות lines
של of
תוכנית code"""

util.printb(heb3)

#print(heb)
#print(heb2)

