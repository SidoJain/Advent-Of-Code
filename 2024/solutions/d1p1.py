def readFile(filename: str, firstList: list[int], secondList: list[int]) -> None:
    with open(filename) as file:
        for line in file:
            [first, *_, second] = line.split(' ')
            firstList.append(int(first))
            secondList.append(int(second))

def getDist(firstList: list[int], secondList: list[int]) -> int:
    firstList.sort()
    secondList.sort()
    dist = 0

    while (len(firstList) > 0):
        first = firstList.pop(0)
        second = secondList.pop(0)
        dist += abs(first - second)
    return dist

firstList = []
secondList = []
readFile('../inputs/input1.txt', firstList, secondList)
print(getDist(firstList, secondList))