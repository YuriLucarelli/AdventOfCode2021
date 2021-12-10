def main():
    f = open("day10.txt","r")
    lines = [i.replace('\n','') for i in f.readlines()]
    f.close()

    brackets = {")":"(","]":"[","}":"{",">":"<"}
    points_2 = {")":1,"]":2,"}":3,">":4}
    results = []

    for line in lines:
        seq = ""
        corrupted = False
        for l in line:
            if l in "{[(<":
                seq += l
                continue
            if seq[-1] == brackets[l]:
                seq = seq[:-1]
            else: 
                corrupted = True
                break
        if corrupted: continue

        result = 0
        for l in seq[::-1]:
            result *= 5
            c = list(brackets.keys())[list(brackets.values()).index(l)]
            result += points_2[c]
        print(seq,result)
        results.append(result)

    results = sorted(results)
    print(results[len(results)//2])

if __name__ == "__main__":
    main()