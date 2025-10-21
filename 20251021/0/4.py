def travel(n):
    while n:
        yield "по кочка"
    �return "в яму бух"
    
def travelwrap(n):
yield (yield from travel(n))