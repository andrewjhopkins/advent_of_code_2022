import sys

class Node:
    def __init__(self, name, flowRate, valveConnectionsList):
        self.name = name
        self.flowRate = flowRate
        self.connections = valveConnectionsList 

def main():
    if len(sys.argv) < 2:
        print("Usage py part_1.py input.txt")
        return
    
    lines = getInput(sys.argv[1])

    nodes = {}

    valvesWithFlow = 0

    for line in lines:
        valveName = line[6:8]
        flowRate = int(line[line.find("=") + 1: line.find(";")])

        if flowRate > 0:
            valvesWithFlow += 1

        valveConnectionsIndex = line.find("valve", line.find("tunnels"))
        valveConnectionsList = []

        if (line[valveConnectionsIndex + 5] == "s"):
            valveConnections = line[line.find("valves ") + 7:]
            valveConnectionsList = valveConnections.split(", ")
        else:
            valveConnection = line[line.find("valve ") + 6:]
            valveConnectionsList = [valveConnection]

        newNode = Node(valveName, flowRate, valveConnectionsList)
        nodes[valveName] = newNode

    opened = set()
    cache = {}

    output = runSim("AA", nodes, 30, 0, opened, [], valvesWithFlow, cache, False)
    print(output[0])


def runSim(currentNode, nodes, minutes, currentRate, opened, prev, valvesWithFlow, cache, openValve):
    if (currentNode, minutes, tuple(opened), openValve) in cache:
        return cache[(currentNode, minutes, tuple(opened), openValve)]

    if minutes <= 0 or len(opened) >= valvesWithFlow:
        return (currentRate, prev)

    node = nodes[currentNode]

    if openValve and node.flowRate > 0 and currentNode not in opened:
        minutes -= 1
        currentRate += (minutes * node.flowRate)
        opened.add(currentNode)

    maxOutput = currentRate
    maxPrev = prev

    for nextNode in node.connections:
        newPrev = prev + [currentNode, currentRate]

        output1 = runSim(nextNode, nodes, minutes - 1, currentRate, opened.copy(), newPrev, valvesWithFlow, cache, True)
        output2 = runSim(nextNode, nodes, minutes - 1, currentRate, opened.copy(), newPrev, valvesWithFlow, cache, False)

        maxOfTwo = output2 if output2[0] > output1[0] else output1

        if maxOfTwo[0] > maxOutput:
            maxOutput = maxOfTwo[0]
            maxPrev = maxOfTwo[1]

    cache[(currentNode, minutes, tuple(opened), openValve)] = (maxOutput, maxPrev)

    return (maxOutput, maxPrev)


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
