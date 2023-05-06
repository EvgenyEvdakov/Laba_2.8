#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    return input("Введите число: ")


def test_input(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def str_to_int(num):
    return int(num)


def print_int(num):
    print(f"Введенное значение: {num}")


# Основная ветка программы
if __name__ == '__main__':
    num_str = get_input()
    if test_input(num_str):
        num_int = str_to_int(num_str)
        print_int(num_int)
    else:
        print("Ошибка: Некорректный ввод.")