def day3solverpart1(path):
    with open(path, "r") as file:
        inp=file.read().split('\n')
        banks = [ list(map(int,s)) for s in inp]

    total = 0
    for bank in banks:

        # indices
        left = 0
        right = len(bank)-1

        mlindex = 0
        mrindex = right
        mlval = bank[mlindex]
        mrval = bank[mrindex]

        left+=1
        while left < right:
            if bank[left] > mlval:
                mlval = bank[left]
                mlindex = left
            left+= 1

        right -= 1
        while right > mlindex:
            if bank[right] > mrval:
                mrval = bank[right]
            right -= 1

        total += mrval + mlval*10

    return total

def day3solverpart2(path):
    with open(path, "r") as file:
        inp=file.read().split('\n')
        banks = [ list(map(int,s)) for s in inp]

    total = 0
    for bank in banks:

        temp = 0
        index = 0 # the digit we are finding
        lasti = 0 # the index of the last digit we found

        while index < 12:
            # find the largest possible index'th digit
            i = lasti # starting at the next digit
            maxdigit = bank[i]
            while i < len(bank)-(11-index):
                if bank[i] > maxdigit:
                    maxdigit = bank[i]
                    lasti = i
                i+= 1

            temp += (10**(11-index))*maxdigit
            lasti += 1
            index+=1
            
        total+= temp


    return total



print(day3solverpart2("../Input/Day3.txt"))