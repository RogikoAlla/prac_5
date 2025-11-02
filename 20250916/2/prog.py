total = 0

while True:
    num = int(input())
    if num <= 0:
        print(num)
        break
    total += num
    if total > 21:
        print(total)
        break