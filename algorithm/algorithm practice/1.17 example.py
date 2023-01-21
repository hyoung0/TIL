# 10818
N = int(input())
numbers = list(map(int, input().split()))
print(min(numbers), max(numbers), end=" ")

# 11720
N = int(input())
numbers = input()
result = 0
for number in numbers:
    result += int(number)
print(result)

# 2750
N = int(input())
num_list = []
for n in range(N):
    number = int(input())
    num_list.append(number)

num_list.sort()
for num in num_list:
    print(num)

# 2562
numbers = []
for i in range(9):
    num = int(input())
    numbers.append(num)
n_max = max(numbers)
print(n_max, numbers.index(n_max) + 1, sep="\n")