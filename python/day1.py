
def day1solver(path):
    with open(path,"r") as file:
        inp = file.read()


        count = 0
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
                current = (current+(mult*int(num_str)))%100
                if current < 0:
                    current *=-1
                num_str = ""
                count += 1 if current ==0 else 0
            else:
                i+=1

    return count