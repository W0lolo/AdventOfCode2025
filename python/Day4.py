import numpy as np

def day4part1solver(path):
    total = 0
    with open(path, "r") as file:

        offsets = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        window = [[],"."+ file.readline().strip() +".",[]]
        window[0] = "." * len(window[1]) #buffer to avoid having bounds checking
        # moving window of 3 lines

        def process():
            # counts the number of rolls with less than 4 adjacent rolls in window[1]
            nonlocal total
            nonlocal window

            for i in range(1,len(window[2])-1):
                if window[1][i] == '@':
                    rolls = 0
                    for off in offsets:
                        if window[off[0] +1][off[1]+i] == '@':
                            rolls += 1
                    if rolls<4:
                        total += 1
                        print('X', end=' ')
                    else:
                        print('@',end=' ')
                else:
                    print('.',end=' ')

        for line in file:
            window[2] = "." + line.strip() + "."

            print("")
            process()
            # moving down window
            window[0] = window[1]
            window[1] = window[2]

        # last line
        window[2] = "."*len(window[1])
        print("")
        process()

    return total

def day4part2solver(path):
    total = 0
    with open(path, "r") as file:
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        inp = file.read().split('\n')
        inp = ["."+line+"." for line in inp]
        padding = "."*len(inp[0])
        inp = [padding] + inp + [padding]

        def count_neighbours(x:int,y:int) -> int:
            """
            :param x: column index
            :param y: row index
            :return: returns the number of rolls neighbouring x,y, assumes padding
            """
            nonlocal offsets
            nonlocal inp
            total = 0
            for off in offsets:
                if inp[y+off[0]][x+off[1]] == '@':
                    total+=1
            return total




        # convert inp into numpy array where . has value 0
        # and @ are represented by an int that is their number of neighbours, + buffer of 0s
        pile = np.zeros((len(inp),len(inp[0])))
        rows, cols = pile.shape
        for y in range(1,rows-1):
            for x in range(1,cols-1):
                if inp[y][x] == '@':
                    pile[y,x] = count_neighbours(x,y) + 1

        def remove_roll(x:int,y:int) -> None:
            """
            Decrements the neighbour count of neighbouring rolls
            :param x: col index
            :param y: row index
            :return: None
            """
            nonlocal pile

            pile[x, y] = 0
            for off in offsets:
                if pile[x+off[0],y+off[1]] > 0:
                    pile[x+off[0],y+off[1]] -= 1
            return

    found = True
    while found:
        found = False
        for y in range(1,rows-1):
            for x in range(1,cols-1):
                if 0 < pile[x,y] < 5:
                    found = True
                    remove_roll(x,y)
                    total += 1


    return total


print(day4part2solver("../Input/Day4.txt"))