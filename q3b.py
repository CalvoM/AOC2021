def get_report():
    report_nums = []
    with open("input3.txt", "r") as f:
        content = f.read()
        report_nums = [r for r in content.splitlines() if len(r)>0]
    return report_nums,len(report_nums[0])

def get_ox_rating(index, repo_list = None):
    if len(repo_list) == 1:
        return "".join(repo_list)
    ones = 0
    for r in repo_list:
        if r[index] == "1":
            ones += 1
    check = "1"
    if ones <len(repo_list)/2:
        check = "0"
    removing = []
    for (i,r) in enumerate(repo_list):
        if r[index] != check:
            removing.append(i)
    rem_tracker = 0
    for r in removing:
        del repo_list[r -rem_tracker]
        rem_tracker += 1
    index += 1
    return get_ox_rating(index, repo_list)


def get_carb_rating(index, repo_list = None):
    if len(repo_list) == 1:
        return "".join(repo_list)
    zeros = 0
    for r in repo_list:
        if r[index] == "0":
            zeros += 1
    check = "0"
    if zeros > len(repo_list)/2:
        check = "1"
    removin = []
    for (i,r) in enumerate(repo_list):
        if r[index] != check:
            removin.append(i)
    rem_tracker = 0
    for r in removin:
        del repo_list[r - rem_tracker]
        rem_tracker += 1
    index += 1
    return get_carb_rating(index, repo_list)


def sol():
    diagnostic, rep_len = get_report()
    oxlist = diagnostic.copy()
    carblist = diagnostic.copy()
    ox_rating = int(get_ox_rating(0, oxlist),2)
    carb_rating = int(get_carb_rating(0, carblist), 2)
    print(ox_rating, carb_rating)
    return ox_rating * carb_rating

if __name__ == "__main__":
    ans = sol()
    print(ans)
