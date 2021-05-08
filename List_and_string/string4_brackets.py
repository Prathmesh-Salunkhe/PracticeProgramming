str = input()
counter = -1
stack =[]

for ch in str:
    if ch =='{' or ch == '[' or ch == '(' :
        stack.append(ch)
        counter +=1
        print('in',stack)
        continue

    if counter == 0 and (ch == '}' or ch == ']' or ch == ')'):
        print(counter+1)
        break

    a = stack.pop()
    #print(stack)
    if a == '{' and ch == '}':
        counter -=1

    elif a == '[' and ch == ']':
        counter -=1

    elif a == '(' and ch == ')':
        counter -= 1

    else:
        print(counter+1)
        break
    print('out',stack)

if len(stack) == 0:
    print(0)

else:
    print(counter+1)

