def main():
    f = open("num.txt","r")
    lines = f.readlines()
    f.close()
    
    values = list()
    for l in lines: values.append(int(l.replace("\n","")))

    counter = 1
    solution = 0
    while counter < len(values):
        if (values[counter] - values[counter-1]) > 0: solution += 1
        counter += 1
    print(solution)

if __name__ == "__main__":
    main()
