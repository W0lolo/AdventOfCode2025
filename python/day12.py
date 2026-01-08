
def day12part1solver(path):

    with open(path,'r') as file:
        shapes = []
        current = []
        for line in file:
            if len(line)<=1:
                shapes.append(current[1:])
                current=[]
            else:
                current.append(line[:-1] if line[-1] == '\n' else line)

        trees = [ tree.split() for tree in current]
        presents = [ list(map(int,tree[1:])) for tree in trees]
        dimensions = [ list(map(int,tree[0][:-1].split('x'))) for tree in trees]

        sizes = []
        for s in shapes:
            count = 0
            for l in s:
                count += l.count('#')
            sizes.append(count)

        def calc_area(present):
            nonlocal sizes
            area = 0
            for i,amm in enumerate(present):
                area += sizes[i] * amm
            return area

        fitting = 0
        for pres, dim in zip(presents,dimensions):

            if calc_area(pres) < dim[0]*dim[1]:
                fitting+=1


        return fitting








print(day12part1solver("../Input/Day12.txt"))