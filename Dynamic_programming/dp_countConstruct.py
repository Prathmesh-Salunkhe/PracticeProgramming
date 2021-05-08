def countConstruct(target,words):
    if target == '':
        return 1
    if len(target) < len(min(words)):
        return 0

    ways = 0
    for w in words:
        if target[:len(w)] == w:
            rem = target[len(w):]
            ways += countConstruct(rem,words)

    return ways

#print(countConstruct('purple',['purp','p','ur','le','purle']))
#print(countConstruct('abcdef',['ab','abc','cd','def','abcd']))
#print(countConstruct('purple',['purp','p','ur','le','purle']))
#print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef',['e','eee','ee','eeee','eeeee']))

def countConstruct_dp(target,words,memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    if len(target) < len(min(words)):
        return 0

    ways = 0
    for w in words:
        if target[:len(w)] == w:
            rem = target[len(w):]
            ways += countConstruct_dp(rem,words,memo)

    memo[target] = ways
    return ways

print(countConstruct_dp('eeeeeeeeeeeeeeeeeeeeeeeeeef',['e','eee','ee','eeee','eeeee']))
