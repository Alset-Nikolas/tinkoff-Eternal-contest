if __name__ == '__main__':
    l, r = input().split()
    l, r = min(l, r), max(l, r)

    res = 0
    len_start = len(l)
    len_end = len(r)
    if len_end > len_start+1:
        res += (len_end - len_start - 1) * 9
    if len_end > len_start:
        if int(l[0]*len_start)>=int(l):
            res += 9 - int(l[0])+1
        else:
            res += 9 - int(l[0])
        if int(r[0]*len_end) <= int(r):
            res += int(r[0])
        else:
            res += int(r[0]) - 1
    else:
        if int(l[0] * len_start) >= int(l):
            res += 9 - int(l[0]) +1
        else:
            res += 9 - int(l[0])
        if int(r[0] * len_end) <= int(r):
            res -= 9 - int(r[0])
        else:
            res -= 9 - int(r[0]) + 1
    print(res)
