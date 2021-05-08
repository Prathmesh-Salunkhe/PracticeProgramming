def LCS(string1, string2, n, m):
    if n < 0 or m < 0:
        return 0
    count = 0
    if string1[n] == string2[m]:
        count += 1 + LCS(string1, string2, n - 1, m - 1)
    else:
        count += max(LCS(string1, string2, n - 1, m), LCS(string1, string2, n, m - 1))

    return count


if __name__ == '__main__':
    string1 = input()
    string2 = input()
    print(LCS(string1, string2, len(string1) - 1, len(string2) - 1))
