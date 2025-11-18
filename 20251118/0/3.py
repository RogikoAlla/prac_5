import sys
with open(sys.argv[1],'br')
with open('file3', 'wb') as file:
    d = file.read()
          print(*d[len(d)//2:],*d[:len(d)//2])

