# 10039
원섭 = int(input())
세희 = int(input())
상근 = int(input())
숭 = int(input())
강수 = int(input())
list = [원섭, 세희, 상근, 숭, 강수]

total = 0
for i in list:
    if i >= 40 :
        i = i
    else:
        i = 40
    total += i
print(int(total / len(list)))

# 10871
N, X = map(int, input().split())
n = list(map(int, input().split()))
for i in n:
    if i < X:
        print(i, end=" ")

# 2480
a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c:
    print(1000 + a * 100)
elif b == c :
    print(1000 + b * 100)
elif a != b != c:
    print(max(a, b, c) * 100)

# 10886
N = int(input())
cnt_cute = 0
cnt_no = 0

for n in range(N):
    op = int(input())
    if op == 1:
        cnt_cute += 1
    else:
        cnt_no += 1
if cnt_cute > cnt_no:
    print("Junhee is cute!")
else:
    print( "Junhee is not cute!")
    
# 2506
N = int(input())
answer = map(int, input().split())

cnt = 0
list = []
for i in answer:
    if i == 1:
        list.append(i)
        len(list) * 1
        cnt += len(list)
    else:
        list = []
print(cnt)
