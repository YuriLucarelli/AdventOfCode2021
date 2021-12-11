values = None
def main():
    global values
    f = open("day11.txt","r")
    values = [[int(j) for j in i.replace('\n','')] for i in f.readlines()]
    f.close()

    flashes = 0
    sim = -1
    for i in range(1,501):
        res = compute_step()
        if res == 100 and sim == -1: sim = i
        flashes += res
        if i == 100: print(i,flashes)
    print("sincronized flash %d" % sim)

def compute_step():
    global values
    positions = list()
    for i in range(10):
        for j in range(10):
            values[i][j] += 1
            if values[i][j] > 9: positions.append([i,j])

    old_positions = list()
    check = True
    while check:
        new_positions = list()
        check = False
        for pos in positions:
            old_positions.append(pos)
            for i in range(-1,2):
                for j in range(-1,2):
                    if i == 0 and j == 0: continue
                    x = pos[0] + i
                    y = pos[1] + j
                    if x >= 10 or x < 0: continue
                    if y >= 10 or y < 0: continue
                    
                    values[x][y] += 1

                    if values[x][y] == 10: 
                        new_positions.append([x,y])
                        check = True # don't stop the cycle
        
        positions = new_positions
    
    for p in old_positions: values[p[0]][p[1]] = 0
    return len(old_positions)

if __name__ == "__main__":
    main()