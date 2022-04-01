import sys

num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())

#num2 의 자릿수 구하기
a = num2 // 100                           # 백의 자리
b = (num2 - (a * 100)) // 10              # 십의 자리
c = (num2 - (a * 100) - (b * 10) ) // 1   # 일의 자리

print(num1 * c)
print(num1 * b)
print(num1 * a)
print(num1 * num2)