import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part_1.py input.txt")
        return
    
    lines = getInput(sys.argv[1])

    smallestX = float("inf")
    smallestY = float("inf")

    largestX = float("-inf")
    largestY = float("-inf")

    sensors = []
    beacons = []

    for line in lines:
        sensorX = int(line[line.find("x=") + 2 : line.find(",")])
        sensorY = int(line[line.find("y=") + 2 : line.find(":")])

        sensors.append([sensorY, sensorX])

        smallestX = min(smallestX, sensorX)
        smallestY = min(smallestY, sensorY)

        largestX = max(largestX, sensorX)
        largestY = max(largestY, sensorY)

        beaconX = int(line[line.find("x=", line.find("beacon")) + 2 : line.find(",", line.find("beacon"))])
        beaconY = int(line[line.find("y=", line.find("beacon")) + 2 :])

        beacons.append([beaconY, beaconX])

        smallestX = min(smallestX, beaconX)
        smallestY = min(smallestY, beaconY)

        largestX = max(largestX, beaconX)
        largestY = max(largestY, beaconY)


    grid = [["." for i in range(smallestX, largestX + 1)] for j in range(smallestY, largestY + 1)]

    for sensor in sensors:
        sensor[0] -= smallestY
        sensor[1] -= smallestX

    for beacon in beacons:
        beacon[0] -= smallestY
        beacon[1] -= smallestX

    for i in range(len(sensors)):
        manhattanDistance(sensors[i][0], sensors[i][1], beacons[i][0], beacons[i][1], grid)

    for i in range(len(sensors)):
        grid[sensors[i][0]][sensors[i][1]] = "S"
        grid[beacons[i][0]][beacons[i][1]] = "B"

    print(grid[10 - smallestY])

    output = 0

    for i in range(len(grid[0])):
        if grid[2000000 - smallestY][i] == "#":
            output += 1

    print(output)


def manhattanDistance(sensorY, sensorX, beaconY, beaconX, grid):
    yDiff = abs(beaconY - sensorY)
    xDiff = abs(beaconX - sensorX)

    arcSize = yDiff + xDiff

    for arcSize in range(yDiff + xDiff, -1, -1):

        yCoord = (yDiff + xDiff) - arcSize

        for j in range(arcSize + 1):

            if sensorY - yCoord >= 0:
                if sensorX - arcSize >= 0:
                    grid[sensorY - yCoord][sensorX - j] = "#"
                if sensorX + arcSize < len(grid[0]):
                    grid[sensorY - yCoord][sensorX + j] = "#"

            if sensorY + yCoord < len(grid):
                if sensorX - arcSize >= 0:
                    grid[sensorY + yCoord][sensorX - j] = "#"
                if sensorX + arcSize < len(grid[0]):
                    grid[sensorY + yCoord][sensorX + j] = "#"


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
