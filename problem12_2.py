routes_count = 0
links = None
def main():
    global links
    f = open("day12.txt","r")
    links = [i.replace('\n','').split('-') for i in f.readlines()]
    f.close()

    routes = list()
    routes_count = 0
    paths = compute_paths(["start"])
    print(paths)

def compute_paths(seq,two_passes = False):
    global links, routes_count
    paths = list()

    for link in links:
        if not (link[0] == seq[-1] or link[1] == seq[-1]): continue
        destination = link[0]
        if link[0] == seq[-1]: destination = link[1]

        if destination == "start": continue
        if is_small(destination):
            if two_passes and destination in seq: continue

        paths.append(destination)

    counter = 0
    while counter < len(paths):
        if paths[counter] == "end":
            routes_count += 1
            paths.pop(counter)
        else: 
            counter += 1

    if len(paths) == 0: return routes_count

    for p in paths:
        path = seq + [p]

        if not two_passes:
            check = True
            for i in path:
                if not is_small(i): continue
                if path.count(i) > 1:
                    compute_paths(path,True)
                    check = False
                    break
            if check:
                compute_paths(path,False)
        else: compute_paths(path,True)

    return routes_count

def is_small(code): return code == code.lower()

if __name__ == "__main__":
    main()