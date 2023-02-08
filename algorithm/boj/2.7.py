# 17608
import sys

n = int(sys.stdin.readline())
h_ls = []
for _ in range(n):
    h = int(sys.stdin.readline())
    h_ls.append(h)

standard = h_ls[-1]
cnt = 0
for elem in h_ls[::-1]:
    if elem > standard:
        cnt += 1
        standard = elem

print(cnt + 1)

# 7568
N = int(input())
people = []
rank = 1
rank_ls = []
for _ in range(N):
    x, y = map(int, input().split())
    people.append((x, y))
# print(people)

for person in people:
    for j in people:
        if person[0] < j[0] and person[1] < j[1]:
            rank += 1
    rank_ls.append(rank)
    rank = 1
print(*rank_ls)

# 1063
import pprint
move_ls = {'R': (0, 1),
'L' : (0, -1),
'B' : (1, 0),
'T' : (-1, 0),
'RT' : (-1, 1),
'LT' : (-1, -1),
'RB' : (1, 1),
'LB' : (1, -1)}

matrix = [[0]*8 for _ in range(8)]
king, stone, N = input().split()
# 킹 위치
k_column = 'ABCDEFGH'.index(king[0])  
k_row = '87654321'.index(king[1])
matrix[k_row][k_column] = 'k'
# 돌 위치
s_column = 'ABCDEFGH'.index(stone[0])
s_row = '87654321'.index(stone[1])
matrix[s_row][s_column] = 's'

# pprint.pprint(matrix)
for _ in range(int(N)):
    move = input()
    dx = move_ls[move][0]
    dy = move_ls[move][1]
    if k_row + dx not in range(8) or k_column + dy not in range(8):
        continue
    if matrix[k_row + dx][k_column + dy] == matrix[s_row][s_column]: # k이 옮겨갈 자리와 s의 자리가 같을 경우
        if s_row + dx not in range(8) or s_column + dy not in range(8):
            continue    
        matrix[k_row][k_column] = 0
        matrix[k_row + dx][k_column + dy] = 'k'
        matrix[s_row + dx][s_column + dy] = 's'
        k_row = k_row + dx
        k_column = k_column + dy
        s_row = s_row + dx
        s_column = s_column + dy
    else:
        matrix[k_row][k_column] = 0
        matrix[k_row + dx][k_column + dy] = 'k'
        k_row = k_row + dx
        k_column = k_column + dy
# pprint.pprint(matrix)

for i in range(8):
    for j in range(8):
        if matrix[i][j] == 'k':
            print('ABCDEFGH'[j] + '87654321'[i])
for i in range(8):
    for j in range(8):
        if matrix[i][j] == 's':
            print('ABCDEFGH'[j] + '87654321'[i])


################################################ 1063
import pprint
move_ls = {'R': (0, 1),
'L' : (0, -1),
'B' : (1, 0),
'T' : (-1, 0),
'RT' : (-1, 1),
'LT' : (-1, -1),
'RB' : (1, 1),
'LB' : (1, -1)}

matrix = [[0]*8 for _ in range(8)]
king, stone, N = input().split()
# 킹 위치
k_column = 'ABCDEFGH'.index(king[0])  
k_row = '87654321'.index(king[1])
matrix[k_row][k_column] = 'k'
# 돌 위치
s_column = 'ABCDEFGH'.index(stone[0])
s_row = '87654321'.index(stone[1])
matrix[s_row][s_column] = 's'

# pprint.pprint(matrix)
for _ in range(int(N)):
    move = input()
    dx = move_ls[move][0]
    dy = move_ls[move][1]
    if k_row + dx not in range(8) or k_column + dy not in range(8) or s_row + dx not in range(8) or s_column + dy not in range(8):
        continue    # 이러면 틀림. s는 k와 겹칠 때만 이동해야 되는데 무조건 이동시킨 값으로 봤기 때문
    if matrix[k_row + dx][k_column + dy] == matrix[s_row][s_column]: # k이 옮겨갈 자리와 s의 자리가 같을 경우
        matrix[k_row][k_column] = 0
        matrix[k_row + dx][k_column + dy] = 'k'
        matrix[s_row + dx][s_column + dy] = 's'
        k_row = k_row + dx
        k_column = k_column + dy
        s_row = s_row + dx
        s_column = s_column + dy
        print(2)
    else:
        matrix[k_row][k_column] = 0
        matrix[k_row + dx][k_column + dy] = 'k'
        k_row = k_row + dx
        k_column = k_column + dy
        print(3)

########################
