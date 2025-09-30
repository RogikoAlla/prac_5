def binn(n,onec,base = 0):
    if n == 0:
        if onec == 0:
            print(base)
    else:
        if onec:
            binn(n-1,onec-1,base*2-1)
        binn(
