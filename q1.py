heights = []
def get_heights():
    with open("input.txt", "r") as f:
        content = f.read()
        heights = [int(h) for h in content.split("\n") if len(h) > 0]
        return heights

if __name__ == "__main__":
    heights = get_heights()
    prev = None
    inc = 0
    for h in heights:
        if prev == None:
            prev = h
            continue
        else:
            if h > prev:
                inc+=1
            prev = h

    print(inc)
