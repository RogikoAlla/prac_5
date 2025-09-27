numbers = list(map(int, input().split(',')))
n = len(numbers)

for i in range(n):
    for j in range(0, n-i-1):
        if (numbers[j]**2 % 100) > (numbers[j+1]**2 % 100):
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)