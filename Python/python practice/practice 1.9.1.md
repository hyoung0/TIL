```python
#1
string = input("문자열을 입력하세요 > ")
for i in range(len(string)):
    if string[i] == "e":
        print(i)
        break
else:
    print(-1)

#2
strings = input("문자열을 입력하세요 > ").split()
dict = {}
for string in strings:
    if string not in dict:
        dict[string] = 1
    else:
        dict[string] += 1
for key, value in dict.items():
    print(key, value)

#3
string = input("문자열을 입력하세요 > ")
new = []
for i in string:
    if i != "e":
        new.append(i)
result = ""
for j in new:
    result += j
print(result)

#4
a, b = input("문자열을 입력하세요 > ").split()
cnt = 0
for a_ in a:
    if a_ == b:
        cnt += 1
print(cnt)

#5
a, b, c = input("문자열을 입력하세요 > ").split()
print(a + "-" + b + "-" + c)

#6
num = int(input("양의 정수를 입력하세요 > "))
if num < 0:
    print(-1)
else:
    i = 1
    num1 = 0
    while (num / (10 ** i)) > 0:
        num1 += num % (10 ** i) // (10 ** (i-1))
        i += 1
    print(num1)

#6-1
n = int(input())
result = 0
while n > 0:
    result += n%10
    n //= 10
print(result)
```
