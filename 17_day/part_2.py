import sys

class LineShape:
    def updateCoordinates(self, row, col):
        self.topRow = row
        self.bottomRow = self.topRow
        self.leftCol = col
        self.rightCol = self.leftCol + 3

    def printCoordinates(self):
        return [[self.topRow, self.leftCol], [self.topRow, self.leftCol + 1], [self.topRow, self.leftCol + 2], [self.topRow, self.leftCol + 3]]

class PlusShape:
    def updateCoordinates(self, row, col):
        self.topRow = row
        self.bottomRow = self.topRow + 2

        self.leftCol = col
        self.rightCol = self.leftCol + 2

    def printCoordinates(self):
        return [[self.topRow, self.leftCol + 1], [self.topRow + 1, self.leftCol], [self.topRow + 1, self.leftCol + 1], [self.topRow + 1, self.leftCol + 2], [self.topRow + 2, self.leftCol + 1]] 

class LShape:
    def updateCoordinates(self, row, col):
        self.topRow = row
        self.bottomRow = self.topRow + 2

        self.leftCol = col
        self.rightCol = self.leftCol + 2

    def printCoordinates(self):
        return [[self.topRow, self.leftCol + 2], [self.topRow + 1, self.leftCol + 2], [self.topRow + 2, self.leftCol], [self.topRow + 2, self.leftCol + 1], [self.topRow + 2, self.leftCol + 2]]

class VertLineShape:
    def updateCoordinates(self, row, col):
        self.topRow = row
        self.bottomRow = self.topRow + 3

        self.leftCol = col
        self.rightCol = self.leftCol

    def printCoordinates(self):
        return [[self.topRow, self.leftCol], [self.topRow + 1, self.leftCol], [self.topRow + 2, self.leftCol], [self.topRow + 3, self.leftCol]]

class SquareShape:
    def updateCoordinates(self, row, col):
        self.topRow = row
        self.bottomRow = self.topRow + 1

        self.leftCol = col
        self.rightCol = self.leftCol + 1

    def printCoordinates(self):
        return [[self.topRow, self.leftCol], [self.topRow, self.leftCol + 1], [self.topRow + 1, self.leftCol], [self.topRow + 1, self.leftCol + 1]]

def main():
    if len(sys.argv) < 2:
        print("Usage py part_1.py input.txt")
        return

    lines = getInput(sys.argv[1])
    jetPattern = []
    for line in lines:
        jetPattern = list(line)

    grid = [["." for j in range(7)] for i in range(4)]
    shapeRotation = [LineShape(), PlusShape(), LShape(), VertLineShape(), SquareShape()]

    matchIndex = None
    beforeNum = None
    found = set()

    firstNumHeight = None

    highestRow = len(grid)
    jetPatternCounter = 0

    heights = {}

    for rockNum in range(0, 1000000000000):
        rockType = shapeRotation[rockNum % len(shapeRotation)]
        rockType.updateCoordinates(0, 2)

        if isinstance(rockType, LineShape):
            jetPatternIndex = jetPatternCounter % len(jetPattern)

            if matchIndex is not None and jetPatternIndex == matchIndex:
                rocksRemaining = 1000000000000 - beforeNum
                rockDifference = rockNum - beforeNum

                rockHeight = len(grid) - highestRow

                # height per rockDifference
                patternHeight = rockHeight - firstNumHeight

                patterns = rocksRemaining // rockDifference
                patternsRemaining = rocksRemaining % rockDifference

                total = patternHeight * patterns

                if patternsRemaining != 0:
                    total += heights[beforeNum + patternsRemaining - 1] - heights[beforeNum]

                print(total + firstNumHeight)
                return

            elif matchIndex is None and jetPatternIndex in found:

                firstNumHeight = (len(grid) - highestRow) 

                beforeNum = rockNum
                matchIndex = jetPatternIndex
            else:
                found.add(jetPatternIndex)

        # Add height buffer
        while highestRow - rockType.bottomRow < 4:
            gridRow = ["." for j in range(7)]
            grid = [gridRow] + grid
            highestRow += 1

        while highestRow - rockType.bottomRow > 4:
            grid.pop(0)
            highestRow -= 1

        while True:
            coordinates = rockType.printCoordinates()

            # drawShape in starting position
            for coord in coordinates:
                grid[coord[0]][coord[1]] = "@"

            # Find out the jet pattern and update new coordinates
            jetDirection = jetPattern[jetPatternCounter % len(jetPattern)]
            jetPatternCounter += 1

            originalTopRow = rockType.topRow
            originalLeftCol = rockType.leftCol

            if jetDirection == ">":
                rockType.updateCoordinates(rockType.topRow, rockType.leftCol + 1)
            else:
                rockType.updateCoordinates(rockType.topRow, rockType.leftCol - 1)

            # Check if possible? 
            newSideCoordinates = rockType.printCoordinates()

            canMoveSide = True
            for coord in newSideCoordinates:
                if coord[1] < 0 or coord[1] >= len(grid[0]) or grid[coord[0]][coord[1]] == "#":
                    canMoveSide = False
                    break
            
            # Redraw if so, leave alone if not
            if canMoveSide:
                for coord in coordinates:
                    grid[coord[0]][coord[1]] = "."
                for coord in newSideCoordinates:
                    grid[coord[0]][coord[1]] = "@"
            else:
                rockType.updateCoordinates(originalTopRow, originalLeftCol)

            coordinates = rockType.printCoordinates()

            originalTopRow = rockType.topRow
            originalLeftCol = rockType.leftCol

            rockType.updateCoordinates(rockType.topRow + 1, rockType.leftCol)
            newDownCoordinates = rockType.printCoordinates()

            # Check if possible to move down
            canMoveDown = True

            for coord in newDownCoordinates:
                if coord[0] >= len(grid) or grid[coord[0]][coord[1]] == "#":
                    canMoveDown = False
                    break

            if canMoveDown:
                for coord in coordinates:
                    grid[coord[0]][coord[1]] = "."
                for coord in newDownCoordinates:
                    grid[coord[0]][coord[1]] = "@"

            else:
                rockType.updateCoordinates(originalTopRow, originalLeftCol)
                coordinates = rockType.printCoordinates()

                for coord in coordinates:
                    highestRow = min(coord[0], highestRow)
                    grid[coord[0]][coord[1]] = "#"

                heights[rockNum] = len(grid) - highestRow
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
