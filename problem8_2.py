#  aaaaa
# b     c
# b     c
#  ddddd
# e     f
# e     f
#  ggggg

# |----------------------------|
# | digit | number of segments |
# | 1     |       2            | you can get cf elements from 1
# | 7     |       3            |  
# | 4     |       4            | you can get bd elements by subtracting cf from 4
# | 8     |       7            | 
# |----------------------------|
# | 3     |       5            | in this group it's the only one with cf elements
# | 5     |       5            | once you found 3, 5 it's the only one in this group with bd elements
# | 2     |       5            | 2 it's found by process of elimination for this group
# |----------------------------| 
# | 6     |       6            | in this group it's the only one withOUT cf elements
# | 9     |       6            | once you found 6, 9 it's the only one in this group with bd elements
# | 0     |       6            | 0 it's found by process of elimination for this group
# |----------------------------|

def main():
    f = open("day8.txt","r")
    pairs = [i.replace('\n','').split('|') for i in f.readlines()]
    f.close()

    digits = [sorted(i[0].strip().split(' '), key=len) for i in pairs]
    codes = [i[1].strip().split(' ') for i in pairs]

    solution = 0    
    for i in range(len(digits)):
        dig = digits[i]
        #table contains the coding of every digit e.g. 'cf':1, 'acf':7 etc...
        table = {sort_string(dig[0]): 1, sort_string(dig[1]): 7, sort_string(dig[2]): 4, sort_string(dig[-1]): 8} 

        len_5_digits = dig[3:6]
        len_6_digits = dig[6:9]

        for j in range(3): #check which digit contains c and f segments
            if dig[0][0] in len_5_digits[j] and dig[0][1] in len_5_digits[j]:
                table[sort_string(len_5_digits.pop(j))] = 3
                break

        #contains bd segments
        bd_seg = remove_letters(dig[2], dig[0])
        for j in range(2): 
            if bd_seg[0] in len_5_digits[j] and bd_seg[1] in len_5_digits[j]: # find 5
                table[sort_string(len_5_digits[j])] = 5
                table[sort_string(len_5_digits[1-j])] = 2
                break
        
        for j in range(3):
            if not (dig[0][0] in len_6_digits[j] and dig[0][1] in len_6_digits[j]): # find 6
                table[sort_string(len_6_digits.pop(j))] = 6
                break

        for j in range(2):
            if bd_seg[0] in len_6_digits[j] and bd_seg[1] in len_6_digits[j]: # find 9 
                table[sort_string(len_6_digits[j])] = 9
                table[sort_string(len_6_digits[1-j])] = 0
                break
        res = table[sort_string(codes[i][0])]*1000 + table[sort_string(codes[i][1])]*100 + table[sort_string(codes[i][2])]*10 + table[sort_string(codes[i][3])]
        print(res)
        solution += res
    print(solution)

def sort_string(s1):
    return "".join(sorted(s1))  

#remove s2 letters from s1
def remove_letters(s1,s2):
    a = s1
    for l in s2: a = a.replace(l,"")
    return a
   
if __name__ == "__main__":
    main()