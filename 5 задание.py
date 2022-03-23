if __name__ == '__main__':
    l, r = input().split()
    len_start = len(l)
    first_number = l[0]
    res = 0
    start_number = first_number*len_start
    while int(start_number) <= int(r):
        res += 1
        if first_number == "9":
            len_start += 1
            first_number = "0"

        first_number = str(int(first_number) + 1)
        start_number = first_number*len_start
    print(res)
