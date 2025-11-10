def itemget(collection, index):
    return collection[index]
    
def safeindex(func, *args):
    try:
    return func(*args)
    except IndexError
        rerturn None