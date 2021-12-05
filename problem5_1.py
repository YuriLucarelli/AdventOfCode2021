def main():
    f = open("day5.txt","r")
    lines = f.readlines()
    f.close()
    tables = list()
    grid = list()

    # x1,y1,x2,y2
    coords = [[int(k[0]),int(k[1]),int(k[2]),int(k[3])] for k in [j for j in [i[:-1].replace(' -> ',',').split(",") for i in lines]]]
    del lines

    table = [[0 for i in range(1000)] for j in range(1000)]
    solution = 0

    for row in coords:
        t = -1
        if row[0] == row[2]:
            t = 1
        elif row[1] == row[3]:
            t = 0
        else: continue

        minimum = min(row[t], row[2+t])
        maximum = max(row[t], row[2+t])

        for i in range(minimum,maximum+1):
            if t == 0:
                table[i][row[1]] += 1
                if table[i][row[1]] == 2: solution += 1
            elif t == 1:
                table[row[0]][i] += 1
                if table[row[0]][i] == 2: solution += 1

    print(solution)

if __name__ == "__main__":
    main()