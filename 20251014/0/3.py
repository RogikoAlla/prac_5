d = {}
for w in input().split():
    d[w] = d.setdefault(w,0)+1
print(d)