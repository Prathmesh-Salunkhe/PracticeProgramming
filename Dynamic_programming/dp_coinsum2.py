def coinsum(sum,coin):
    if sum == 0:
        return []
    if sum<0:
        return None

    shortest_path = None

    for c in coin:
        reminder = sum - c
        path = coinsum(reminder,coin)

        if path is not None:
            newpath = path + [c]
            if shortest_path is not None:
                if len(newpath) < len(shortest_path):
                    shortest_path = newpath
            else:
                shortest_path = newpath

    return shortest_path


#print(coinsum(7,[5,3,4,7]))

def coinsum_dp(sum,coin,memo={}):
    if sum in memo:
        return memo[sum]
    if sum == 0:
        return []
    if sum<0:
        return None

    shortest_path = None

    for c in coin:
        reminder = sum - c
        path = coinsum_dp(reminder,coin,memo)

        if path is not None:
            newpath = path + [c]
            if shortest_path is not None:
                if len(newpath) < len(shortest_path):
                    shortest_path = newpath
            else:
                shortest_path = newpath

    memo[sum] = shortest_path
    return shortest_path


print(coinsum_dp(100,[4,1,5,25]))
