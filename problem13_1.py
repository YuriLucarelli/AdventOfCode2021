def main():
    global links
    f = open("day13.txt","r")
    lines = f.readlines()
    folds = [[j[0][-1],int(j[1])] for j in [i.replace('\n','').split("=") for i in lines[-12:]]]
    points = [[int(j[0]), int(j[1])] for j in [i.replace('\n','').split(',') for i in lines[:-13]]]
    del lines
    f.close()

    ly = 895
    lx = 1311
    table = [[0 for _ in range(lx)] for i in range(ly)]
    for point in points: 
        table[point[1]][point[0]] = 1

    for fold in folds:
        if fold[0] == 'x':
            for i in range(ly):
                for j in range(fold[1]+1):
                    table[i][fold[1] - j] = int(table[i][fold[1] - j] or table[i][fold[1] + j])
            lx = fold[1]
        else:
            for i in range(fold[1]+1):
                for j in range(lx):
                    table[fold[1] - i][j] = int(table[fold[1] - i][j] or table[fold[1] + i][j])
            ly = fold[1]
        table = [[table[i][j] for j in range(lx)] for i in range(ly)]
        print(sum([sum(i) for i in table]))
    for i in table: print(''.join([" " * (1-q) + "#"*q for q in i]))
if __name__ == "__main__":
    main()