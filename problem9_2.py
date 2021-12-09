values = None
def main():
    global values
    f = open("day9.txt","r")
    values = [[9] + [int(q) for q in i.replace('\n','')] + [9] for i in f.readlines()]
    f.close()

    x_len = len(values[0])
    values.append([9] * x_len)
    values.insert(0,[9] * x_len) 

    lens = []
    for i in range(1,len(values)-1):
        for j in range(1,x_len-1):
            if values[i][j] == 9: continue
            if values[i][j] >= values[i][j-1] or values[i][j] >= values[i][j+1] or values[i][j] >= values[i-1][j] or values[i][j] >= values[i+1][j]: continue

            positions = [[i,j]]
            compute_basin([i,j],positions)
            l = len(positions)

            if len(lens) < 3:
                lens.append(l)
                continue

            for q in range(3):
                if lens[q] < l:
                    print(l,lens)
                    lens.pop(q)
                    lens.append(l)
                    break
    print(lens[0] * lens[1] * lens[2])

# pos = position to check
# positions = positions already in that basin
def compute_basin(pos,positions):
    global values
    for direction in [[1,0],[-1,0],[0,1],[0,-1]]:
        p = [pos[0] + direction[0], pos[1] + direction[1]]

        if p[0] == 0 or p[0] == len(values)-1 or p[1] == 0 or p[1] == len(values[0])-1: continue
        if values[p[0]][p[1]] == 9: continue
        if values[p[0]][p[1]] < values[pos[0]][pos[1]]: continue

        check = False
        for pp in positions:
            if pp[0] == p[0] and pp[1] == p[1]:
                check = True
                break
        if check: continue

        positions.append(p)
        compute_basin(p, positions)

if __name__ == "__main__":
    main()