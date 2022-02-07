def shift(lst, steps):
    for _ in range(steps):
        temp_lst = lst[len(lst) - 1]
        for i in range(len(lst) - 2, -1, -1):
            lst[i + 1] = lst[i]
        lst[0] = temp_lst
    return lst


def main():
    shift_count = int(input("Сдвиг: "))
    str_list = input("Изначальный список: ")
    nums = [int(i) for i in str_list[1:-1].split(', ')]
    print("Сдвинутый список:", shift(nums, shift_count))


if __name__ == '__main__':
    main()
