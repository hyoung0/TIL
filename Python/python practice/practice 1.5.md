```python
#1 (for사용)
text = input("문자열을 입력하세요 > ")
count = 0
for i in text:
    if i == "e":
        count += 1
print(count)

#1-1 (while사용)
text = input("문자열을 입력하세요 > ")
count = 0
i = 0
while i < len(text):
    if text[i] == "e":
        count += 1
    i += 1
print(count)

#2
text = input("문자열을 입력하세요 > ")
count = 0
for i in text:
    if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        count += 1
print(count)

#3
dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}

print(2023 - int(dict_variable["생년"]) + 1)

#4 (items 사용)
dict = {}
dict["이름"] = input("이름을 입력하세요 > ")
dict["전화번호"] = input("전화번호를 입력하세요 > ")
dict["거주지"] = input("거주지를 입력하세요 > ")
print(dict)
for key, value in dict.items():
    print(f'{key} : {value}')

#4-1 (items사용 안함)
dict = {}
dict["이름"] = input("이름을 입력하세요 > ")
dict["전화번호"] = input("전화번호를 입력하세요 > ")
dict["거주지"] = input("거주지를 입력하세요 > ")
print(dict)
for key in dict:
    print(f'{key} : {dict[key]}')

#5
dict1 = {}
dict2 = {}
dict2["전화번호"] = input("전화번호를 입력하세요 > ")
dict2["이메일"] = input("이메일을 입력하세요 > ")
dict2["거주지"] = input("거주지를 입력하세요 > ")
dict1[input("이름을 입력하세요 > ")] = dict2
print(dict1)

#6
text = input("문자열을 입력하세요 > ")
dict = {}
i = 0
count = 1
while i < len(text):
    if text[i] not in text[:i]:
        dict[text[i]] = 1
        i += 1
    else:
        count += 1
        dict[text[i]] = count
        i += 1
for key, value in dict.items():
    print(key, value)
```