def get_report():
    report_nums = []
    with open("input3.txt", "r") as f:
        content = f.read()
        report_nums = [r for r in content.splitlines() if len(r)>0]
    return report_nums,len(report_nums[0])


def sol():
    diagnostic, rep_len = get_report()
    ones = [0] * rep_len
    for d in diagnostic:
        for (i,n) in enumerate(d):
            ones[i] += int(n)

    gamma = ""
    for o in ones:
        if o >= len(diagnostic)/2:
            gamma += "1"
        else:
            gamma += "0"
    gamma = int(gamma, 2)
    epsilon = gamma ^ (2**rep_len)-1
    return gamma * epsilon


if __name__ == "__main__":
    ans = sol()
    print(ans)
