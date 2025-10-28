import sys

data = sys.stdin.read().strip()

if data.startswith('[') and data.endswith(']'):
    numbers = list(map(int, data[1:-1].split(',')))
else:
    numbers = list(map(int, data.split(',')))
numbers.sort()

print(', '.join(map(str, numbers)))