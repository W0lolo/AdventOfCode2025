from functools import lru_cache

def day11part1solver(path):
    # assuming there are no cycles otherwise there would be an infinite number of paths
    with open(path,"r") as file:

        graph = {}
        for line in file:
            nodes = line.split(' ')
            nodes[0] = nodes[0][:-1]
            nodes[-1] = nodes[-1][:-1] if nodes[-1][-1] == '\n' else nodes[-1] # last line doesnt have an \n

            graph[nodes[0]] = nodes[1:]

        graph['out'] = [] # not strictly necessary

        pathno = 0
        def traverse(current):
            nonlocal graph
            nonlocal pathno
            connections = graph[current]
            for device in connections:
                if device == 'out':
                    pathno+=1
                else:
                     traverse(device)

        traverse('you')
        return pathno

def day11part2solver(path):

    with open(path,"r") as file:

        graph = {}
        for line in file:
            nodes = line.split(' ')
            nodes[0] = nodes[0][:-1]
            nodes[-1] = nodes[-1][:-1] if nodes[-1][-1] == '\n' else nodes[-1] # last line doesnt have an \n

            graph[nodes[0]] = nodes[1:]

        graph['out'] = []

        @lru_cache(maxsize=None)
        def traverse(current: str,fft = False,dac = False,end ='out') -> int:
            """
            :param dac:
            :param fft:
            :param current: current node
            :param end: end node
            :return:
            """
            nonlocal graph
            connections = graph[current]
            total = 0
            for device in connections:
                if device == end:
                    if fft and dac:
                        return 1
                else:
                    total += traverse(device,fft or device == 'fft',dac or device == 'dac')
            return total

        return traverse('svr')





print(day11part2solver("../Input/Day11.txt"))