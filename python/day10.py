import re
import numpy as np
from z3 import *

def day10part1solver(path):
    # does not find the minimal number of button presses

    total = 0
    with open(path,"r") as file:
        inp = file.readlines()

    def pressbuttons(machine):
        """
        :param machine: a line from the input representing a machine
        :return: the minimal no of button presses needed
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

        undiag = 0 # index of first row not checked to have a leading 0
        for col in range(0,cols-1):
            for row in range(undiag,rows):
                if am[row,col] == 1:
                    # switch rows
                    am[[undiag,row]] = am[[row,undiag]]
                    add_row_to_nonzero(col,undiag)
                    undiag+=1
                    break


        # list of free vars
        free = []  # indexes of the free variables

        col = 0 # column index
        diag = 0 # row we are trying to find leading 1 for
        while col<cols-1 and diag<rows:
            if am[diag,col]==1: # found leading 1
                diag+=1
            else: # found free var
                free+=[col]
            col+=1

        for i in range(col,cols-1):
            free += [i]

        def solve_vars(settings):
            """
            :param settings: setting of free variables
            :return: solution to augmented matrix
            """

            nonlocal free, am, cols, rows
            ans = [0] * (cols - 1)

            # setting free variables
            for index in range(0, len(settings)):
                ans[free[index]] = settings[index]

            leading = 0  # col of leading 1 (index of ans)
            for row in range(0,rows):
                while am[row,leading] == 0 and leading<cols-1: # finding col of leading 1
                    leading+=1

                if leading >= cols-1:
                    break

                ans[leading] = int(am[row,cols-1])

                for ind in free:
                    if am[row,ind] == 1 and ans[ind] == 1:
                        ans[leading] ^=1

            return ans

        matrix_sol =None
        best_sol=None
        # loop through settings of free vars
        for no in range(0,2**len(free)):
            setting = [1 if (no >> i) & 1 else 0  for i in range(0,len(free))]
            matrix_sol = solve_vars(setting)
            temp = matrix_sol.count(1)
            if temp < small:
                best_sol = matrix_sol
                small = temp


        # testing sol to get failing cases

        for i in range(0,len(best_sol)):
            if best_sol[i] ==1:
                for light in buttons[i]:
                    config[light] ^= 1

        if config.count(1) >0:
            print("problematic case: ")
            print(am)
            print(f"free: {free}, smallest no of presses {small}")
            print(f"shape: rows: {rows} cols:{cols}")
            print(f"solution {best_sol}")
            print(f"buttons {buttons}")
            print(f"config {config}")
            print()

        return small


    for line in inp:
        total += pressbuttons(line)
    return total



def day10part2solver(path):

    with open(path,"r") as file:
        inp = file.readlines()

    def pressbuttons(machine):
        """
        :param machine: a line from the input representing a machine
        :return: the minimal no of button presses needed
        """

        #config = list(map( lambda x: 1 if x=='#' else 0 ,machine.partition('{')[2].partition('}')[0]))
        # 1 if the light needs to be on 0 otherwise
        config = list(map(int,machine.partition('{')[2].partition('}')[0].split(',')))
        buttons = list(map( lambda x: list(map(int,x.split(','))),re.findall(r'\(([^)]+)\)',machine)))


        # each row is a list of buttons that contribute to that light
        eq = [[] for _ in range(0,len(config))]
        for i,button in enumerate(buttons):
            for l in button:
                eq[l] += [i]

        # solving using z3
        z3vars = [Int(f'x{i}') for i in range(0, len(buttons))] # vars in solver z3 will try to find
        solver = Optimize() # z3 solver

        # adding z3 constraints
        for var in z3vars: # non-negative number of button presses condition
            solver.add(var >= 0)

        for i,row in enumerate(eq): # solution to linear system of equations
            solver.add(sum(z3vars[x] for x in row) == config[i])

        solver.minimize(sum(var for var in z3vars))
        solver.check()
        sol = solver.model()
        tot = 0
        for var in z3vars:
            tot += sol[var].as_long()
        return tot


    total =0
    for line in inp:
        total += pressbuttons(line)

    return total



print(day10part2solver("../Input/Day10.txt"))