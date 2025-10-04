from math import *

def Calc(s, t, u):
    def func(x):
        s_val = eval(s, globals(), {'x': x})
        t_val = eval(t, globals(), {'x': x})
        return eval(u, globals(), {'x': s_val, 'y': t_val})
    return func

# Ввод и вывод
s, t, u = eval(input())
x = eval(input())
F = Calc(s, t, u)
print(F(x))