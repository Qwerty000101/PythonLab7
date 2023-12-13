#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    A = [int(i) for i in input("Введите 10 целых чисел через пробел:\n").split()]
    if len(A) != 10:
        print("Должно быть введено 10 элементов", file=sys.stderr)
        exit(1)

    index_max = A.index(max(A))
    temp_first = A[0]
    temp_second = A[index_max]

    A[0] = temp_second
    A[index_max] = temp_first

    for item in A:
        print(item, end=' ')