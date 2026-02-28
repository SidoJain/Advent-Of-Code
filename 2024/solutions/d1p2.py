def readFile(filename: str, firstList: list[int], secondList: list[int]) -> None:
    with open(filename) as file:
        for line in file:
            [first, *_, second] = line.split(' ')
            firstList.append(int(first))
            secondList.append(int(second))

def getCount(firstList: list[int], secondList: list[int]) -> int:
    firstList.sort()
    secondList.sort()
    count = 0

    while (len(firstList) > 0):
        first = firstList.pop(0)
        second = secondList.count(first)
        count += first * second
    return count

firstList = []
secondList = []
readFile('../inputs/input1.txt', firstList, secondList)
print(getCount(firstList, secondList))