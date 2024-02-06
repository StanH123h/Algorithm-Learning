import random

a = [10, 2, 1, 3, 5, 4, 0, 9, 6, 8, 7]


def quick_sort(l):
    if len(l) <= 1:
        return l
    bigger = []
    smaller = []
    base_num = l.pop(random.randint(0, len(l) - 1))
    for item in l:
        if item > base_num:
            bigger.append(item)
        else:
            smaller.append(item)
    return quick_sort(smaller) + [base_num] + quick_sort(bigger)


print(quick_sort(a))
