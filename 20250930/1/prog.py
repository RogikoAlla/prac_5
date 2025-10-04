def Pareto(*pairs):
    result = []
    for i, (x1, y1) in enumerate(pairs):
        dominated = False
        for j, (x2, y2) in enumerate(pairs):
            if i != j and x2 >= x1 and y2 >= y1 and (x2 > x1 or y2 > y1):
                dominated = True
                break
        if not dominated:
            result.append((x1, y1))
    return tuple(result)

# Ввод и вывод
data = eval(input())
print(Pareto(*data))