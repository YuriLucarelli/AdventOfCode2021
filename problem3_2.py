def main():
    f = open("day3.txt","r")
    lines = f.readlines()
    f.close()
    
    oxi = 0
    co2 = 0

    oxi_candidates = list()
    co2_candidates = list()
    for i in lines:
        oxi_candidates.append(i)
        co2_candidates.append(i)
    
    for position in range(12):
        oxi_zero, oxi_one = count_zero_one(oxi_candidates,position)
        co2_zero, co2_one = count_zero_one(co2_candidates,position)
                
        co2_num = "%d" % int(co2_zero > co2_one)
        oxi_num = "%d" % int(oxi_one >= oxi_zero)        

        if len(oxi_candidates) == 1:
            c = oxi_candidates.pop(0)
            oxi = compute_number(c)
        if len(co2_candidates) == 1:
            c = co2_candidates.pop(0)
            co2 = compute_number(c)
        
        select_candidates(oxi_candidates,position,oxi_num)
        select_candidates(co2_candidates,position,co2_num)
            
    print("oxi:",oxi)
    print("co2:",co2)
    print(oxi * co2)

def compute_number(candidate):
    num = 0
    for i in range(12):
        candidate
        num += int(candidate[i] == '1') * (2**(11-i))
    return num

def count_zero_one(candidates,position):
    one_counter = zero_counter = 0
    for line in candidates:
        if line[position] == '0':
            zero_counter += 1
        else:
            one_counter += 1
    return zero_counter, one_counter

def select_candidates(candidates, position, num):
    counter = 0
    while counter < len(candidates):
        if candidates[counter][position] != num:
            candidates.pop(counter)
        else: counter += 1

if __name__ == "__main__":
    main()
