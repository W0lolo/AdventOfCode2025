import math

def day2part1solver(path):
    with open(path,"r") as file:
        inp = file.read().rsplit(',')
        ranges = [tuple(map(int,p.split('-'))) for p in inp]

    ranges =sorted(ranges, key=lambda x:x[0])

    maxrange = ranges[len(ranges)-1][1] # cutoff point
    invalidtot : int =  0

    i=1
    repeated = 11
    rgind = 0
    while repeated < maxrange:
        # finding range that can fit repeated
        while ranges[rgind][1]<repeated:
            rgind += 1

        # checking if repeated is in the range
        if ranges[rgind][0] <= repeated <= ranges[rgind][1]:
            invalidtot += repeated
            print(f"{repeated} +  in  + {ranges[rgind]}")

        i += 1
        repeated = i * (10 ** (int(math.log10(i)) + 1)) + i


    return invalidtot

def day2part2solver(path):
    with open(path,"r") as file:
        inp = file.read().rsplit(',')
        ranges = [tuple(map(int,p.split('-'))) for p in inp]

    ranges =sorted(ranges, key=lambda x:x[0])

    maxrange = ranges[len(ranges)-1][1] # cutoff point
    maxdigits = int(math.log10(maxrange)) + 1
    invalidtot : int =  0


    repetitions = 1
    invalidno = set()

    while repetitions < maxdigits:
        repetitions += 1
        i = 1
        repeated = calc_repeated(i,repetitions)

        rgind = 0
        while repeated < maxrange:
            # finding range that can fit repeated
            while ranges[rgind][1] < repeated:
                rgind += 1

            # checking if repeated is in the range
            if ranges[rgind][0] <= repeated <= ranges[rgind][1] and not (repeated in invalidno):
                invalidtot += repeated
                invalidno.add(repeated)
                print(f"{repeated} +  in  + {ranges[rgind]} + {i}x{repetitions}")

            i += 1
            repeated = calc_repeated(i,repetitions)

    return invalidtot


def calc_repeated(x,repetitions):
    tot = x
    for y in range(1,repetitions):
        exp = (10 ** (int(math.log10(x)) + 1))**y

        tot += x*  exp
    return tot

print(day2part2solver("../Input/Day2.txt"))

print(calc_repeated(12,1))
print(calc_repeated(12,2))