# 딕셔너리(Dictionary)

* 키 - 값(key - value)쌍으로 이루어진 모음(collection)  
    * 키(key)  
         * 변경 불가능한 데이터(immutable)만 활용 가능  
        (string, integer, float, boolean, tuple, range)
    * 값(values)
        * 모든 값으로 설정 가능
* 키와 값은 : 로 구분되고, 개별 요소는 ,로 구분된다.
```python
students = {'홍길동': 30, '김철수': [{'age' : 25}, {'country' : 'korea'}, 8]}
print(students['홍길동'])   # 30
print(students['김철수'])   # [{'age': 25}, {'country': 'korea'}, 8]
print(students['김철수'][0])   # {'age': 25}
print(students['김철수'][1]['country'])  # korea
print(students['김철수'][2])  #8
```
* 변경 가능하며(mutable), 반복 가능함(iterable)
    * 딕셔너리는 반복하면 키가 반환된다.
---

## 딕셔너리(Dictionary) 키 - 값 추가 및 변경
* 딕셔너리에 키와 값의 쌍을 추가할 수 있다.
* 이미 해당하는 키가 있다면 기존 값이 변경된다.
```python
students = {'홍길동': 30, '김철수': 25}
students['박영희'] = 95
print(students)  # {'홍길동': 30, '김철수': 25, '박영희': 95}

students['홍길동'] = 80
print(students)  # {'홍길동': 80, '김철수': 25, '박영희': 95}
```
## 딕셔너리(Dictionary) 키 - 값 삭제
* .pop()를 이용하여 키를 삭제(키가 기준으로 키가 삭제되면 값도 삭제된다)
```python
students = {'홍길동': 80, '김철수': 25, '박영희': 95}
students.pop('홍길동')
print(students)   # {'김철수': 25, '박영희': 95}
```
* 키가 없는 경우는 KeyError발생
---
## 딕셔너리(Dictionary) 순회
* 딕셔너리는 기본적으로 key를 순회하며 key를 통해 값(value)을 활용
```python
students = {'홍길동': 30, '김철수': 25}
for student in students:
    print(student, stdents[student])
# 홍길동 30
# 김철수 25
```
* 추가 메서드를 활용하여 순회 가능
    * keys() : key로 구성된 결과
    * values() : value로 구성된 결과
    * items() : (key, value)의 튜플로 구성된 결과  
        ```python
        students = {'홍길동': 30, '김철수': 25}
        for key, value in students.items():
            print(key, value)  
        ```  
        > 바로 위의 코드랑 같은 값이 나옴

