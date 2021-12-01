def main():
    f = open("num.txt","r")
    lines = f.readlines()
    f.close()
    
    values = list()
    for l in lines: values.append(int(l.replace("\n","")))

    windows = list()
    for i in range(2,len(values)): windows.append(values[i] + values[i-1] + values[i-2])
    
    counter = 1
    solution = 0
    while counter < len(windows):
        if (windows[counter] - windows[counter-1]) > 0: solution += 1
        counter += 1
    print(solution)

if __name__ == "__main__":
    main()
