def allConstruct(target, words):
    if target == '':
        return [[]]
    if len(target) < len(min(words)):
        None
    combo = []
    for w in words:
        if target[:len(w)] == w:
            rem = target[len(w):]
            ways = allConstruct(rem, words)
            if ways is not None:
                for i in range(len(ways)):
                    ways[i] = ways[i] + [w]
                combo = ways + combo

    return combo


result = allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purle'])
print(result)

for ele in result:
    ele.reverse()

print(result)

def allConstruct_dp(target, words,memo = {}):
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    if len(target) < len(min(words)):
        None
    combo = []
    for w in words:
        if target[:len(w)] == w:
            rem = target[len(w):]
            ways = allConstruct_dp(rem, words,memo)
            if ways is not None:
                for i in range(len(ways)):
                    ways[i] = ways[i] + [w]
                combo = ways + combo

    memo[target] = combo
    return combo


result = allConstruct_dp('purple', ['purp', 'p', 'ur', 'le', 'purle'])
print(result)