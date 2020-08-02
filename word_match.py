#program that matches a word containing 'z' , not at the start or end of the word
import re
def text_match(text):
    patterns='\Bz\B'
    if re.search(patterns,text):
        return'Found a word containing z!'
    else:
        return('The word not containing Z!')

print(text_match("specialization"))
print(text_match("raghav is very lazy boy"))
print(text_match("welcome to aurangabad"))

      
    
