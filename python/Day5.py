def day5part1solver(path):
    fresh = 0
    with open(path, "r") as file:
        temp = file.readline()

        # reading ranges
        ranges = []
        while len(temp) > 1:
            ranges += [tuple(map(int,temp.strip().split('-')))]
            temp = file.readline()

        ranges.sort()

        # reading ids
        ids = [int(s.strip()) for s in file.readlines()]
        ids.sort()

        index = 0
        for food in ids:

            while index < len(ranges) and food > ranges[index][1]:
                index+=1

            if index == len(ranges):
                break

            if ranges[index][0] <= food <= ranges[index][1]:
                print(f"{food} is fresh")
                fresh += 1

    return fresh

def day5part2solver(path):
    fresh = 0
    with open(path, "r") as file:
        temp = file.readline()

        # reading ranges
        ranges = []
        while len(temp) > 1:
            ranges += [tuple(map(int,temp.strip().split('-')))]
            temp = file.readline()

        ranges.sort()
        last = 0
        for ran in ranges:
            fresh += max(ran[1]-max(ran[0]-1,last),0)
            last = ran[1]


    return fresh



print(day5part2solver("../Input/Day5.txt"))