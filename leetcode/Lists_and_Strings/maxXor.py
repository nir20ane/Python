def maxXor(l, r, k):
    diff = []
    a = l
    while a < r:
        b = a+1
        while b <= r:
            if a^b <= k:
                diff.append(a^b)
            b += 1
        a += 1
    return max(diff)

result = maxXor(1,6789, 9999)
print(result)