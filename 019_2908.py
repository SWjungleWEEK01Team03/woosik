import sys

a, b = map(str, sys.stdin.readline().split())

reverseA = int(a[::-1])
reverseB = int(b[::-1])

if reverseA>reverseB:
    print(reverseA)
else:
    print(reverseB)

# import sys

# a, b = list(map(str, sys.stdin.readline().split()))

# a = a[::-1]
# b = b[::-1]

# print(type(a))
# print(type(b))