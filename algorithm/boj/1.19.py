# 2576
odd = []
for i in range(7):
    num = int(input())
    if num % 2 == 1:
        odd.append(num)
if odd == []:
    print(-1)
else:
    print(sum(odd))
    print(min(odd))

# 10822
S = list(map(int, input().split(",")))
print(sum(S))

# 2754
score = input()
score_dict = {"A+":4.3, "A0":4.0,"A-":3.7,
"B+":3.3, "B0":3.0,"B-":2.7, "C+":2.3, "C0":2.0,"C-":1.7, 
"D+":1.3, "D0":1.0,"D-":0.7, "F":0.0}
print(score_dict[score])

# 5622  dictionay로 풀기
string = input()
num_dict = {"A":2, "B":2, "C":2, "D":3, "E":3, "F":3, "G":4, "H":4, "I":4,
         "J":5, "K":5, "L":5, "M":6, "N":6, "O":6, "P":7, "Q":7, "R":7, "S":7,
         "T":8, "U":8, "V":8, "W":9, "X":9, "Y":9, "Z":9} 
cnt = 0
for alpha in string:
    cnt += num_dict[alpha]
print(cnt + len(string))

# 5622   list로 풀기
cnt = 0
string = input()
alpha_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
for i in string:
    for j in range(len(alpha_list)):
        if i in alpha_list[j]:
            num = j + 2
            cnt += num
print(cnt + len(string))

# 2577
A = int(input())
B = int(input())
C = int(input())
num = str(A * B * C)
for i in range(10):
    print(num.count(str(i)))

# 7785
N = int(input())
record_dict = {}
for n in range(N):
    name, record = input().split()
    if record == "enter":
        record_dict[name] = record
    else:
        record_dict.pop(name)

record_dict = sorted(record_dict.keys(), reverse = True)

for i in record_dict:
    print(i)