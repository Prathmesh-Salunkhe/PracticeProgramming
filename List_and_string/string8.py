string = input()
l = len(string)

start = 0
end = len(string) - 1
string = list(string)
while start < end :
    if string[start].isalpha() and string[end].isalpha():
        temp = string[start]
        string[start] = string[end]
        string[end] = temp
        start += 1
        end -=1

    elif string[start].isalpha() == False and string[end].isalpha() == False:
        start += 1
        end -= 1

    elif string[start].isalpha() == False:
        start += 1

    else:
        end -= 1

string = ''.join(string)
print(string)