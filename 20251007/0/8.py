def bin(a,b):
    maxlenbin = len(bin(b))
    maxlenhex = len(hex(b))
for i in range(a,b+1):
    print(f:{i:<#{bw}b} = {i:#{hw}x}")