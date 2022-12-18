import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part_1.py input.txt")
        return

    lines = getInput(sys.argv[1])
    coordinates = []

    minX = float("inf")
    minY = float("inf")
    minZ = float("inf")

    maxX = float("-inf")
    maxY = float("-inf")
    maxZ = float("-inf")

    for line in lines:
        line = line.split(",")
        x, y, z, = int(line[0]), int(line[1]), int(line[2])

        minX, minY, minZ = min(minX, x), min(minY, y), min(minZ, z)
        maxX, maxY, maxZ = max(maxX, x), max(maxY, y), max(maxZ, z)

        coordinates.append([x, y, z])

    output = 0

    cube = {}
    seen = {}

    for i in range(minX - 1, maxX + 2):
        for j in range(minY - 1, maxY + 2):
            for k in range(minZ - 1, maxZ + 2):
                cube[(i, j, k)] = "."
                seen[(i, j, k)] = False

    for coord in coordinates:
        cube[(coord[0], coord[1], coord[2])] = "x"

    start = (minX - 1, minY - 1, minZ - 1)

    output = floodFillNoRecursion(start, cube, seen)
    print(output)


def floodFillNoRecursion(start, cube, seen):
    output = 0
    queue = [start]

    while len(queue):
        position = queue.pop(0)

        if position not in seen or seen[position] == True:
            continue

        seen[position] = True

        x, y, z = position[0], position[1], position[2]

        neighbors = [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]
        goNext = []

        for n in neighbors:
            if n in cube:
                if cube[n] == "x":
                    output += 1
                else:
                    queue.append(n)

    return output


# recursion depth exceeds on input.txt
def floodFill(position, cube, seen):
    if position not in cube or seen[position] == True:
        return 0
    
    output = 0

    seen[position] = True

    x, y, z = position[0], position[1], position[2]

    neighbors = [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]
    goNext = []

    for n in neighbors:
        if n in cube:
            if cube[n] == "x":
                output += 1
            else:
                goNext.append(n)

    for g in goNext:
        output += floodFill(g, cube, seen)

    return output


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
