def main():
    f = open("day7.txt","r")
    values = [int(i) for i in f.readline().replace('\n','').split(',')]
    f.close()

    fuel = 0
    for av in range(min(values),max(values)):
        res = sum([sum(range(1,1+abs(i-av))) for i in values])
        if fuel == 0 or res < fuel: fuel = res
        print(av,res,fuel)
    
    print(fuel)

if __name__ == "__main__":
    main()