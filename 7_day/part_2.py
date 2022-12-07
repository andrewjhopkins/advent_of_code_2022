import sys

def main():
    if len(sys.argv) < 2:
        print("Usage py part_1.py input.txt")
        return
    
    lines = getInput(sys.argv[1])

    root = Node("/")
    root.parent = "/"
    root.fileType = "dir"
    
    currentNode = root

    for line in lines[1:]:
        if line[0] == '$':
            if line[2] == 'c':
                nextDirectory = line[line.find("cd ") + 3:].strip()
                if nextDirectory == "..":
                    currentNode = currentNode.parent
                else:
                    currentNode = currentNode.children[nextDirectory]

        else:
            if line[0] == 'd':
                directoryName = line[4:]
                newNode = Node(directoryName)
                newNode.parent = currentNode
                newNode.type = "dir"

                currentNode.children[newNode.name] = newNode
                
            else:
                fileSize = line[0:line.find(" ")]
                fileName = line[line.find(" ") + 1:]

                newNode = Node(fileName)
                newNode.parent = currentNode
                newNode.type = "file"
                newNode.size = int(fileSize)

                currentNode.children[newNode.name] = newNode

    sizes = []
    rootSize = traverseTree(root, sizes)

    spaceNeeded = 30000000 - (70000000 - rootSize)
    sizes.sort()

    for size in sizes:
        if size >= spaceNeeded:
            print(size)
            return


def traverseTree(root, sizes):
    output = 0
    for name, childNode in root.children.items():
        if childNode.type == "file":
            output += childNode.size
        else:
            dirSize = traverseTree(childNode, sizes)
            childNode.size = dirSize
            sizes.append(childNode.size)
            output += childNode.size

    return output


def getInput(fileName): 
    lines = []
    with open(fileName) as file: 
        fileLines = file.readlines()
        for line in fileLines: 
            lines.append(line.strip())

    return lines

class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = {}
        self.fileType = ""
        self.size = 0


if __name__ == "__main__":
    main()
