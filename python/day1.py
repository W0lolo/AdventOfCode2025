
def day1solverpart1(path):
    with open(path,"r") as file:
        inp = file.read()

        count = 0 # number of times current lands on 0
        current = 50
        i =0
        mult = 1
        num_str = ""
        while i < len(inp):
            if inp[i].isalpha():
                if inp[i]=='R':
                    mult =1
                elif inp[i]=='L':
                    mult = -1
                i+=1
            elif inp[i].isdigit():
                num_str += inp[i]
                i+=1
                while i< len(inp) and inp[i].isdigit():
                    num_str += inp[i]
                    i+=1


                movabs = int(num_str)
                unwrapped = (current+(movabs*mult))
                next_pos = unwrapped%100

                # counting 0s
                if next_pos == 0:
                    count += 1

                current = next_pos
                num_str = ""

            else:
                i+=1

    return count

def day1solverpart2(path):
    with open(path,'r') as file:
        inp = list(map(int, file.read().replace('R', '').replace('L', '-').split()))


    passes = 0
    dial = 50
    for turn in inp:

        full, rem = divmod(abs(turn),100)
        passes += full
        rem = -rem if turn < 0 else rem
        nextdial = dial + rem

        if dial != 0:
            if rem < 0 and nextdial <=0:
                passes+=1
            elif rem > 0 and nextdial >= 100:
                passes+=1

        dial =nextdial%100
    return passes

print(day1solverpart2("../Input/Day1.txt"))

