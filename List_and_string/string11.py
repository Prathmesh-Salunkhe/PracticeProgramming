string = "abcd"

r = "ab"
if string[:len(r)] == r:
    string = string[len(r):]

print(string)