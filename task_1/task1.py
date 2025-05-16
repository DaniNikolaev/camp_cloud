def sort_list(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return sort_list(left) + middle + sort_list(right)


def main():
    try:
        original_list = list(map(int, input().split()))
    except ValueError:
        original_list = []

    even_list = list(filter(lambda x: x % 2 == 0, original_list))
    print(f'Четные числа: {even_list}')

    if original_list:
        print(f'Максимальное число: {max(original_list)}')
        print(f'Минимальное число: {min(original_list)}')
    else:
        print("Максимальное число: список пуст")
        print("Минимальное число: список пуст")

    sorted_list = sort_list(original_list)
    print(f'Отсортированный список: {sorted_list}')


if __name__ == "__main__":
    main()
