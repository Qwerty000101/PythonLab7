#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    A = [float(i) for i in input("Введите числа через пробел\n").split()]
    B = [abs(i) for i in A]
    index_min = B.index(min(B))
    print(f"Номер минимального по модулю элемента списка: {B.index(min(B))}")

    index_negative = 0
    counter_negative = 0
    for i, item in enumerate(A):
        if item < 0:
            index_negative = i
            counter_negative += 1
            break

    sum_elements = 0
    if counter_negative == 0:
        print("В списке нет отрицательных элементов")
    else:
        sum_elements = sum(B[index_negative+1:])
        print(f"Сумма модулей элементов списка, расположенных после"
              f" первого отрицательного элемента: {sum_elements}")

    a = float(input("Введите значение а: "))
    b = float(input("Введите значение b: "))

    C = [i for i in A if i < a or i > b]
    del_counter = len(A) - len(C)
    
    print("Новый список:")
    print(*(C + [0]*del_counter), sep="  ")