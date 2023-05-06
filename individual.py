#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Функция для ввода данных о маршрутах
def add_route(routes):
    start = input("Введите начальный пункт маршрута: ")
    end = input("Введите конечный пункт маршрута: ")
    number = input("Введите номер маршрута: ")
    route = {
        "start": start,
        "end": end,
        "number": number
    }
    routes.append(route)
    return routes


# Функция для сортировки списка маршрутов по номерам маршрутов
def sort_routes(routes):
    routes = sorted(routes, key=lambda x: x["number"])
    return routes


# Функция для вывода информации о маршруте по номеру
def find_route(routes, number):
    found = False
    for route in routes:
        if route["number"] == number:
            print("Начальный пункт маршрута:", route["start"])
            print("Конечный пункт маршрута:", route["end"])
            found = True
            break
    if not found:
        print("Маршрут с таким номером не найден.")


if __name__ == '__main__':
    # Создаем пустой список для хранения словарей
    routes = []

    # Запускаем бесконечный цикл для добавления маршрутов
    while True:
        # Добавляем маршрут в список
        routes = add_route(routes)

        # Сортируем список маршрутов по номерам маршрутов
        routes = sort_routes(routes)

        # Спрашиваем пользователя, хочет ли он добавить еще один маршрут
        choice = input("Хотите добавить еще один маршрут? (y/n): ")
        if choice.lower() == "n":
            break

    # Выводим на экран информацию о маршруте по номеру
    number = input("Введите номер маршрута для поиска: ")
    find_route(routes, number)