
```python

# 1
number1 = 1
number2 = number1 + 1  
print(number1, number2)  # 1, 2
```
> number1에 1이 할당되었으므로, number2 = 1 + 1

```python
# 2
number1 = 10
number2 = 5
number3 = str(number1) + str(number2)
number4 = number1 + number2

print(number1, number2, number3, number4) # 10 5 105 15
```
> str은 문자로 변형해준다.  
number3는 숫자 10과 숫자 5를 더한 것이 아닌, 문자 10과 문자5를 더 한 것이기에 105가 된다. 문자와 문자는 더할 수 있다.

```python
# 3
string1 = "Hello"
string2 = string1
string3 = "World" + "!"

print(string2, "?", string3) # Hello ? world!

```
```python
# 4
string = "Hello?"
n = 5

print(string * n) # Hello?Hello?Hello?Hello?Hello?
```
> 문자와 숫자를 곱하면, 문자가 숫자만큼 반복된다.   
```python
# 5
string = "abc hello def"
sub_string1 = string[4:10]
sub_string2 = string[1:4]
sub_string3 = string[-1]

print(sub_string1) # hello 
print(sub_string2) # bc 
print(sub_string3) # f
```
> 띄어쓰기도 문자로 취급한다.   
```python
# 6
number1 = 5
number2 = 10.0 + number1
number1 - 5
number3 = number1 * (number2 + 10)

print(number1, number2, number3) # 5 15.0 125.0
```
> number1 - 5는 print가 없으므로 출력되지 않는다.
```python
# 7
list_variable = [1, 2, 3, [1, 2, 3]]
sub_list = list_variable[3][-1]

print(sub_list) # 3
```
> list-variable의 3번째 인덱스( list-variable[3] )는 [1, 2, 3]이다.  
이것의 -1번째 인덱스는 3이다.
```python
# 8
list_variable = []
list_variable.append(1)
list_variable.append("a")
list_variable[0] = 0

print(list_variable) # 0 a
```
> .append()로 인해 list_variable = [1, "a"]이 된다.  
여기서 0번째 인덱스는 1인데(list_variable[0] = 1), 0번째 인덱스가 0이라고 했으므로(list_variable[0] = 0) list_variable = [0, "a"] 가 된다.  

```python
# 9
name = input("너의 이름은?")   # 터미널에 루피 침
print(name) # 너의 이름은?    # 루피

# 10
age = int(input("너의 나이는?"))

print("올해 나이 : ", age)   # 올해 나이 : 5     # terminal에 5를 침
print("내년 나이 : ", age + 1)    # 내년 나이 : 6   # terminal에 5를 침
```