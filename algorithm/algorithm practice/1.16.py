# 1000
a, b = map(int, input().split())
print(a + b)

#2558
a = int(input())
b = int(input())
print(a + b)

# 10950
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(a + b)

# 10953
T = int(input())

for i in range(T):
    a, b = map(int, input().split(","))
    print(a + b)

# 11021
T = int(input())

for t in range(1, T + 1):
    a, b = map(int, input().split())
    print(f'Case #{t}: {a + b}')

# 11022
T = int(input())

for t in range(1, T + 1):
    a, b = map(int, input().split())
    print(f'Case #{t}: {a} + {b} = {a + b}')
