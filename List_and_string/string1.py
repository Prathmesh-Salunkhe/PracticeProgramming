word = input()
outputword = ""

for ch in word:
    if ch not in outputword:
        outputword += ch
print(outputword)
rev = outputword[::-1]
print(rev)

#optimized way
#to get unique items we use dictionary as each key in dictionary is unique

dict = dict.fromkeys(word)
print(dict)
dict = list(dict)
dict.reverse()
print(dict)
rev = ''.join(dict)  #joins the key of dict with the character in between
print(rev)

rev='*'.join(dict) #output: 'r*t*s'
print(rev)
print(type(rev))