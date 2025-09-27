M, N = map(int, input().split(','))
print([x for x in range(M, N) if all(x % i != 0 for i in range(2, int(x**0.5)+1)) and x > 1])