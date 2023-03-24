# 9085
T = int(input())
for t in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(sum(numbers))

# 10824
A, B, C, D = input().split()
print(int(A + B) + int(C + D))

# 3009 list
x_list = []
y_list = []
for i in range(3):
    x, y = list(map(int, input().split()))
    x_list.append(x)
    y_list.append(y)

for i in range(3):
    if x_list.count(x_list[i]) == 1:
        X = x_list[i]
    if y_list.count(y_list[i]) == 1:
        Y = y_list[i]
print(X, Y)

# 3009 dictionary
x = {}
y = {}

for i in range(3):
    a, b = map(int, input().split())

    if a not in x:
        x[a] = 1
    else:
        x[a] += 1

    if b not in y:
        y[b] = 1
    else:
        y[b] += 1

for i in x:
    if x.get(i) != 2:
        print(i, end=" ")

for i in y:
    if y.get(i) != 2:
        print(i)

# 10952
while True:
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        break
    print(a + b)

# 1110  string으로 풀기
N = input()
tmp = N
cnt = 0
while True:
    if len(N) == 1:
        tmp = "0" + N
        N_1 = N
    else:
        N_1 = str(int(N[0]) + int(N[1]))
    N = N[-1:] + str(N_1[-1:])
    cnt += 1
    if N == tmp:
        break
print(cnt) 

# 1110 string으로 풀기 2
N = input()
tmp = N
if len(N) == 1:
    N = "0" + N
cnt = 0
while True:
    N_1 = str(int(N[0]) + int(N[1]))
    N = N[-1:] + str(N_1[-1:])
    cnt += 1
    if int(N) == int(tmp):
        break
print(cnt)

# 1110  int로 풀기
N = int(input())
tmp = N
cnt = 0
while True:
    N_1 = N // 10 + N % 10
    N_2 = (N % 10) * 10  + N_1 % 10
    cnt += 1

    N = N_2
    if N == tmp:
        break
print(cnt)   