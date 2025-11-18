import sys

with open('a','w+') as file:
    print('привет друкг, \n  Я = ты', file = file)

with open ('a', 'r+') as file:
    d = file.readlines()
    print(*sorted(d), file = file)


