import sys

x, y, w, h = map(int, sys.stdin.readline().split())

w = w - x
h = h - y

if x > w:
    x = w
if y > h:
    y = h

if x > y:
    print(y)
else:
    print(x)