#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    A = input("Введите 10 целых чисел через пробел:\n").split()

    if len(A) != 10:
        print("Должно быть введено 10 элементов", file=sys.stderr)
        exit(1)

    B = []
    for item in A:
        B.append(int(item))

    index_max = B.index(max(B))
    temp_first = B[0]
    temp_second = B[index_max]

    B[0] = temp_second
    B[index_max] = temp_first

    for item in B:
        print(item, end=' ')