import argparse
import random


def append_array(main_arr, arr, limit):
    sum = 0
    for i in arr:
        sum = sum + i

    start = -sum
    end = limit - sum

    for i in range(start, end):
        if i == 0 or i + sum == 0:
            continue
        a = arr.copy()
        a.append(i)
        main_arr.append(a)


def generate_two_numbers(limit):
    arr = []

    for i in range(1, limit):
        a = [i]
        append_array(arr, a, limit)

    return arr


def generate_numbers(limit, c):
    if c < 1:
        raise Exception("column cannot be less than 2")

    c -= 2
    arr = generate_two_numbers(limit)
    for _ in range(0, c):
        a = []
        for aa in arr:
            append_array(a, aa, limit)
        arr = a

    return arr


def random_select(arr, n):
    arr_size = len(arr)
    if arr_size < n:
        raise Exception("cannot select " + str(n) +
                        " for array length " + str(len(array)))

    ret = []
    selected_idx = set()
    while n > 0:
        idx = random.randrange(0, arr_size)
        while idx in selected_idx:
            idx = random.randrange(0, arr_size)
        selected_idx.add(idx)
        ret.append(arr[idx])
        n = n - 1
    return ret


def str_equation(arr):
    s = ""
    n = len(arr)
    for i in range(0, n):
        if i != 0 and arr[i] > 0:
            s = s + "+"
        s = s + str(arr[i])
    s = s + "="
    return s


def add_main(limit, column, nums, pages):
    row = (int)(nums / len(column))
    if row <= 0:
        raise Exception("row (nums / len(column)) is less than 0")

    arrs = []
    for i in column:
        arrs.append(generate_numbers(limit, i))

    for i in range(0, pages):
        print("Page " + str(i + 1) +
              "    Date:___________     Name:____________\n")
        cols = []
        for c in arrs:
            cols.append(random_select(c, row))

        for r in range(0, row):
            for a in cols:
                equation = str_equation(a[r])
                space = ""
                for _ in range(0, 14-len(equation)):
                    space = space + " "
                print(equation, end=space)
            print()

        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit", type=int,
                        help="set the limit of plus method, etc. 20", default=20)
    parser.add_argument("-c", "--column", nargs='+', type=int,
                        help="set the column of plus method, etc. \"2 3 3 4\"", default=[2, 3, 3, 4])
    parser.add_argument("-n", "--nums", type=int,
                        help="set how many items will be generated in one page, etc. 100", default=100)
    parser.add_argument("-p", "--pages", type=int,
                        help="set how many pages will be generated, etc. 30", default=30)

    args = parser.parse_args()

    add_main(args.limit, args.column, args.nums, args.pages)
