def solution(l):
    coeff = [0] * len(l)
    counter = 0
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                coeff[i] = coeff[i] + 1
                counter = counter + coeff[j]
    return counter
