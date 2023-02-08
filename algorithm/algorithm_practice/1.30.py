# 1225 정답

# num = list(input().split())
# matrix = []
# for i in num:
#     matrix.append(list(i))
# print(matrix)
matrix = [list(i) for i in list(input().split())] 
# a = 123
# print(list(a))   # 에러 발생 [1,2,3]이 되지 않는다. 숫자형은 list할 수 없다.

num1 = sum(list(map(int, matrix[0])))
num2 = sum(list(map(int, matrix[1])))
print(num1 * num2)

# 1225 시간초과
matrix = [list(i) for i in list(input().split())]
result = 0
for j in range(len(matrix[0])):
    for i in range(len(matrix[1])):
        first = int(matrix[0][j]) * int(matrix[1][i])
        result += first
print(result)

# 2438
N = int(input())

for n in range(1, N + 1):
    print("*" * n)

# 2438
N = int(input())
star_list = [print("*" * n) for n in range(1, N + 1)]

# 2739
n = int(input())

for i in range(1, 10):
    print(f'{n} * {i} = {n * i}')

# 2953
matrix = [list(map(int, input().split())) for _ in range(5)]
sum_matrix = [sum(score) for score in matrix]
print(sum_matrix.index(max(sum_matrix)) + 1, max(sum_matrix))

# 2669
matrix = [[0] * 100 for _ in range(100 + 1)]

cnt = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    
    for a in range(x1, x2): 
        for b in range(y1, y2):
            if matrix[a][b] == 0:
                matrix[a][b] += 1
                cnt += 1

print(cnt)