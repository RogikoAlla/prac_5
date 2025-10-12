from fractions import Fraction

def check_solution(s, w, *coeffs):
    # Извлекаем степени и коэффициенты
    deg_A = int(coeffs[0])
    coeffs_A = [Fraction(str(x)) for x in coeffs[1:1+deg_A+1]]
    deg_B = int(coeffs[1+deg_A+1])
    coeffs_B = [Fraction(str(x)) for x in coeffs[2+deg_A+1:2+deg_A+1+deg_B+1]]
    
    # Преобразуем s и w в Fraction
    s = Fraction(str(s))
    w = Fraction(str(w))
    
    # Вычисляем A(s) и B(s)
    A_s = sum(coeffs_A[i] * (s ** (deg_A - i)) for i in range(deg_A + 1))
    B_s = sum(coeffs_B[i] * (s ** (deg_B - i)) for i in range(deg_B + 1))
    
    # Проверяем уравнение A(s)/B(s) = w
    if B_s == 0:
        return False
    return A_s / B_s == w

# Ввод и вывод
data = eval(input())
print(check_solution(*data))