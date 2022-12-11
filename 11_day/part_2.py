import sys
import math

class Monkey:
    def __init__(self):
        self.items = []
        self.inspected = 0
        self.operationType = ""
        self.operationMag = ""
        self.divisible = 0
        self.divisibleTrue= 0
        self.divisibleFalse = 0

def main():
    if len(sys.argv) < 2:
        print("Usage py part_1.py input.txt")
        return
    
    lines = getInput(sys.argv[1])
    monkeys = parseLinesForMonkeys(lines)

    lcm = math.lcm(*[monkey.divisible for monkey in monkeys])

    for i in range(10000):
        for monkey in monkeys:
            while(len(monkey.items)):
                item = monkey.items.pop(0)
                monkey.inspected += 1;
                operationMag = monkey.operationMag if monkey.operationMag != "old" else item

                operation = monkey.operationType
                if operation == "+":
                    item = item + operationMag
                else:
                    item = item * operationMag
                
                item = item % lcm

                throwDecision = item % monkey.divisible == 0
                if throwDecision:
                    recieveMonkey = monkeys[monkey.divisibleTrue]
                    recieveMonkey.items.append(item)
                else:
                    recieveMonkey = monkeys[monkey.divisibleFalse]
                    recieveMonkey.items.append(item)

    inspected = []
    for monkey in monkeys:
        inspected.append(monkey.inspected)

    inspected.sort()

    print(inspected[-1], inspected[-2])
    print(inspected[-1] * inspected[-2])


def parseLinesForMonkeys(lines):
    monkeys = []
    i = 0
    while i < len(lines):
        if (lines[i][0:6] == "Monkey"):
            newMonkey = Monkey()

            startingItemsLine = lines[i + 1][16:]
            startingItems = startingItemsLine.split(", ")

            for item in startingItems:
                newMonkey.items.append(int(item))

            operation = lines[i + 2][21:22]

            newMonkey.operationType = lines[i + 2][21:22]


            newMonkey.operationMag = lines[i + 2][23:]

            if newMonkey.operationMag != "old":
                newMonkey.operationMag = int(newMonkey.operationMag)

            divisible = lines[i + 3][19:]
            newMonkey.divisible = int(divisible)

            divisibleTrue = lines[i + 4][25:]
            newMonkey.divisibleTrue = int(divisibleTrue)

            divisibleFalse = lines[i + 5][26:]
            newMonkey.divisibleFalse = int(divisibleFalse)

            monkeys.append(newMonkey)
            i += 6
        else:
            i += 1

    return monkeys



def getInput(fileName): 
    lines = []
    with open(fileName) as file: 
        fileLines = file.readlines()
        for line in fileLines: 
            lines.append(line.strip())

    return lines


if __name__ == "__main__":
    main()
