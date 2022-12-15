import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part_2.py input.txt")
        return
    
    lines = getInput(sys.argv[1])

    sensors = []
    beacons = set()

    radiuses = []

    minimum = 0
    maximum = 4000000

    if sys.argv[1].find("test") != -1:
        minimum = 0
        maximum = 20

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


    for targetRow in range(minimum, maximum + 1):

        intervals = []

        for i in range(len(sensors)):

            diff = abs(targetRow - sensors[i][0])
            if diff <= radiuses[i]:

                intervals.append([sensors[i][1] - (radiuses[i] - diff), sensors[i][1] + (radiuses[i] - diff)])

        intervals.sort()

        intervalIndex = 1

        while intervalIndex < len(intervals):
            if intervals[intervalIndex][0] <= intervals[intervalIndex - 1][1]:
                intervals[intervalIndex - 1][1] = max(intervals[intervalIndex - 1][1], intervals[intervalIndex][1])
                intervals.pop(intervalIndex)
            else:
                intervalIndex += 1

        targetCol = minimum

        while targetCol <= maximum:
            for interval in intervals:
                if interval[0] <= targetCol:
                    targetCol = interval[1] + 1
                    interval.pop(0)
                    continue

            if targetCol <= maximum:
                print((targetCol * 4000000) + targetRow)
                return


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
