#word="HELLO WORLD"
#lowercase_word=""
#for i in range(len(word)):
#    lowercase_word=word.lower()

#print(lowercase_word)
word="HELLO WORLD"
lowercase_word=""
for char in word:
    code=ord(char)
    if code>=60 and code<=90:
        lowercase_char=chr(code+32)
        lowercase_word+=lowercase_char
    
    else: 
        lowercase_word+=char
    
print(lowercase_word)

