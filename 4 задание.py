if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    sum1 = sum(numbers)
    delta = []
    for i, number in enumerate(numbers):
        number_str = str(number)
        for i in range(len(number_str)):
            new_number = "".join([str(number)[:i], "9", str(number)[i+1:]])
            delta.append(int(new_number) - number)
    delta.sort(reverse=True)
    print(sum(delta[:k]))
