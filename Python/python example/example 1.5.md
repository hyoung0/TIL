```python
#1
dict_variable = {}
dict_variable["이름"] = "정우영"
dict_variable["생년월일"] = "19000101"
dict_variable["회사"] = "하이퍼그로스"

print(dict_variable["이름"]) # 정우영
print(dict_variable["생년월일"]) # 19000101
print(dict_variable["회사"]) # 하이퍼그로스

#2
dict_variable = {"a": "A", "B": "b"}
dict_variable["c"] = "C"
dict_variable["D"] = "d"
dict_variable["e"] = "E"


print(dict_variable["a"]) # A
print(dict_variable["D"]) # d 
print(dict_variable["b"]) # Key 값에 b는 없으므로 오류 

#3
dict_variable = {}
dict_variable["apple"] = 5000
dict_variable["banana"] = 3000
dict_variable["apple"] = 2000
dict_variable["banana"] = dict_variable["banana"] + 1000

print(dict_variable["apple"] + dict_variable["banana"]) # 6000

#4
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key in dict_variable:
    print(key, dict_variable[key])

"""
예측을 작성하세요.
이름 정우영
생년월일 190001101
회사 하이퍼그로스
"""

#5
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key, value in dict_variable.items():
    print(key, value)

"""
예측을 작성하세요.
이름 정우영
생년월일 190001101
회사 하이퍼그로스
"""
#> key, value가 아닌 i, j 이런식으로 써도 됨.
#>즉 .items()하면  key, value자체를 인식하는 것이 아니라 순서대로 key값과 value를 받는듯

#6
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

print("나이" in dict_variable) # False

#> print("이름" in dict_variable) # True
#> print("정우영" in dict_variable) # False

#7
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

if "거주지" not in dict_variable:
    dict_variable["거주지"] = "서울특별시"
    # 위 조건문의 조건식이 무엇을 의미하는지 작성하세요.
    # 만약 거주지가 dict_variable의 key값에 없다면,
    
print(dict_variable) # {'이름': '정우영', '생년월일': '19000101', '회사': '하이퍼그로스', '거주지': '서울특별시'}

#8
list_variable = []

try:
    list_variable.append(0)
    list_variable.append(1)
    list_variable.append(2)
    print(list_variable[3])
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

"""
출력 결과를 예측해서 작성하세요.
에러가 발생했습니다.
에러의 원인은 무엇인가요?
"""  
#> list_variable = [0, 1, 2]으로 인덱스는 2까지밖에 없다.
#> 그런데 list_variable[3] 즉 3번째 인덱스를 출력하라고 했으므로 오류가 떠야한다.
#> 이 떄 except에 의해 예외 처리를 하였기 때문에 위와 같은 출력이 나옴.

#9
try:
    number = 1
    if number == 1
        print(number)
    
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

"""
if문의 끝에 :를 쓰지 않았기 때문이다.
(invalid syntax)

""" 
#10
n = 10
total = 0

for number in range(0, n + 1):
    if number % 2 == 0:
        total += number * 2
    elif number % 2 == 1:
        total += number + 1 * 3

print(total) # 100
```