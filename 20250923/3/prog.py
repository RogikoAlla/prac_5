# Чтение первой матрицы
matrix1 = []
line = list(map(int, input().split(',')))
matrix1.append(line)
n = len(line)
for i in range(n-1):
    line = list(map(int, input().split(',')))
    matrix1.append(line)

# Чтение второй матрицы  
matrix2 = []
for i in range(n):
    line = input()
    matrix2.append(list(map(int, line.split(','))))

# Умножение матриц
result = []
for i in range(n):
    row = []
    for j in range(n):
        sum_val = 0
        for k in range(n):
            sum_val += matrix1[i][k] * matrix2[k][j]
        row.append(sum_val)
    result.append(row)

# Вывод результата
for i in range(n):
    print(','.join(map(str, result[i])))