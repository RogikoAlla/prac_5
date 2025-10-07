from math import sin

def scale(a,b,A,B,x)
    return (x-a) * (B-A) / (b-a) + A
    
def out(screen)
    print ("\n".join("".join(line) for line in screen))
    
w,h = eval(input())
a , b = eval(input())
for line in range(0,h):
    x = scale(0,w-1,a,b,i)
    y = sin (x)
    k = round(scale(-1, 1,0.w-1,y)
    screen[h-k-1][i] = "*"
out(screen)   