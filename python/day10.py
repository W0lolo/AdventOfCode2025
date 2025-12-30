import re
import numpy as np

def day10part1solver(path):
    # need total least amount of button presses to switch on all machines
    total = 0
    with open(path,"r") as file:
        inp = file.readlines()

    def pressbuttons(machine):
        """
        :param index: the machine index (line no)
        :return: the number of buttons needing pressing
        """

        config = list(map( lambda x: 1 if x=='#' else 0 ,machine.partition('[')[2].partition(']')[0]))
        # 1 if the light needs to be on 0 otherwise


        buttons = list(map( lambda x: list(map(int,x.split(','))),re.findall(r'\(([^)]+)\)',machine)))
        small = 1000

        # constructing augmented matrix
        am = np.zeros((len(config),len(buttons)+1))
        rows, cols = np.shape(am)
        for c in range(0,len(buttons)):
            for i in buttons[c]:
                am[i,c] = 1

        for row in range(0,rows):
            am[row,cols-1] = config[row]

        # Gaussian elimination
        def add_row(dest,add):
            """
            :param dest: the index of the row to be added to
            :param add: the index of the row to be added
            :return:
            """
            nonlocal cols, am

            for i in range(0,cols):
                if am[add,i] == 1:
                    am[dest,i] = 1 if am[dest,i] == 0 else 0

        def add_row_to_nonzero(leading,add):
            """
            :param add: the row to add to all the other rows
            :param leading: the column of the leading one
            :return:
            """
            nonlocal rows,cols,am

            for r in range(0,add):
                if am[r,leading] == 1:
                    add_row(r,add)
            for r in range(add+1,rows):
                if am[r,leading] == 1:
                    add_row(r,add)

        # TODO handle rows where the leading 1 is not on the diagonal/check indexes
        for col in range(0,cols-1): # col of leading one
            for row in range(col,rows): # col of row with leading one
                if am[row,col]==1:
                    # switch rows
                    am[[col,row]]=am[[row,col]]
                    add_row_to_nonzero(col,col)
                    break

        # list of free vars
        free = [] # indexes of the free variables
        for i in range(0,min(cols-1,rows)):
            if am[i,i] == 0:
                free+=[i]

        if rows < cols-1:
            for i in range(rows,cols-1): # TODO find some way to count free vars where rows is the limiting factor
                free+=[i]

        def count_zs(settings):
            """
            :param settings: the setting of free variables
            :return: -1 if not solution
            """
            nonlocal free, am, cols, rows
            ans = [0]*(cols-1)

            # setting free variables
            for index in range(0, len(settings)):
                ans[free[index]] = settings[index]

            for diag in range(0, min(cols, rows)):
                if am[diag,diag] == 1: # not a free variable
                    ans[diag] = am[diag, cols - 1]

                    for ind in free:
                        if am[diag,ind] == 1 and ans[ind] == 1: # dependent on free var
                            ans[diag] = 1 if ans[diag] == 0 else 0 # flip


            return ans.count(1)



        # loop through settings of free vars
        for no in range(0,2**len(free)):
            setting = [1 if (no >> i) & 1 else 0  for i in range(0,len(free))]
            temp = count_zs(setting)
            if temp < small:
                small = temp




        print(am)
        print(f"free: {free}, smallest no of presses {small}")
        print(f"shape: rows: {rows} cols:{cols}")
        print()


        return small


    for line in inp:
        total += pressbuttons(line)
    return total


print(day10part1solver("../Input/Day10test.txt"))