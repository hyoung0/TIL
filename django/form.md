# 2023.03.21

## 'form' element
  * 사용자로부터 할당된 데이터를 서버로 전송한다. 웹에서 사용자 정보를 입력하는 여러 방식(text, password 등)을 제공한다.  
  * form의 핵심 속성은 2가지 이다.  
  *action* (데이터를 어디로),  *method* (어떤 방식으로) 보낼 것인가  
  * 'form' element 안에 보통 사용자의 데이터를 입력 받을 수 있는 'input' element사용  
    * type 속성 값에 따라 다양한 유형의 데이터를 받음  
    * 'name'은 input의 핵심 속성으로 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 dictionary의 key값으로 받아 사용자가 입력한 데이터에 접근할 수 있음.

---

### action  
  * 입력 데이터가 전송될 URL을 지정
  * 만약 이 속성을 지정하지 않은면 데이터는 현재 form이 있는 페이지의 URL로 보내짐  

### method  
  * 데이터를 어떤 방식으로 보낼 것인지 정의  
  * 데이터의 HTTP request methods (GET, POST)를 지정


```django
{% extends 'base.html' %}

{% block content %}
  <form action="/catch/" method="GET">
    <input type="text" name="message">
    <input type="submit">
  </form>
{% endblock content %}
```

```django
<body>
  <form action="{% url 'todos:create' %}" method="POST">
    {% csrf_token %}
    <div>
      <label for="date_">마감기한</label>
      <input type="date" name='date' id='date_'>
    </div>
    <input type="submit" value='할 일 생성'>
  </form>
</body>
```