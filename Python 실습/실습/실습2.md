```python

# 1
num = int(input("정수를 입력하세요 > "))
if num > 0:
    print(True)
else:
    print(False)

#2
num1 = int(input("첫 번째 정수를 입력하세요 > "))
num2 = int(input("두 번째 정수를 입력하세요 > "))
if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print(False)

#3
num = int(input("정수를 입력하세요 > "))
if num > 1 and num > 10:
# 두 조건을 모두 만족해야 하므로 and
    print(True)
else:
    print(False)

#3-1
num = int(input("정수를 입력하세요 > "))
if num > 10:
    print(True)
else:
    print(False)

#4
num = int(input("정수를 입력하세요 > "))
if num > 0 and num % 2 == 0:   
# num % 2 == 0 이면 짝수, num % 2 ==1 이면 홀수
    print(True)
else:
    print(False)

#5
num = int(input("정수를 입력하세요 > "))
if num > 100 or num < 0:
# 두 조건은 동시에 성립할 수 없으며 or을 써야한다.
    print("에러")
elif num >= 60:
    print("합격")
elif num < 60:
    print("불합격")

#6
text = input("문자열을 입력하세요 > ")
for i in range(len(text)):
# 문자열을 뒤집고 싶다면 0,1,2,3,.. 인 인덱스를 거꾸로 ...,-3,-2,-1,0으로하면 된다. 따라서 인덱스 번호를 구한다.
    print(text[-i - 1])
# 뒤집기 위해 음수 인덱스 번호를 사용한다.


#7
num1 = int(input("첫 번째 정수를 입력하세요 > "))
num2 = int(input("두 번째 정수를 입력하세요 > "))
if num1 < num2:
    for i in range(num1 + 1, num2):
        print(i)
elif num2 < num1:
    for i in range(num2 + 1, num1):
        print(i)
else:
    print(False)

#8
num1 = int(input("첫 번째 정수를 입력하세요 > "))
num2 = int(input("두 번째 정수를 입력하세요 > "))
if num1 < num2:
    for i in range(num2 - 1 , num1 , -1):
        print(i)
elif num2 < num1:
    for i in range(num1 - 1, num2 , -1):
        print(i)
else:
    print(False)

#9
num = int(input("정수를 입력하세요 > "))

if num >= 1:
    for i in range(1, num):
        if i % 2 == 1:
            print(i)
else:
    print(False)

#10
for j in range(2,10):
    for i in range(2,10):
        print(f"{j} X {i} = {j * i}")
# j가 2일 때 i의 for문으로 들어가서 i가 2,3,..,9까지 반복된다. i의 반복문이 끝나면 다시 j로 돌아가 j는 3이 되면 다시 i의 반복문이 시작된다. j가 9가 될 때까지 이 과정이 반복된다.