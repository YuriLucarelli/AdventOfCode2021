def main():
    f = open("day3.txt","r")
    lines = f.readlines()
    f.close()
    
    one_counter = [0,0,0,0, 0,0,0,0, 0,0,0,0]
    zero_counter = [0,0,0,0, 0,0,0,0, 0,0,0,0]

    gamma = 0
    epsilon = 0
    
    for line in lines:
        for i in range(12):
            if line[i] == '0': zero_counter[i] += 1
            else: one_counter[i] += 1

    for i in range(12):
        val = 2**(11-i)
        if zero_counter[i] > one_counter[i]:
            epsilon += val
        else:
            gamma += val
            
    print("gamma:",gamma)
    print("epsilon:",epsilon)
    print(gamma * epsilon)

if __name__ == "__main__":
    main()
