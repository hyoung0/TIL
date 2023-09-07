# 예외 처리 (Exception Handling)
* try 문 / except 절을 이용하여 예외 처리를 할 수 있다
* 에러가 발생하는 코드여도 실행이 된다.
* try문은 반드시 한 개 이상의 except문이 필요  


* try문 
    * 오류가 발생할 가능성이 있는 코드를 실행
    * 예외가 발생되지 않으면, exept없이 실행 종료
* exept문  
    * 예외가 발생하면, except절이 실행
* finally
    * 예외 발생 여부와 관계없이 항상 실행
---
## 작성방법
```python
try:
    실행하고자 하는 코드
except:
    에러가 발생했을 때 실행할 코드
    # 에러가 발생하는 상황을 인지하고 작성
```
```python
try:
    실행하고자 하는 코드
except < >:
    해당 에러(< >)가 발생했을 때 실행할 코드  
    # 어떤 에러가 발생할 지 알아야함(예를 들어 < > 에 사용할 수 있는 것은,ValueError , ZeroDivisionError 등)
except < >:
    해당 에러(< >)가 발생했을 때 실행할 코드  
    # 어떤 에러가 발생할 지 알아야함
finally:
    실행하고자 하는 코드
    # 선택사항임.
```
---
## 예외 발생 시키기

* raise statement  
    * raise <표현식> <메시지>

* assert statement  
    * assert <표현식> <메시지>
```python
assert len([1, 2]) == 1, '길이가 1이 아닙니다'
```
를 입력하면 다음과 같이 출력된다.
```python
Traceback (most recent call last):
  File "c:\Users\yeuno\Desktop\TIL\test.py", line 1, in <module>
    assert len([1, 2]) == 1, '길이가 1이 아닙니다'
AssertionError: 길이가 1이 아닙니다
```
마지막줄을 보면 AssertionError이 발생한다. assert는 표현식이 False인 경우 동작하지 않는다. 표현식의 True, False여부에 따라 동작하지 않을 수 있기 때문에 실제 서비스코드에서는 사용을 지양하며 디버깅을 위한 목적으로 사용된다.