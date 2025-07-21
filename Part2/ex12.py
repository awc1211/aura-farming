def checkstring(word):
    if word[0:3] == "The":
        return "Found It!"
    else:
        return "Nope."

str1 = 'The'
str2 = 'Thumbs up'
str3 = 'Theatre can be boring'

print(checkstring(str1))  
print(checkstring(str2)) 
print(checkstring(str3))   