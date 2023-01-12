```python
#1
num = int(input("정수를 출력하세요\n"))
print(num)

#2
string = input("단어를 구분해서 출력하세요\n").split()
for i in string:
    print(i, end="")

#3
string = input("테스트 케이스마다 입력 값을 그대로 출력하세요\n")
for i in range(int(string)):
    print(input())

#4
num = map(int, input("2개 이상의 정수를 출력하세요\n").split())
for i in num:
    print(i, end="")

#5
a, b = map(int, input("2개의 정수를 출력하세요\n").split())
print(a, b)

#6
a, b, c = input("단어를 구분해서 출력하세요\n").split()
print(a, b, c)

#7
string = int(input("테스트 케이스마다 입력 값을 그대로 출력하세요\n"))
for t in range(string):
    numbers = map(int, input().split())
    print(numbers)

#8
string = int(input("테스트 케이스마다 입력 값을 그대로 출력하세요\n"))
for t in range(string):
    numbers = map(int, input().split())
    print(numbers)
```