#10817
import heapq

num = list(map(int, input().split()))  
heapq.heapify(num)
heapq.heappop(num)  
print(heapq.heappop(num))

# 200001
from collections import deque

problem = deque([])
while True:
    string = input()
    if string == "문제":
        problem.append("1")
    if len(problem) > 0 and string == "고무오리":
        problem.popleft()
    elif string == "고무오리":
        problem.append("1")
        problem.append("1")
    if string == "고무오리 디버깅 끝":
        break
if len(problem) == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")

# 1269
a, b = list(map(int, input().split()))
a_ = set(list(map(int, input().split())))
b_ = set(list(map(int, input().split())))
print(len(a_ ^ b_))

# 3052
num_list = []
for _ in range(10):
    num = int(input())
    num_list.append(num % 42)
print(len(set(num_list)))

# 1181
num = int(input())
words = []

for _ in range(num):
    word = input().strip()

    if word not in words:
        words.append(word)


words = sorted(words)
words = sorted(words, key=len)

print(*words, sep="\n")

# 1181
N = int(input())
str_list = []
list_sort = []

for i in range(N):
    str_list.append(input())

list_set = list(set(str_list))

for j in list_set:
    list_sort.append((len(j), j))

result = sorted(list_sort)

for length, word in result:
    print(word)


# 11286
import heapq

negative_heap = []
positive_heap = []
n = int(input())
for i in range(n):
	num = int(input()())
	if num > 0: 
		heapq.heappush(negative_heap, num) 
	elif num < 0: 
		heapq.heappush(positive_heap, -num) 
	else:
		if negative_heap: 
			if positive_heap: 
				if negative_heap[0] < positive_heap[0]: 
					print(heapq.heappop(negative_heap)) 
				else: 
					print(-heapq.heappop(positive_heap)) 
			else: 
				print(heapq.heappop(negative_heap)) 
		elif positive_heap: 
			print(-heapq.heappop(positive_heap)) 
		else: 
			print(0)

# 11286
import sys   # ----- 정답
import heapq

N = int(input())
num_list = []

for i in range(N):
    num = int(sys.stdin.readline().rstrip())

    if num != 0:
        heapq.heappush(num_list, (abs(num), num))
    else:
        if not num_list:
            print(0)
        else:
            print(heapq.heappop(num_list)[1])