def Solution(ranks):
    m = max(ranks)
    dict = {}
    for i in range(len(ranks)):
        if ranks[i] < m:
            if ranks[i] not in dict:
                dict[ranks[i]] = 1
            else:
                dict[ranks[i]] += 1
    count = 0
    for key in dict.keys():
        if key == m-1:
            count += dict[key]
        elif key in dict and key+1 in dict:
            count += dict[key]
        else:
            count = count
    return count


print(Solution([3, 4, 3, 0, 2, 2, 3, 0, 0]))
