def main():
    f = open("day4.txt","r")
    lines = f.readlines()
    f.close()
    tables = list()
    grid = list()
    numbers = [int(i) for i in lines[0].replace('\n','').split(',')]

    for l in lines[2:]:
        line = l.replace('\n','')
        if line == "":
            tables.append(Table(grid))
            grid = list()
            continue
        grid.append([ int(i) for i in line.strip().replace('  ',' ').split(' ')] )
    if len(grid) != 0:
        tables.append(Table(grid))

    i = 0
    while i < len(numbers):
        j = 0
        while j < len(tables):
            table = tables[j]
            table.check(numbers[i])
            if table.is_winning():
                if len(tables) == 1:
                    for r in table.grid:
                        print(r)
                    print(numbers[i])
                    print(numbers[i] * tables[0].result())
                    i = len(numbers)
                    break
                else: 
                    print(len(tables),numbers[i])
                    tables.pop(j)
            else: j += 1
        i += 1
    

class Table:
    grid = list()

    def __init__(self,grid):
        self.grid = grid

    def result(self):
        return sum([sum(row) for row in self.grid])

    def check(self,number):
        for i in range(5):
            row = self.grid[i]
            if number in row:
                #print("check",number)
                row[row.index(number)] = 0
                return True
        return False

    def is_winning(self):
        for row in self.grid:
            if sum(row) == 0:
                return True
        for i in range(5):
            check = True
            for j in range(5):
                if self.grid[j][i] != 0:
                    check = False
                    break
            if check: 
                return True
        return False

if __name__ == "__main__":
    main()
