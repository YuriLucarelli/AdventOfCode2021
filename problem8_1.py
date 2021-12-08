def main():
    f = open("day8.txt","r")
    pairs = [i.replace('\n','').split('|') for i in f.readlines()]
    f.close()

    # digits = [sorted(i[0].strip().split(' '), key=len) for i in pairs]
    codes = [i[1].strip().split(' ') for i in pairs]

    solution = 0    
    for i in range(len(codes)):
        for q in codes[i]:
            if len(q) in [2,3,4,7]:
                solution += 1
    print(solution)
        

if __name__ == "__main__":
    main()