```python
#1
num = int(input("정수를 입력하세요 > "))
if num >=0:
    print(num)
else:
    print(num * -1)

#2
number_list = [1, 2, 3, 4, 5]
i = 0
for number in number_list:
    i += 1
print(i)

number_list = []
i = 0
for number in number_list:
    i += 1
print(i)

#3 (for 사용)
number_list = [1, 2, 3, 4, 5]
total = 0
for i in number_list:
    total += i
print(total)

number_list = [-1, -2, -3, -4, -5]
total = 0
for i in number_list:
    total += i
print(total)

#3-1 (while 사용)
number_list = [1, 2, 3, 4, 5]
i = 0
total = 0
while i < len(number_list):
    total += number_list[i]
    i += 1
print(total)

number_list = [-1, -2, -3, -4, -5]
i = 0
total = 0
while i < len(number_list):
    total += number_list[i]
    i += 1
print(total)

#4 (for 사용)
number_list = [2, 4, 6]
total = 0
n = 0
for i in number_list:
    total += i
    n += 1
print(total / n)

number_list = [2, 3, 5, 7]
total = 0
n = 0
for i in number_list:
    total += i
    n += 1
print(total / n)

#4-1 (while 사용)
number_list = [2, 4, 6]
total = 0
i = 0
n = 0
while i < len(number_list):
    total += number_list[i]
    n += 1
    i += 1
print(total / n)

number_list = [2, 3, 5, 7]
total = 0
i = 0
n = 0
while i < len(number_list):
    total += number_list[i]
    n += 1
    i += 1
print(total / n)

#5 (for 사용)
number_list = [1, 2, 3, 4, 5]
result = 1
for i in number_list:
    result *= i
print(result)

number_list = [-1, -2, 3]
result = 1
for i in number_list:
    result *= i
print(result)

#5-1 (while 사용)
number_list = [1, 2, 3, 4, 5]
result = 1
i = 0
while i < len(number_list):
    result *= number_list[i]
    i += 1
print(result)

number_list = [-1, -2, 3]
result = 1
i = 0
while i < len(number_list):
    result *= number_list[i]
    i += 1
print(result)

#6 (처음 생각한 방법)
number_list = [1, 2, 3, 4, 5]
i = 0
while i < len(number_list) - 1:
    if number_list[i] <= number_list[i + 1]:
        i += 1
    else:
       a = number_list[i] 
       number_list[i] = number_list[i + 1]
       number_list[i + 1] = a
       i += 1
print(number_list[i])

#6-1 (for 사용)
number_list = [1, 2, 3, 4, 5]
max = number_list[0]
for i in range(1, len(number_list)):
    if max < number_list[i]:
        max = number_list[i]
print(max)

number_list = [1, 1, 1]
max = number_list[0]
for i in range(1, len(number_list)):
    if max < number_list[i]:
        max = number_list[i]
print(max)

#6-2 (while 사용)
number_list = [1, 2, 3, 4, 5]
max = number_list[0]
i = 1
while i < len(number_list):
    if max < number_list[i]:
        max = number_list[i]
    i += 1
print(max)

#7 (for 사용)
number_list = [1, 2, 3, 4, 5]
min = number_list[0]
for i in range(1, len(number_list)):
    if number_list[i] < min:
        min = number_list[i]
print(min)

#7-1 (while 사용)
number_list = [1, 2, 3, 4, 5]
min = number_list[0]
while i < len(number_list):
    if number_list[i] < min:
        min = number_list[i]
    i += 1
print(min)
```