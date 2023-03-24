# 2525
h, m = list(map(int, input().split()))
time = int(input())

if m + time < 60:
    h = h
    m = m + time
elif m + time >= 60:
    h = h + (m+time) // 60
    m = (m + time) % 60
if h >= 24:
    h = h - 24
print(h, m)

# 2798
N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))
total_list = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            total = nums[i] + nums[j] + nums[k]
            if total <= M:
                total_list.append(total)
print(max(total_list))

# 9076
T = int(input())
for t in range(T):
    scores = list(map(int, input().split()))
    scores = sorted(scores)
    scores.pop(0)
    scores.pop(3)
    if scores[2] - scores[0] >= 4:
        print("KIN")
    else:
        print(sum(scores))

# 1526 
N = list(range(4, int(input()) + 1))

num = []
for n in N:
    cnt = 0
    for i in str(n):
        if i == '4' or i == '7':
            cnt += 1
    if cnt == len(str(n)):
        num.append(n)
print(max(num))

# 1526 
num = int(input())
N = list(range(4, num + 1))
tmp = list(range(4, num + 1))
for n in N:
    for i in str(n):
        if i != '4' and i != '7':
            tmp.remove(n)
            break
print(max(tmp))

# 1436
N = int(input())
string = '666'
cnt = 0
n = 666

while True:
    if string in str(n):
        cnt += 1
    if cnt == N:
        print(n)
        break    
    n += 1