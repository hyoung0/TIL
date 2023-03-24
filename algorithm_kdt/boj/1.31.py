# 2441
N = int(input())
for n in range(0, N + 1):
  print(" "*n + "*"*(N - n))

# 2592
num = [int(input()) for i in range(10)]

avg = sum(num) / len(num)
print(int(avg))

for i in range(len(num)):
    num[i] = (num[i], num.count(num[i]))
print(max(num, key = lambda x:x[1])[0])   
# 튜플 따로 만들 필요 없이 max(num, key = num.count)로 바로 가능

# 2592
from collections import Counter
N = []
max = 0
for i in range(10):
    N.append(int(input()))
how_many = sorted(dict(Counter(N)).items(), key=lambda x: x[1])

print(int(sum(N)/10), how_many[-1][0], sep="\n")

# 2592
from collections import Counter   # ----- 함수 사용
ave = 0
N_list = []

for i in range(10):
    N = int(input())
    N_list.append(N)
    ave += N

cnt = Counter(N_list)
result = cnt.most_common(1)

print(ave//10)
print(result[0][0])

# 10798
matrix = []
for i in range(5):
    string = list(input())
    if len(string) != 15:
        string += [""] * (15 - len(string))
    matrix.append(string)
        
new = [[""] * 5 for _ in range(15)]

for i in range(15):
    for j in range(5):
        new[i][j] = matrix[j][i]

for i in new:
    print(''.join(i), end='')

# 10798
words = []
for _ in range(5):
    words.append(list(map(str, input())))

max_len = len(sorted(words, key=len)[-1])

for i in range(5):
    for _ in range(max_len-len(words[i])):
        words[i].append('')

for i in range(max_len):
    for j in range(5):
        print(words[j][i], end="")

# 9455
import pprint

T = int(input())
for t in range(T):
    cnt = 0
    result = 0
    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    new = [[0]*5 for _ in range(M)]
    for i in range(M):
        for j in range(N):
            new[i][j] = matrix[j][i]
    
    for i in range(M):
        for j in range(N):
            if new[i][-j-1] == 1:
                pass
            elif 1 not in new[i][:-j-1]:
                pass
            else:
                cnt += 1
                result += cnt

# 1652
N = int(input())
matrix = [list(input()) for _ in range(N)]

cnt = 0
for i in range(N):
    length = 0
    for j in range(N):
        if matrix[i][j] == ".":
            length += 1
        if matrix[i][j] == "X" or j == N-1:
            if length >= 2:
                cnt += 1
            length = 0

cnt2 = 0
for i in range(N):
    length = 0
    for j in range(N):
        if matrix[j][i] == ".":
            length += 1
        if matrix[j][i] == "X" or j == N-1:
            if length >= 2:
                cnt2 += 1
            length = 0
print(cnt, cnt2)
