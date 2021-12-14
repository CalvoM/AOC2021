def get_numbers():
    numbers = []
    with open("test.txt", "r") as f:
        content = f.read()
        numbers = [k for k in content.split("\n\n") if len(k) > 0]
    return numbers


def solution():
    numbers = get_numbers()
    random_numbers = numbers[0]
    numbers = numbers[1:]
    for (i,n) in enumerate(numbers):
        numbers[i] = n.split("\n")
    print(numbers)


if __name__ == "__main__":
    solution()
