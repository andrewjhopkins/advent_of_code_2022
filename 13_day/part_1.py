import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part_1.py input.txt")
        return
    
    lines = getInput(sys.argv[1])

    output = 0

    index = 1
    l = 0

    while l < len(lines):
        left = eval(lines[l])
        right = eval(lines[l + 1])
        if compare(left, right) == 1:
            output += index
        l += 2
        index += 1

    print(output)

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
                lines.append(line.strip())

    return lines


if __name__ == "__main__":
    main()
