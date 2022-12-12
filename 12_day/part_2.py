import sys
import heapq

def main():
    if len(sys.argv) < 2:
        print("Usage py part_2.py input.txt")
        return
    
    lines = getInput(sys.argv[1])

    output = float("inf")

    start = None
    end = None

    grid = []

    rowCount = 0

    for line in lines:
        listLine = list(line)

        if 'E' in listLine:
            end = (rowCount, listLine.index('E'))

        grid.append(listLine)
        rowCount += 1

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'a':
                seen = [[False for i in grid[0]] for j in grid]
                distance = [[float("inf") for i in grid[0]] for j in grid]

                shortest = dijkstras(grid, seen, distance, (i, j), end)
                output = min(shortest, output)

    print(output)

def dijkstras(grid, seen, distance, start, end):
    queue = []
    heapq.heappush(queue, (0, start))

    distance[start[0]][start[1]] = 0

    while (len(queue)):
        current = heapq.heappop(queue)

        cDistance = current[0]
        cRow = current[1][0]
        cCol = current[1][1]

        if seen[cRow][cCol]:
            continue
        seen[cRow][cCol] = True

        if current[1] == end:
            return cDistance

        neighbors = [(cRow + 1, cCol), (cRow - 1, cCol), (cRow, cCol + 1), (cRow, cCol - 1)]

        cAscii = getAsciiValue(grid[cRow][cCol])

        for neighbor in neighbors:
            nRow = neighbor[0]
            nCol = neighbor[1]

            if nRow < 0 or nRow >= len(grid) or nCol < 0 or nCol >= len(grid[0]):
                continue
            
            nAscii = getAsciiValue(grid[nRow][nCol])

            if (nAscii - cAscii <= 1 and (cDistance + 1 < distance[nRow][nCol])):
                distance[nRow][nCol] = cDistance + 1
                heapq.heappush(queue, (cDistance + 1, (nRow, nCol)))

    return float("inf")


def getAsciiValue(c):
    if c == 'S':
        return ord('a')
    if c == 'E':
        return ord('z')

    return ord(c)

def getInput(fileName): 
    lines = []
    with open(fileName) as file: 
        fileLines = file.readlines()
        for line in fileLines: 
            lines.append(line.strip())

    return lines


if __name__ == "__main__":
    main()
