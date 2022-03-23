if __name__ == '__main__':
    n = int(input())
    ans = 0
    while n >0:
        if n % 2 != 0:
            n -= 1
        else:
            n /=2
        ans+=1
    print(ans-1)