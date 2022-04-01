import sys

# test case
t_case = int(sys.stdin.readline())

for i in range(t_case):
    a = list(map(int, sys.stdin.readline().split()))
    average = sum(a[1:]) / a[0]

    count = 0
    for j in a[1:]:
        if j>average:
            count = count + 1
    rate = count / a[0] * 100

    print(f'{rate:.3f}%')