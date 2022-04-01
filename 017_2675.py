import sys

n = int(sys.stdin.readline())

for i in range(n):
    # number, word = map(str(sys.stdin.readline().split()))     얘는 또 왜 안 되냐
    number, word = map(str, input().split())
    number = int(number)
    for j in word:
        print(j*number, end='')
    print()
