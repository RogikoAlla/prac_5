def subtract(a, b):
    if isinstance(a, (list, tuple)):
        result = []
        for item in a:
            if item not in b:
                result.append(item)
        return type(a)(result)
    else:
        return a - b

# Ввод и вывод
a, b = eval(input())
print(subtract(a, b))