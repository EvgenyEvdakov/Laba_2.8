#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiply():
    result = 1
    while True:
        num = int(input("Введите число: "))
        if num == 0:
            break
        result *= num
    return result


print("Произведение введенных чисел: ", multiply())