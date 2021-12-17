def get_measurements():
    measurements = []
    content = ""
    with open("input2.txt", "r") as f:
        content = f.read()
    measurements = [l for l in content.split("\n") if len(l) > 0]
    return measurements


def solution():
    measurements = get_measurements()
#    measurements = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    hor, ver = 0, 0
    for m in measurements:
        config =  m.split(" ")
        key = config[0]
        value = int(config[1])
        if key == "forward":
            hor += value
        elif key == "up":
            ver -= value
        elif key == "down":
            ver += value
    return hor*ver


if __name__ == "__main__":
    ans = solution()
    print(ans)
