def main():
    f = open("directions.txt","r")
    lines = f.readlines()
    f.close()
    
    values = list()
    for l in lines:
        pair = l.replace("\n","").split(" ")
        values.append([pair[0], int(pair[1])])

    x_pos = 0
    aim = 0
    depth = 0
    for pair in values:
        if pair[0] == "forward":
            x_pos += pair[1]
            depth += pair[1] * aim
        elif pair[0] == "down":
            aim += pair[1]
        elif pair[0] == "up":
            aim -= pair[1]
    print(x_pos)
    print(depth)
    print(x_pos * depth)

if __name__ == "__main__":
    main()
