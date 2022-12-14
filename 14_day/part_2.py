import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part_2.py input.txt")
        return
    
    lines = getInput(sys.argv[1])

    lowestX = float("inf")
    highestX = float("-inf")

    lowestY = 0
    highestY = float("-inf")

    rockPoints = []

    for line in lines:
        rockPoint = []
        points = line.split(" -> " )

        for point in points:
            pointSplit = point.split(",")
            xPoint = int(pointSplit[0])
            yPoint = int(pointSplit[1])

            rockPoint.append([xPoint, yPoint])

            lowestX = min(xPoint, lowestX)
            highestX = max(xPoint, highestX)

            lowestY = min(yPoint, lowestY)
            highestY = max(yPoint, highestY)

        rockPoints.append(rockPoint)

    highestY += 2

    additionalWidth = 1
    for i in range(1, highestY + 2):
        additionalWidth += 2

    centerWidth = additionalWidth // 2
    correctionX = 500 - centerWidth

    grid = [["." for i in range(0, additionalWidth + 1)] for j in range(lowestY, highestY + 1)]

    for i in range(len(grid[lowestY])):
        grid[highestY][i] = "#"

    for rockPoint in rockPoints:
        for i in range(len(rockPoint)):
            if i + 1 >= len(rockPoint):
                break
            
            xp1 = rockPoint[i][0]
            yp1 = rockPoint[i][1]

            xp2 = rockPoint[i + 1][0]
            yp2 = rockPoint[i + 1][1]

            if xp1 == xp2:
                for j in range(min(yp1, yp2), max(yp1, yp2) + 1):
                    grid[j][xp1 - correctionX] = "#"
            else:
                for j in range(min(xp1, xp2), max(xp1, xp2) + 1):
                    grid[yp1][j - correctionX] = "#"


    counter = 0

    while True:
        counter += 1
        sandX = 500 - correctionX 
        sandY = 0

        while True:
            if grid[sandY + 1][sandX] == ".":
                sandY += 1
            elif grid[sandY + 1][sandX - 1] == ".":
                sandX -= 1
                sandY += 1
            elif grid[sandY + 1][sandX + 1] == ".":
                sandX += 1
                sandY += 1
            else:
                grid[sandY][sandX] = "o"
                if sandY == 0 and sandX == 500 - correctionX:
                    print(counter)
                    return
                break

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
 
