str = input()

length = len(str)

half = int(length/2)

# half = length//2 to get int
sample = 'abcdabc'
print(length)
for i in range(half,0,-1):   # to get prefix and suffix from the 1st halfs
    print(i)                 # and 2nd half with decrementing lenght
    prefix = str[:i]         #getting char till half
    postfix = str[len(str)-i:] #getting 2nd half
    print(prefix,postfix)
    if postfix == prefix:
        print(True)
        break