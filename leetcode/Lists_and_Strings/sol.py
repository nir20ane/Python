def solution(n):
    narr = []
    for i in range(len(str(n))):
        narr.append(int(str(n)[i]))
    narr.sort(reverse = True)

    strr = ""
    for i in narr:
        strr += str(i)
    if n < int(strr):
        return int(strr)
    else:
        return n


print(solution(553))
