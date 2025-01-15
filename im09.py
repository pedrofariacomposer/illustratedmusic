
def loopRatio(loop=20, ratio=3):
    mainLoop = list(range(loop)) * ratio
    ratioList = [0]
    ratioList += ["x"] * (ratio - 1)
    i = 1
    resultLists = []
    used = []
    while len(ratioList) < len(mainLoop):
        ratioList.append(i)
        ratioList += ["x"] * (ratio - 1)
        i += 1

    print(ratioList)
    for el in range(loop):
        pair = mainLoop[ratioList.index(el)]
        if el not in used and pair not in used:
            newList = [el, pair] if el != pair else [el]
            resultLists.append(newList)
            used.append(el)
            used.append(pair)
        elif el not in used:
            newList = [x for x in resultLists if el in x or pair in x][0]
            if pair not in newList:
                newList.append(pair)
            used.append(el)
            used.append(pair)
    return resultLists


a = loopRatio(16, 4)
print(a)
