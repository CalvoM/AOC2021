def get_heights():
    heights = []
    with open("input.txt", "r") as f:
        content = f.read().split("\n")
        heights = [int(h) for h in content if len(h) > 0]
    return heights

def solution():
    heights = get_heights()
    heights = [199,200,208,210,200,207,240,269,260,263]
    depth = len(heights) - 7

if __name__ == "__main__":
    solution()
