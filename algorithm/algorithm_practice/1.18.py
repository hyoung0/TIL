# 9498
a = int(input())
if a >= 90:
    print("A")
elif a >= 80:
    print("B")
elif a >= 70:
    print("C")
elif a >= 60:
    print("D")
else:
    print("F")

# 9093
T = int(input()) 

for t in range(T):
    sentence = input().split()
    result_list = []
    for word in sentence:
        new_word = word[::-1]
        result_list.append(new_word)
    print(' '.join(result_list))

# 9093
T = int(input())
for t in range(T):
    sentence = input().split()
    for i in range(len(sentence)):
        print(sentence[i][::-1], end=" ")

# 11721
strings = input()
i = 1
while True:
    if len(strings) < 10 * i:
        print(strings[10 * (i-1):])
        break
    print(strings[10 * (i-1):10 * i])
    i += 1

# 11721 -1
word = input()
for i in range(0, len(word), 10):
    print(word[i:i+10])

# 2947
numbers = list(map(int, input().split()))

while True:
    for i in range(len(numbers)):
        if i < len(numbers) - 1:
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                print(' '.join(map(str, numbers)))
    if numbers == [1, 2, 3, 4, 5]:
        break
split없이 문자열로 받아서 문자열 슬랑이싱 후 int로 비교