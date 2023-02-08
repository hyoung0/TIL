# 1547
ball_list = [1, 0, 0]
M = int(input())
for _ in range(M):
    x, y = list(map(int, input().split()))
    tmp = ball_list[x-1]
    ball_list[x-1] = ball_list[y-1]
    ball_list[y-1] = tmp
print(ball_list.index(1) + 1)

# 5576
W = []
K = []
for _ in range(10):
    w = int(input())
    W.append(w)
for _ in range(10):
    k = int(input())
    K.append(k)
w_sorted = sorted(W)[-3:]
k_sorted = sorted(K)[-3:]
print(sum(w_sorted), sum(k_sorted))

# 2846
N = int(input())
load = list(map(int, input().split()))
tmp = [] 
uphill = []  

for i in load:
    if tmp == []:
        tmp.append(i)
    elif i > tmp[-1]:
        tmp.append(i)
    else:
        if len(tmp) > 1:
            uphill.append(tmp[-1] - tmp[0])
        tmp = []
        tmp.append(i)
if len(tmp) > 1:
    uphill.append(tmp[-1] - tmp[0])

if uphill == []:
    print(0)
else:
    print(max(uphill))

# 1251
string = input()
re_ls = []
for i in range(1, len(string) - 1):
    for j in range(i + 1, len(string)):
        re = string[:i][::-1] + string[i:j][::-1] + string[j:][::-1]
        re_ls.append(re)
print(sorted(re_ls)[0])
