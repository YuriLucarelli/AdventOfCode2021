def main():
    f = open("day14.txt","r")
    lines = f.readlines()
    sequence = lines[0].replace('\n','')
    rules = [i.replace('\n','').split(" -> ") for i in lines[2:]]
    del lines
    f.close()

    pairs = dict()
    counts = dict()
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in letters:
        for j in letters: pairs["%s%s" % (i,j)] = 0
        counts[i] = 0

    for i in range(1,len(sequence)):
        pairs[sequence[i-1:i+1]] += 1

    for q in range(40):
        new_pairs = { key : 0 for key in pairs.keys()}

        for rule in rules:
            num = pairs[rule[0]]
            new_pairs["%s%s" % (rule[0][0], rule[1])] += num
            new_pairs["%s%s" % (rule[1], rule[0][1])] += num

        pairs = new_pairs

    counts[sequence[-1]] += 1 # first character stays the same for the entire process
    counts[sequence[0]] += 1 # same for the last character
    for key in pairs.keys():
        counts[key[0]] += pairs[key]
        counts[key[1]] += pairs[key]

    minl = counts[sequence[0]]
    maxl = counts[sequence[0]]
    for key in counts:
        if counts[key] != 0: minl = min(minl,counts[key])
        maxl = max(maxl,counts[key])
    print(maxl/2,minl/2,int((maxl - minl)/2))
    
if __name__ == "__main__":
    main()