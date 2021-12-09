def main():
    f = open("day9.txt","r")
    values = [[9] + [int(q) for q in i.replace('\n','')] + [9] for i in f.readlines()]
    f.close()

    x_len = len(values[0])
    values.append([9] * x_len)
    values.insert(0,[9] * x_len) 

    solution = 0
    for i in range(1,len(values)-1):
        for j in range(1,x_len-1):
            if values[i][j] == 9: continue
            if values[i][j] < values[i][j-1] and values[i][j] < values[i][j+1] and values[i][j] < values[i-1][j] and values[i][j] < values[i+1][j]:
                solution += values[i][j] + 1 
    print(solution)

if __name__ == "__main__":
    main()