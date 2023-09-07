# String Formatting

### %-formatting
```python
name = 'Kim'
score = 4.5

print('Hello, %s' % name)
print('내 성적은 %d' % score)
print('내 성적은 %f' % score)  # 타입에 따라
```

### f-string
```python
name = 'Kim'
score = 4.5
print(f'Hello, {name}! 성적은 {score}')  #Hello, Kim! 성적은 4.5

pi = 3.141592
print(f'원주율은 {pi:.3}. 반지름이 2일 때 원의 넓이는 {pi*2*2}')
# 원주율은 3.14. 반지름이 2일 때 원의 넚이는 12.566368
```

<br>
<br>