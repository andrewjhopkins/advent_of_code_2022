import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part_1.py input.txt")
        return

    lines = getInput(sys.argv[1])
    coordinates = []
    coordSet = set()

    for line in lines:
        line = line.split(",")
        x, y, z, = int(line[0]), int(line[1]), int(line[2])
        coordinates.append([x, y, z])
        coordSet.add((x, y, z))

    output = 0

    for c in coordinates:
        exposedSides = 6
        coordsToFind = [(c[0] - 1, c[1], c[2]), (c[0] + 1, c[1], c[2]), (c[0], c[1] - 1, c[2]), (c[0], c[1] + 1, c[2]), (c[0], c[1], c[2] - 1), (c[0], c[1], c[2] + 1)]

        for cf in coordsToFind:
            if cf in coordSet:
                exposedSides -= 1
        output += exposedSides

    print(output)

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
