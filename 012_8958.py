from posixpath import lexists
import sys

# n 시행 횟수
n = int(sys.stdin.readline())

for _ in range(n):
    # 입력받는 list
    li = list(sys.stdin.readline())
    # O 가 연속으로 나올 때마다 +1 씩 해줄 값
    score = 0 
    # score 합해줄 변수
    scoresum = 0
    for i in li:
        if i == 'O':
            score = score + 1
            scoresum = scoresum + score
        else:
            score = 0
    print(scoresum)