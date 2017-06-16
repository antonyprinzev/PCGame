﻿'''
Вы можете вспомнить хоть одного своего знакомого до двадцатилетнего возраста, который в детстве не играл в компьютерные
игры? Если да, то может быть вы и сами не знакомы с этим развлечением? Впрочем, трудностей при решении этой задачи это 
создать не должно.

Во многих старых играх с двумерной графикой можно столкнуться с подобной ситуацией. Какой-нибудь герой прыгает по
платформам (или островкам), которые висят в воздухе. Он должен перебраться от одного края экрана до другого. При этом
при прыжке с одной платформы на соседнюю, у героя уходит |y2-y1| единиц энергии, где y1 и y2 – высоты, на которых 
расположены эти платформы. Кроме того, у героя есть суперприем, который позволяет перескочить через платформу, но на
это затрачивается 3*|y3-y1| единиц энергии. Конечно же, энергию следует расходовать максимально экономно.

Предположим, что вам известны координаты всех платформ в порядке от левого края до правого. Сможете ли вы найти, какое
минимальное количество энергии потребуется герою, чтобы добраться с первой платформы до последней?

Входные данные

В первой строке входного файла INPUT.TXT записано количество платформ n (1 ≤ n ≤ 30000). Вторая строка содержит n 
натуральных чисел, не превосходящих 30000 – высоты, на которых располагаются платформы.

Выходные данные

В выходной файл OUTPUT.TXT запишите единственное число – минимальное количество энергии, которую должен потратить игрок 
на преодоление платформ (конечно же в предположении, что cheat-коды использовать нельзя).
'''


# входные данные
f = open('input.txt', 'r')

# преобразую 1 строку (количество платформ) в число
n = int(f.readline())

# 2 строка файла (платформы); удаляю в платформах ненужные пробелы
platforms = f.readline()

# закрываю файл, дабы не нагружать систему
f.close()

# преобразую платформы в числа
platforms = list(map(int, platforms.split()))

# просто проверка
print(n)
print(platforms)
print(platforms[0]+platforms[2])

# TODO завершить программу