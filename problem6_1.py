def main():
    f = open("day6.txt","r")
    values = [int(i) for i in f.readline().replace('\n','').split(',')]
    f.close()

    # num of fishes for grouped by days until the next spawn starting from 0
    fishes = [0 for _ in range(9)]
    for i in values: fishes[i] += 1

    next_fishes = 0
    for i in range(256):
        next_fishes = fishes[0]
        for j in range(1,9):
            fishes[j-1] = fishes[j]
        fishes[8] = next_fishes
        fishes[6] += next_fishes

        print(i+1,sum(fishes))

if __name__ == "__main__":
    main()