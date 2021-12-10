def main():
    f = open("day10.txt","r")
    lines = [i.replace('\n','') for i in f.readlines()]
    f.close()

    brackets = {")":"(","]":"[","}":"{",">":"<"}
    points = {")":3,"]":57,"}":1197,">":25137}
    solution = 0

    for line in lines:
        seq = ""
        for l in line:
            if l in "{[(<":
                seq += l
                continue
            if seq[-1] == brackets[l]:
                seq = seq[:-1]
            else:
                solution += points[l]
                break
    
    print(solution)

if __name__ == "__main__":
    main()