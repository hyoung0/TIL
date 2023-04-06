# 2023.03.21

# Django template system  
  * 데이터 표현을 제어하면서, 표현과 관련된 로직을 담당(템플릿 파일과 관련)

## Variable  

* HTMLL 컨텐츠를 변수 갑셍 따라 빠구고 싶을 때 사용
* view 함수에서 render함수의 세번째 인자로 딕셔너리 타입으로 넘겨 받을 수 있음. 
```python
...생략
context = {
  'articles': articles
}
return render(request, 'exam.html', context)
```

* 딕셔너리 key 에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨. 
```python
 {{ articles }}
```

* dot(.)을 사용하여 변수 속성에 접근할 수 있음

---

## Filters

```python
{{ variable|filter }}
```

* 표시할 변수를 설정할 때 사용
* chined가 가능하며 일부 필터는 인자를 받기도 한다  
```python
{{ name|truncateword:30 }}
```  
* 약 60개의 built-in template filters를 제공
.

---

## Tags
* 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행 

```html
<body>
  <div>
    {% for article in articles %}
      <a href="{% url 'todos:detail' article.pk %}">
        <p>pk - {{ article.pk }}</p>
      </a>

      <p>완료상태: {{ article.completed }} 
        {% if article.completed == False %}
        <a href="{% url 'todos:completed' article.pk %}">완료 하기</a>
        {% else %}
        <a href="{% url 'todos:completed' article.pk %}">완료 취소</a>
        {% endif %}
      </p>

    {% endfor %}
  </div>
  
</body>
```
---

## comments
* DTL에서의 주석표현 ( {#  example   #} )

```html
<h1>Hello, {# name #}</h1>
```

