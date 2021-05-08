def check(blocks):
    for i in range(len(blocks)):
        if blocks[i] < len(blocks[i+1:]):
            return False

    return True


def blocksheight(strength):
    strength.sort()
    strength.reverse()
    blocks = []
    for s in strength:
        blocks.append(s)
        if check(blocks) is False:
            return len(blocks) - 1

    return len(blocks)

if __name__ == '__main__':
    n = int(input())
    strength = []
    for i in range(n):
        s = int(input())
        strength.append(s)


    print(blocksheight(strength))