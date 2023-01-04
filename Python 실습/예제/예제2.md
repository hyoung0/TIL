
```python
#1
a = 1
b = 1
print(a < b) # False

#2
a = bool("")
b = False
print(a == b) # True
```
> ""은 False이다  
```python
#3
a = 1
result = ""

if a == 1:
    result = True
else:
    result = False
    
print(result) # True
```
> a에 1이 할당되었으므로 else가 아닌 if로 들어가고 따라서 True가 출력된다.

```python
#4
a = 90 

if a == 90:
    a = a + 10
    
elif a == 100:
    a = a + 10
    
elif a == 110:
    a = a + 10

else:
    a = a + 10

a = a + 10 
print(a) # 110
```
> a에 90이 할당되었으므로 elif나 else가 아닌 if문으로 들어간다. a = 90 + 10 = 100이다.  
print위의 a = a + 10 에 의해 a = 100 + 10 = 110 이다.
```python
#5
string = "hello world!"

for element in string:
    print(element)
    
"""
예측을 작성하세요.
h
e
l
l
0

w
o
r
l
d
!
"""

#6
list_variable = [0, 1, 2, 3, 4, 5, 6]

for element in list_variable:
    print(element, end=" ")  
    
"""
예측을 작성하세요.
0 1 2 3 4 5 6
"""
```
> for문은 시퀀스를 포함한 순회가능한 객체요소를 모두 순회한다. 즉, list_variable의 첫 번째 요소인 0부터 마지막 요소인 6까지 들어간다.

```python
#7
n = 10

for element in range(-n, n):
    print(element, end=" ")
    
"""
예측을 작성하세요.
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9
"""
```
> range(-10, 10)은 10부터 10-1까지의 숫자의 시퀀스이다.  

```python
#8
n = 10

for element in range(1, n + 1, 3):
    print(element, end=" ")
    
"""
예측을 작성하세요.
1 4 7 10
"""
```
> range(1, 11, 3)은 1부터 11-1까지 3만큼 증가시킨 숫자의 시퀀스이다.

```python
#9
n = 10

for element in range(n, -n, -1):
    print(element, end=" ")
    if n < 0:
        break
"""
예측을 작성하세요.
10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9
"""

#10
list_variable = [-1, 3, 5, -2, 1, 9, 21, -3, -5]

for element in list_variable:
    if element < 0:
        continue
    
    print(element, end=" ")
    
"""
예측을 작성하세요.
3 5 1 9 21
"""

#11
N = 3
M = 4

for n in range(N):
    for m in range(M):
        print(f"{n}, {m}")
"""
예측을 작성하세요.
0, 0
0, 1
0, 2
0, 3
1, 0
1, 1
1, 2
1, 3
2, 0
2, 1
2, 2
2, 3
"""
```