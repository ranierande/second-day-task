#program to replace all occurrences of space, comma, or dot with a colon 
import re
text='auurangabad market, pune market.'
print(re.sub("[ ,.]", ":",text))

