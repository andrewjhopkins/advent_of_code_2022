import sys
from functools import cache

class Node:
    def __init__(self, name, flowRate, valveConnectionsList):
        self.name = name
        self.flowRate = flowRate
        self.connections = valveConnectionsList 

nodes = {}
def main():
    if len(sys.argv) < 2:
        print("Usage py part_1.py input.txt")
        return
    
    lines = getInput(sys.argv[1])

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

    output = runSim("AA", 30, tuple([]))
    print(output)


@cache
def runSim(currentNode, minutes, visited):
    if minutes <= 1:
        return 0
    
    rate = 0
    node = nodes[currentNode]
    for connectorNode in node.connections:
        rate = max(rate, runSim(connectorNode, minutes - 1, visited))

    if currentNode not in visited and node.flowRate > 0:
        visited = tuple(sorted([*visited, currentNode]))
        rate = max(rate, runSim(currentNode, minutes - 1, visited) + node.flowRate * (minutes - 1))

    return rate

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
