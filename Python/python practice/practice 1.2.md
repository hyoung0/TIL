```python
# 1.
number = int(input("숫자를 입력해주세요 > "))   
# input은 기본적으로 문자열이므로 숫자 연산을 위해서는 int를 붙여주어야 한다.

print(number + 10)

# 2.
name = input("좋아하는 음식을 입력해주세요 > ")
print("좋아하는 음식 : " + name)
# 문자형끼리 더할 수 있다.

# 3.
name = input("이름을 입력해주세요 > ")
year = int(input("태어난 년도를 입력해주세요 > "))
# age에서 숫자 연산을 해야 하므로 int사용
age = str(2023 - year + 1)
# 아래 print에서 숫자와 문자는 합칠 수 없기 때문에 str을 붙여 문자형으로 변환.
print("저의 이름은 " + name + "이고, 올해 나이는 " + age + "세 입니다.")

# 4.
one = input("첫 번째 문장을 입력해주세요 > ")
two = input("두 번째 문장을 입력해주세요 > ")
print(one + two)

# 5. 
number = int(input("숫자를 입력해주세요 > "))
print(-1 * number)
# 숫자 부호 바꾸기

# 6.
one = int(input("첫 번째 숫자을 입력해주세요 > "))
two = int(input("두 번째 숫자을 입력해주세요 > "))
더하기 = str(one + two)
빼기 = str(one - two)
곱하기 = str(one * two)
몫 = str(one // two)
나머지 = str(one % two)

print("더하기 연산 : " + 더하기)
print("빼기 연산 : " + 빼기)
print("곱하기 연산 : " + 곱하기)
print("몫 연산 : " + 몫)
print("나머지 연산 : " + 나머지)

# 7.
one = int(input("첫 번째 숫자를 입력해주세요 > "))
two = int(input("두 번째 숫자를 입력해주세요 > "))
three = int(input("세 번째 숫자를 입력해주세요 > "))
average = (one + two + three) / 3
print(average)

# 8.
list1 = int(input("첫 번째 숫자를 입력해주세요 > "))
list2 = int(input("두 번째 숫자를 입력해주세요 > "))
list3 = int(input("세 번째 숫자를 입력해주세요 > "))
list4 = int(input("네 번째 숫자를 입력해주세요 > "))
list5 = int(input("다섯 번째 숫자를 입력해주세요 > "))
a = []
a.append(list1)
a.append(list2)
a.append(list3)
a.append(list4)
a.append(list5)
print(a)

# 9.
문자열 = input("문자열을 입력해주세요 > ")
숫자 = int(input("숫자를 입력해주세요 > "))
print(문자열 * 숫자)
# 문자열 * 숫자 하면 문자열이 숫자 만큼 반복되어 나옴

# 10.
a1 = int(input("첫 번째 숫자를 입력해주세요 > "))
print(a1)
a2 = int(input("두 번째 숫자를 입력해주세요 > "))
print(a1 + a2)
a3 = int(input("세 번째 숫자를 입력해주세요 > "))
print(a1 + a2 + a3)
a4 = int(input("네 번째 숫자를 입력해주세요 > "))
print(a1 + a2 + a3 + a4)
a5 = int(input("다섯 번째 숫자를 입력해주세요 > "))
print(a1 + a2 + a3 + a4 + a5)


# 10-1.

result = 0
a1 = int(input("첫 번째 숫자를 입력해주세요 > "))
result = result + a1
print(result)
a2 = int(input("두 번째 숫자를 입력해주세요 > "))
result = result + a2
print(result)
a3 = int(input("세 번째 숫자를 입력해주세요 > "))
result = result + a3
print(result)
a4 = int(input("네 번째 숫자를 입력해주세요 > "))
result = result + a4
print(result)
a5 = int(input("다섯 번째 숫자를 입력해주세요 > "))
result = result + a5
print(result)


# 10-2
result = 0
a1 = int(input("첫 번째 숫자를 입력해주세요 > "))
result += a1
print(result)
a2 = int(input("두 번째 숫자를 입력해주세요 > "))
result += a2
print(result)
a3 = int(input("세 번째 숫자를 입력해주세요 > "))
result += a3
print(result)
a4 = int(input("네 번째 숫자를 입력해주세요 > "))
result += a4
print(result)
a5 = int(input("다섯 번째 숫자를 입력해주세요 > "))
result += a5
print(result)

