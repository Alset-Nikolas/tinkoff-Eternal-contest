if __name__ == '__main__':
    n, t_min = list(map(int, input().split()))
    numbers_room = list(map(int, input().split()))
    number_person = int(input())
    number_person_index = number_person - 1
    if numbers_room[number_person_index] - numbers_room[0] <= t_min or numbers_room[-1] - \
            numbers_room[number_person_index] <= t_min:
        res = numbers_room[-1] - numbers_room[0]
    else:
        res = min(numbers_room[number_person_index] - numbers_room[0],numbers_room[-1] -numbers_room[number_person_index])  + numbers_room[-1] - numbers_room[0]
    print(res)