class A:
    v = 1
    
    
class B(A):
    v = 2
    
print(b.v)
del b.v
del B.v
print(b.v)