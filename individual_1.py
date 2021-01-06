#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решить индивидуальное задание лабораторной работы 6, оформив каждую команду в виде
# отдельной функции.

# Условие индивидуального задания ЛР-6:
# Использовать словарь, содержащий следующие ключи:
# название пункта назначения рейса;
# номер рейса;
# тип самолета.
# Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть упорядочены по возрастанию номера рейса;
# вывод на экран номеров рейсов и типов самолетов, вылетающих в пункт назначения, название которого совпало с названием,введенным с клавиатуры;
# если таких рейсов нет, выдать на дисплей соответствующее сообщение.

import sys


def add(flights, num, typ, place):
    # Создать словарь.
    flight = {
        'num': num,
        'typ': typ,
        'place': place,
    }

    # Добавить словарь в список.
    flights.append(flight)
    # Отсортировать список в случае необходимости.
    if len(flights) > 1:
        flights.sort(key=lambda item: item.get('num', ''))


def list(flights):
    table = []
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 25
    )
    table.append(line)
    table.append(
        '| {:^4} | {:^30} | {:^20} | {:^25} |'.format(
            "№",
            "Номер рейса? ",
            "Тип самолёта? ",
            "Пункт назначения рейса? "
        )
    )
    table.append(line)

    # Вывести данные о всех сотрудниках.
    for idx, flight in enumerate(flights, 1):
        table.append(
            '| {:>4} | {:<30} | {:<20} | {:<25} |'.format(
                idx,
                flight.get('num', 0),
                flight.get('typ', ''),
                flight.get('place', '')
            )
        )

    table.append(line)

    return '\n'.join(table)


def select(flights, plane):

    # Инициализировать результат.
    result = []
    # Проверить сведения работников из списка.
    for flight in flights:
        if plane == flight.get('place'):
            result.append(flight)

    return result


if __name__ == '__main__':
    # Список работников.
    flights = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ")

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о рейсе.
            num = int(input("Номер рейса? "))
            typ = (input("Тип самолёта? "))
            place = input("Пункт назначения рейса? ")

            add(flights, num, typ, place)

        elif command == 'list':
            print(list(flights))

        elif command.startswith('select '):
            # Разбить команду на части для выделения номера года.
            plane = command.split(maxsplit=1)
            # Получить список работников.
            selected = select(flights, plane[1])
            count = 0
            # Вывод списка работников.
            if selected:
                for idx, flight in enumerate(selected, 1):
                    print(
                        '{:>4}: Номер самолёта - {}, Тип самолёта - {}'.format(count, flight.get('num', ''), flight.get('typ', ''))
                    )
            else:
                print("Таких пунктов назначения не найдено.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить рейс;")
            print("list - вывести список рейсов;")
            print("select <Пункт назначения рейса> - запросить нужный рейс;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)