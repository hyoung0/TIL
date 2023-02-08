# 10101
a = int(input())
b = int(input())
c = int(input())
if a == b == c == 60:
    print("Equilateral")   
elif a + b + c == 180 and (a == b or a == c or b == c):
    print("Isosceles")
elif a + b + c == 180 and a != b != c:
    print("Scalene")
elif a + b + c != 180:
    print("Error") 

# 2720
T = int(input())
for t in range(T):
    money = int(input())
    print(money // 25, money % 25 // 10, money % 25 % 10 // 5, money % 25 % 10 % 5 // 1)

# 1453
N = int(input())
number_list = []
numbers = list(map(int, input().split()))
cnt = 0
for number in numbers:
    if number not in number_list:
        number_list.append(number)
    else:
        cnt += 1
print(cnt)

# 10773
K = int(input())
num_list = []
for k in range(K):
    num = int(input())
    if num == 0:
        num_list.pop()
    else:
        num_list.append(num)
print(sum(num_list))

# 2161
N = int(input())
num_list = [i for i in range(1, N + 1)]
# num_list = list(range(1, N + 1))
result_list = []
while len(num_list) > 1: 
    result_list.append(num_list.pop(0))
    num_list.append(num_list.pop(0))
print(*result_list, num_list[0])

# 2161 deque사용
from collections import deque

N = int(input())
num_list = deque(list(range(1, N + 1)))
result_list = []
while len(num_list) > 1: 
    result_list.append(num_list.popleft())
    num_list.append(num_list.popleft())
print(*result_list, num_list.popleft())


# 9012
# (1) for-else문 사용의 의미. (2)가 정답이고 비교해보자.
T = int(input())
for t in range(T):
    strings = input()
    stack = []
    for string in strings:
        if string == "(":
            stack.append(string)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                break
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")

# (2) 이게 정답
T = int(input())
for t in range(T):
    strings = input()
    stack = []
    for string in strings:
        if string == "(":
            stack.append(string)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                break
    # for-else문은 for에서 break로 중단되지 않으면 else실행. 
    # break로 중단되면 else실행 안 함
    else:
        if len(stack) == 0:   
            print("YES")
        else:
            print("NO")
