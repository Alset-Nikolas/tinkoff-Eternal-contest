if __name__ == '__main__':
    n = int(input())
    links = list(map(int, input().split()))
    counts = [set() for x in range(n + 1)]
    number = 1
    povtors = None
    res = None
    for number_link in links:
        if number == number_link:
            '''Учет повторов'''
            if povtors is None:
                povtors = number
            else:
                res = (-1, -1)
                break
        else:
            counts[number_link].add(number)
        number += 1

    if res is None:
        if povtors is not None:
            counts_len_0 = 0
            ans = None
            for i, counts_i in enumerate(counts[1:]):
                if len(counts_i) == 0:
                    counts_len_0 += 1
                    ans = i + 1
            if counts_len_0 == 1:
                res = (povtors, ans)
            else:
                res = (-1, -1)
        else:
            counts_len_0 = 0
            counts_len_2 = 0
            ans_set_0 = 0
            ans_set_2 = 0
            for i, counts_i in enumerate(counts[1:]):
                if len(counts_i) == 0:
                    counts_len_0 += 1
                    ans_set_0 = i + 1
                if len(counts_i) == 2:
                    counts_len_2 += 1
                    ans_set_2 = i + 1
            if counts_len_0 == 1 and counts_len_2 == 1:
                counts[ans_set_2].remove(ans_set_0)
                res = (counts[ans_set_2].pop(), ans_set_0)
            else:
                res = (-1, -1)

    print(*res)
