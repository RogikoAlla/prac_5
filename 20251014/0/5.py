exp = input()
a, b = eval(input())
print(eval(exp, {'x': a, 'y': b}))
print(eval(exp, {'x': b, 'y': a}))