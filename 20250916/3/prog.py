n = int(input())

i = 0
while i < 3:
    a = n + i
    
    j = 0
    while j < 3:
        b = n + j
        product = a * b
        
        # Проверяем, равна ли сумма цифр 6 (без использования строк)
        temp = product
        digit_sum = 0
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
        
        if digit_sum == 6:
            result = ":=)"
        else:
            # Формируем результат без format()
            result = str(product)
        
        # Выводим без форматирования столбцов
        if j > 0:
            print(" ", end="")
        print(f"{a} * {b} = {result}", end="")
        
        j += 1
    
    print()  # Переход на новую строку
    i += 1