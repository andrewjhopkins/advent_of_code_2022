import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part_2.py input.txt")
        return
    
    lines = getInput(sys.argv[1])
    lines.append([[2]])
    lines.append([[6]])
    lines = bubbleSort(lines)

    print((lines.index([[2]]) + 1) * (lines.index([[6]]) + 1))

# better ways to do this but its a weekday
def bubbleSort(lines):
    run = True
    while(run):
        run = False
        for i in range(len(lines) - 1):
            if compare(lines[i], lines[i + 1]) == -1:
                lines[i], lines[i + 1] = lines[i + 1], lines[i]
                run = True

    return lines

def compare(left, right):
    for i in range(len(left)):
        if i >= len(right):
            return -1 

        if type(left[i]) is int and type(right[i]) is int:
            if right[i] < left[i]:
                return -1 

            elif right[i] > left[i]:
                return 1 

        elif type(left[i]) is int and type(right[i]) is not int:
             ordered = compare([left[i]], right[i])
             if ordered != 0:
                 return ordered

        elif type(left[i]) is not int and type(right[i]) is int:
            ordered = compare(left[i], [right[i]])
            if ordered != 0:
                return ordered

        else:
            ordered = compare(left[i], right[i])
            if ordered != 0:
                return ordered

    if len(left) == len(right):
        return 0

    return 1

def getInput(fileName): 
    lines = []
    with open(fileName) as file: 
        fileLines = file.readlines()
        for line in fileLines: 
            if len(line.strip()) != 0:
                lines.append(eval(line.strip()))

    return lines


if __name__ == "__main__":
    main()
