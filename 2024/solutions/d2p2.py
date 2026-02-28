def readFile(filename: str, splitList: list[list[int]]) -> None:
    with open(filename) as f:
        for line in f:
            splitLine = line.replace('\n', '').split(' ')
            splitList.append([int(x) for x in splitLine])

def isSorted(report: list[int]) -> bool:
    sorted = True
    for i in range(len(report) - 1):
        if report[i] > report[i + 1]:
            sorted = False
            break

    if sorted:
        return True
    else:
        sorted = True
    for i in range(len(report) - 1):
        if report[i] <= report[i + 1]:
            sorted = False
            break

    return sorted

def areSafe(splitList: list[list[int]]) -> int:
    count = 0
    for report in splitList:
        originalReport = report.copy()
        
        for i in range(-1, len(report)):
            report = originalReport.copy()
            if i >= 0:
                report.pop(i)
            if not isSorted(report):
                continue

            flag = True
            for i in range(len(report) - 1):
                if (abs(report[i] - report[i + 1]) > 3 or abs(report[i] - report[i + 1]) < 1):
                    flag = False
                    break
            if flag:
                count += 1
                break

    return count

splitList = []
readFile('../inputs/input2.txt', splitList)
print(areSafe(splitList))