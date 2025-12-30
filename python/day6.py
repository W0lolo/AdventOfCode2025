def day6part1solver(path):
    total = 0
    with open(path, "r") as file:
        inp = file.readlines()
        inp = [line.strip().split(' ') for line in inp]

        inp = [ list(filter(lambda x: x != '',line)) for line in inp]

        operators = inp[len(inp)-1]
        for x in range(0,len(operators)):
            if operators[x] == '+':
                temp = 0
                for y in range(0,len(inp)-1):
                    temp +=int(inp[y][x])
                total += temp
            elif operators[x] == '*':
                temp = 1
                for y in range(0, len(inp) - 1):
                    temp *= int(inp[y][x])
                total += temp

        return total

def day6part2solver(path):
    total = 0
    with open(path, "r") as file:
        inp = file.readlines()

        def get_num(index:int):
            """
            :param index: column index
            :return: the number represented in that column
            """
            nonlocal inp
            num = ""

            for y in range(0,len(inp)-1):
                if inp[y][index] != ' ':
                    num += inp[y][index]

            return int(num)

        operators = inp[len(inp) - 1]

        def get_end_index(index:int):
            """
            :param index: column index
            :return: the index of the end of the sum
            """
            nonlocal inp
            nonlocal operators
            index += 1
            while index < len(operators):
                if operators[index] != ' ':
                    return index-1
                index += 1

            return index

        def get_operands(index:int):
            """
            :param index: start of sum index
            :return: list of operands that make the sum
            """
            end = get_end_index(index)
            operands = []
            for i in range(index,end):
                operands += [get_num(i)]
            return operands


        for i in range(0,len(operators)):
            if operators[i] == '+':# start of a sum
                temp = 0
                for op in get_operands(i):
                    temp += op
                total += temp
            elif operators[i] == '*':
                temp = 1
                for op in get_operands(i):
                    temp *= op
                total += temp

    return total



print(day6part2solver("../Input/Day6.txt"))