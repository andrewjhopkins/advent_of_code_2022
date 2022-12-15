import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part_1.py input.txt")
        return
    
    lines = getInput(sys.argv[1])

    sensors = []
    beacons = []

    radiuses = []

    targetRow = 2000000

    for line in lines:
        sensorX = int(line[line.find("x=") + 2 : line.find(",")])
        sensorY = int(line[line.find("y=") + 2 : line.find(":")])
        sensors.append([sensorY, sensorX])

        beaconX = int(line[line.find("x=", line.find("beacon")) + 2 : line.find(",", line.find("beacon"))])
        beaconY = int(line[line.find("y=", line.find("beacon")) + 2 :])

        beacons.append([beaconY, beaconX])

        yDiff = abs(beaconY - sensorY)
        xDiff = abs(beaconX - sensorX)

        arcSize = yDiff + xDiff

        radiuses.append(arcSize)

    scannedCoords = set()
    for i in range(len(sensors)):
        diff = abs(targetRow - sensors[i][0])
        if diff <= radiuses[i]:
            for j in range(0, radiuses[i] - diff + 1):
                scannedCoords.add((targetRow, sensors[i][1] - j))
                scannedCoords.add((targetRow, sensors[i][1] + j))

    for beacon in beacons:
        if (beacon[0], beacon[1]) in scannedCoords:
            scannedCoords.remove((beacon[0], beacon[1]))

    print(len(scannedCoords))

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
