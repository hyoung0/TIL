# lambda  
* 함수를 간편하게 작성할 수 있게 해주어 다른 함수의 인수로 넣을 때 주로 사용한다.  

* lambda 매개변수들 : 식

```python
lambda x : x + 1
>>> <function <lambda> at 0x0000012A8657F280>

plus = lambda x : x + 1
print(plus(3))
>>> 4
```
람다 표현식은 말 그대로 이름이 없는 함수를 만들기 때문에 그대로 함수를 호출할 수 없다. 따라서 람다 표현식을 변수에 할당하여 출력해야한다.  

---

## 람다표현식 변수  
* 람다 표현식 안에서는 변수를 만들 수 없다.  

```python
(lambda x: y = 10; x + y)(1)
>>> SyntaxError: invalid syntax
```
> lambda 매개변수들 : 식  
이므로 식 안에서는 새로운 변수를 만들 수 없다.  
단,  다음과 같이 람다 표현식 바깥에 있는 변수는 사용할 수 있다.  
```python
y = 10
(lambda x: x + y)(1)
>>> 11
```
## 람다 표현식을 인수로 사용
```python
list(map(lambda x: x + 10, [1, 2, 3]))
>>> [11, 12, 13]
```
---
## 정렬함수에 lambda 활용하기   

* key에서 정렬을 목적으로 하는 함수를 값으로 넣는다. 이 때 lambda를 함수로 이용할 수 있다.

```python 
a = ['kdkd', 'dfw', 'dgwdg', 's']
   
a2 = sorted(a, key = lambda x : len(x))
a3 = sorted(a, key=len)

>>> ['s', 'dfw', 'kdkd', 'dgwdg']
```
> 두번째 줄에서 key=len(a)가 아닌 key=len임에 주의하자. key는 함수를 값으로 넣기 때문.  

<br>

* 튜플 lambda로 정렬하기  
  * 첫 번쨰 원소로 내림차순 정렬, 첫 번쨰 원소 같은 경우 두 번쨰 원소로 오름차순 정렬

  ```python
  v = [(3,4), (2,2), (3,3), (1,2), (1,-1)]
  v.sort(key=lambda x: (-x[0], x[1]))
  print(v)

  >>> [(3,3), (3,4), (2,2), (1,-1), (1,2)]
  ```