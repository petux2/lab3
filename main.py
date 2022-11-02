import itertools
i1 = {"и": (1, 5),
        "н": (1, 15),
        "о": (1, 25),
        "ф": (1, 15),
        "д": (1, 10)}
i2 = {"п": (2, 15),
        "б": (2, 15),
        "а": (2, 20),
        "к": (2, 20),
        "р": (2, 20)}
i3 = {"в": (3, 25),
        "т": (3, 20)}

items = [{"и": (1, 5),
        "н": (1, 15),
        "о": (1, 25),
        "ф": (1, 15),
        "д": (1, 10)},
    {"п": (2, 15),
        "б": (2, 15),
        "а": (2, 20),
        "к": (2, 20),
        "р": (2, 20)},
    {"в": (3, 25),
        "т": (3, 20)}]

patterns0 = [[3, 3, 3],
            [3, 3, (2, 1)],
            [3, 3, (1, 1, 1)],
            [3, (2, 1), (2, 1)],
            [3, (2, 1), (1, 1, 1)],
            [3, (1, 1, 1), (1, 1, 1)],
            [(2, 1), (2, 1), (2, 1)],
            [(2, 1), (2, 1), (1, 1, 1)],
            [(2, 1), (1, 1, 1), (1, 1, 1)],
            [(1, 1, 1), (1, 1, 1), (1, 1, 1)]]

patterns = [[3, 3, (2, 1)],
            [3, 3, (1, 1, 1)],
            [3, (2, 1), (2, 1)],
            [3, (2, 1), (1, 1, 1)],
            [(2, 1), (2, 1), (2, 1)],
            [(2, 1), (2, 1), (1, 1, 1)]]

for i in patterns:
    a = [[0 for j in range(3)] for k in range(3)]
    value = -sum(sum(k[1] for k in list(items[j].values())) for j in range(3))
    print(value)



# items = {"в": (3, 25),
#         "п": (2, 15),
#         "б": (2, 15),
#         "а": (2, 20),
#         "и": (1, 5),
#         "н": (1, 15),
#         "т": (3, 20),
#         "о": (1, 25),
#         "ф": (1, 15),
#         "д": (1, 10),
#         "к": (2, 20),
#         "р": (2, 20)}
#
# value = sum(-i[1] for i in list(items.values()))
# a = [[0 for i in range(3)] for i in range(3)]
# items = dict(sorted(items.items(), key=lambda item: item[1]))
#
# items_ = dict(sorted(items.items(), key=lambda item: item[1][1]/item[1][0]))
# items__ = [i[1]/i[0] for i in list(items.values())]
# print(items)
# print(items_)
# print(items__)
# print(value)
#
# def f(itemsf):
#         a = [[0 for i in range(3)] for j in range(3)]
#         for i in range(3):
#                 for j in range(3):
#                         1
#         return a
a = [2, (3, 4), 1, 1]
for i in a:
    print(1 if type(i) is int else len(i))
