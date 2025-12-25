
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

    current = 50
    passes = 0
    for turn in inp:
        passes += abs(turn)//100 # counting full turns
        current = current + (turn%100) if turn >= 0 else current-((-turn)%100)

        if current == 0:
            passes += 1
        elif current > 100:
            passes += 1
            current -= 100
        elif current < 0:
            passes += 1
            current += 1

        current = current %100

    return passes

print(day1solverpart2("../Input/Day1test.txt"))
