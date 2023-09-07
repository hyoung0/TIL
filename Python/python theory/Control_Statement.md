# 제어문(Control Statement)
- 위에서 아래로 순차적 명령 수행

- 특정 상황에 따라 코드 선택적 실행/반복하는 제어 필요

- 제어문은 flow chart로 표현 가능

<br>
<br>

## 조건문(Conditional Statement)
### 기본 조건문 형식

else는 선택적 사용
```python
if  expression :
  ~ code ~
else :
  ~ code ~
```

### 복수 조건문
```python
if  expression :
  ~ code ~
elif  expression :
  ~ code ~
elif  expression :
  ~ code ~
else :
  ~ code ~
```

### 중첩 조건
```python
if  expression :
  ~ code ~
  if expression :
    ~ code ~
else :
  ~ code ~
```

<br>

## 반복문
### while문
- 조건식이 참인 경우 반복적으로 코드 실행

- 기본 형식
  ```python
  while expression :
    ~ code ~
  ```

<예시>
```python
a = 0
while a < 5 :
  print(a)
  a += 1
```



### for문
- 시퀀스를 포함한 순회가능한 객체(iterable)의 모든 요소 순회

- 순회가능한 객체 : string, tuple, list, range, set, dictionary

- 기본 형식
  ```python
  for 변수명 in iterable :
    ~ code ~
  ```

<예시>
```python
chars = input()  # apple

for index in range(len(chars)) :
  print(chars[index], end=" ")
  # a p p l e 
```

cf) print 시 
기본값은 모두 출력 후 \n이며 변경 가능
- end = "" → 모두 출력 후 마지막에 붙는 것
- sep = "" → 각각의 인자 출력 시 마다 붙는 것


### enumerate()
- index와 원소 동시에 접근 가능
  ```python
  list(enumarate(['A', 'B', 'C']))
  # = [(0, 'A'), (1, 'B'), (2, 'C')]
  ```
- in의 뒷부분인 iterable을 enumerate()로 감싸줌
  ```python
  for i, letter in enumerate('apple') :
    print(i, letter)
  # 0, a \n 1, p \n 2, p \n, 3, l \n 4, e
  ```
- 시작 인덱스 변경하고 싶을 때 start= 사용
  ```python
  for i, word in enumerate(['a', 'b', 'c'], start=1) :
    print(i, word)
  # 1, a \n 2, b \n 3, c
  ```