def recursiveRemove(string1, string2):
    if string2 in string1:
        string1 = removestring(string1, string2)        #alternative: str.rfind(sub)
    else:
        return len(string1)
    return recursiveRemove(string1, string2)


def removestring(string1, string2):         #alternative: string.rfind(substring) return the start index of substring in string
    i = 0
    j = 0
    first = True

    while i < len(string1):
        if string1[i] == string2[j]:
            if first:
                start = i
                first = False

            if j >= len(string2)-1:
                end = i
                break
            i += 1
            j += 1

        elif string1[i]!= string2[j] and string1[i] != string2[0]:
            i += 1
            first = True
            j = 0

        else:
            j=0
            first = True

    str1 = string1[:start] + string1[end+1:]

    return str1

if __name__ == '__main__':
    string1 = input()
    string2 = input()
    #print(removestring(string1,string2))
    print(recursiveRemove(string1, string2))




# sample input
# xxyzyzyv
# xyz
#output = 2


# removestring
# aceab
# ab
#
# i = 0
# j = 0
# i = 1
# j = 1
# i =2
# j =0
# i =3
# j =0
# i =4
# j =1
