def canConstruct(target,words):
    if target == '':
        return True

    for w in words:
        if target[:len(w)] == w:
            rem = target[len(w):]
            if canConstruct(rem,words) == True:
                return True

    return False

print(canConstruct('happy',['h','a','y','ha','y']))
#print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeef',['e',"ee","eee","eeee"]))


def canConstruct_dp(target,words,memo = {}):
    if target in memo:
        return memo[target]
    if target == '':
        return True

    for w in words:
        if target[:len(w)] == w:
            rem = target[len(w):]
            if canConstruct_dp(rem,words,memo) == True:
                memo[target] = True
                return True

    memo[target] = False
    return False

print(canConstruct_dp('eeeeeeeeeeeeeeeeeeeeeeeeef',['e',"ee","eee","eeee"]))
