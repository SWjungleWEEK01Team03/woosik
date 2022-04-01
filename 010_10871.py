import sys

# a는 몇개의 숫자를 받을것이냐, b는 b보다 작은 수 뽑기
a, b = map(int, sys.stdin.readline().split())
c = list(map(int, sys.stdin.readline().split()))

for i in range(a):
    if c[i]<b:
        print(c[i], end=' ')