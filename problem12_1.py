links = None
def main():
    global links
    f = open("day12.txt","r")
    links = [i.replace('\n','').split('-') for i in f.readlines()]
    f.close()

    routes = list()
    paths = compute_paths(["start"],list())
    
    print(len(paths))

def compute_paths(seq,routes):
    global links
    paths = list()

    for link in links:
        if not (link[0] == seq[-1] or link[1] == seq[-1]): continue
        destination = link[0]
        if link[0] == seq[-1]: destination = link[1]

        if destination == "start": continue

        if is_small(destination) and destination in seq: continue
        
        paths.append(destination)

    counter = 0
    while counter < len(paths):
        if paths[counter] == "end":
            routes.append(seq + [paths.pop(counter)])
        else: 
            counter += 1

    if len(paths) == 0: return routes

    for p in paths:
        compute_paths(seq + [p], routes)

    return routes
    
def is_small(code):
    return code == code.lower()

if __name__ == "__main__":
    main()