import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part_1.py input.txt")
        return
    
    lines = getInput(sys.argv[1])

    sensors = []
    beacons = set()

    radiuses = []

    targetRow = 2000000
    if sys.argv[1].find("test") != -1:
        targetRow = 10

    for line in lines:

        sensorX = int(line[line.find("x=") + 2:line.find(",")])
        sensorY = int(line[line.find("y=") + 2:line.find(":")])
        sensors.append([sensorY, sensorX])

        beaconX = int(line[line.find("x=", line.find("beacon")) + 2:line.find(",", line.find("beacon"))])
        beaconY = int(line[line.find("y=", line.find("beacon")) + 2:])

        beacons.add((beaconY, beaconX))

        yDiff = abs(beaconY - sensorY)
        xDiff = abs(beaconX - sensorX)

        arcSize = yDiff + xDiff

        radiuses.append(arcSize)

    intervals = []

    for i in range(len(sensors)):
        diff = abs(targetRow - sensors[i][0])
        if diff <= radiuses[i]:

            intervals.append([sensors[i][1] - (radiuses[i] - diff), sensors[i][1] + (radiuses[i] - diff)])

    intervals.sort()

    i = 1
    while i < len(intervals):
        if intervals[i][0] <= intervals[i - 1][1]:
            intervals[i - 1][1] = max(intervals[i - 1][1], intervals[i][1])
            intervals.pop(i)
        else:
            i += 1

    output = 1
    for interval in intervals:
        output += (interval[1] - interval[0])

    for beacon in beacons:
        if (beacon[0] == targetRow and beacon[1] >= interval[0] and beacon[1] <= interval[1]):
            output -= 1

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
