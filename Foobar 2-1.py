def solution(i):
    lenght = len(i)
    right_arrow = []
    left_arrow = []
    total = 0
    for j in range(lenght):
        if i[j] == ">":
            right_arrow.append(j)
        if i[j] == "<":
            left_arrow.append(True)
        if i[j] != "<":
            left_arrow.append(False)
    for k in right_arrow:
        total += sum(left_arrow[k:])
    return total*2







