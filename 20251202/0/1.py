def meet(n):
    for i in range(n):
        yield f'{i}: Hello'
    return f'You{3}: bue'

def meeting(m):
    for i in range(m):

        res = yield from meet(3)
        yield f'<{i}>:{res}'
    return 'fin'

