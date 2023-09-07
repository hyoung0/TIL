# 반복문 제어
* break  
    * 반목문을 종료
* continue
    * continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
* for-else  
    * 끝까지 반복문을 실행한 이후에 else문 실행
    * break를 통해 중간에 종료되는 경우 else문은 실행되지 않음  
---

## break
: break문을 만나면 반복문은 종료된다.
```python
n = 0
while True:
    if n == 3:
        break
    print(n)
    n += 1
```
```
0
1
2
```
---

## continue
: continue 이후의 코드블록은 수행하지 않고, 다음 반복을 수행한다
```python
for i in range(6):
    if i % 2 == 0 :
        continue
    print(i)
```
```python
1
3
5
```
i가 0일 때는 if문의 조건이 참이 되어 continue를 만난다. continue를 만나면 이후 코드 블록은 실행되지 않기 때문에 print(0)이 실행되지 않고 다음 반복(i는 1일 때)을 시행한다.

---

## for-else
: for-else문은 끝까지 반복문을 실행한 이후에 else문 실행한다.  
for에서 break로 중단되면 else실행 안 함. break로 중단되지 않으면 else실행. 

```python
# 백준 9012번
# (1) for-else문 사용의 의미. (2)가 정답이고 비교해보자.
T = int(input())
for t in range(T):
    strings = input()
    stack = []
    for string in strings:
        if string == "(":
            stack.append(string)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                break
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
    # 

# (2) 이게 정답
T = int(input())
for t in range(T):
    strings = input()
    stack = []
    for string in strings:
        if string == "(":
            stack.append(string)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                break
    # for-else문은 for에서 break로 중단되지 않으면 else실행. 
    # break로 중단되면 else실행 안 함
    else:
        if len(stack) == 0:   
            print("YES")
        else:
            print("NO")