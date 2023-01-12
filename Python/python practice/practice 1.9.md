```python
#1
number = int(input("문자열을 입력하세요 >"))
print(number)

#2
a, b = list(map(int, input("문자열을 입력하세요 >").split()))
print(a, b)  # 2 5

#x = input().split()
#type(x)  # list
#print(x)  # ['2', '5']

#x = list(map(int, input().split()))
#print(x)  # [2, 5]

#3
a, b, c = list(map(int, input("문자열을 입력하세요 >").split()))
print(a, b, c)

#4
a, b, c = list(input("문자열을 입력하세요 >").split())
print(a, b, c)

#5
num = list(map(int, input("문자열을 입력하세요 >").split()))   # list 없어도 됨.
for i in num:                           # num 자리에 map형식이 들어갈 수 있다.
    print(i, end=" ")

#6
a, b = list(map(int, input().split()))
print(a, b)

#7
num = input().split()
for i in num:                         
    print(i, end=" ")

#8
num = map(int, input().split())
for i in num:                         
    print(i, end=" ")

#9
num = map(int, input().split())
for i in num:                         
    print(i, end=" ")
````