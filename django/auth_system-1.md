# Authentication

## Authentication System
> 사용자 인증과 관련된 기능을 모아 놓은 시스템으로 인증과 권한 부여를 함께 처리

※ 사전 설정
- 'accounts'라는 이름으로 app 생성 및 등록(settings.py, urls.py에 작성)

- django 내부적으로 auth와 관련된 경로나 키워드들을 accounts라는 이름으로 사용하므로 accounts로 지정 권장!


### Custom User model 대체

- django가 기본적으로 제공하는 User model은 내장된 auth모듈의 User class를 사용

- 이는 별도의 설정 없이 사용 가능하여 간편하지만 직접 수정할 수 없기 때문에 User model을 커스텀해야 함

- Custom User model로 대체 시 기본 User model과 동일하게 작동하면서도 필요한 경우 맞춤 설정 가능

- ※ 이 작업은 프로젝트의 모든 migrations 혹은 첫 migrate 실행 전에 마쳐야 함!!!

- [공식문서 참고](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model)

1. AbstractUser를 상속받는 커스텀 User class 작성
    ```python
    # accounts/models.py
    from django.contrib.auth.models import AbstractUser

    class User(AbstractUser):
      pass
    ```
    - 기존 User class도 AbstractUser를 상속받기 때문에 custom User class도 완전히 같은 모습을 가짐

2. django 프로젝트가 사용하는 기본 User model을 우리가 작성한 custom User model로 지정
    ```python
    # settings.py

    AUTH_USER_MODEL = 'accounts.User'  # 'app_name.custom_user_class_name'
    ```
    - 수정 전 기본값은 'auth.User'

    - __※※ [주의] 프로젝트 중간에 AUTH_USER_MODEL을 변경할 수 없음 ※※__ (이미 진행한 경우 DB초기화 후 진행 필요)

3. admin에 등록하기
    ```python
    # accounts/admin.py

    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    from .models import User

    admin.site.register(User, UserAdmin)
    ```
    - 기본 User model이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음

→ 대체 후 migrate 시 DB에 'accounts_user' table 확인 가능


### Login

> Session을 생성하는 과정으로 로그인을 위한 내장 form 'AuthenticationForm()' 사용

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
]


# accounts/views.py

# built-in form인 AuthenticationForm import
from django.contrib.auth.forms import AuthenticationForm
# login을 import하고 이름이 겹치면 안되니까 as로 다른 이름 지어주기
from django.contrib.auth import login as auth_login

def login(request):
  if request.method == 'POST':
    # POST method인 경우 request, request.POST를 인자로 넣고 받은 Form을 변수에 할당
      form = AuthenticationForm(request, request.POST)
      # form = AuthenticationForm(request, data=request.POST)
      if form.is_valid():
        # 유효성 검사를 통과한 경우 login 메서드로 session 생성
          auth_login(request, form.get_user())
          return redirect('accounts:index')
  else:
    # GET method인 경우 AuthenticationForm을 변수에 저장하여 context로 보내줌
      form = AuthenticationForm()
  
  # 유효성 검사를 통과하지 못한 경우, GET method인 경우
  context = {
      'form': form,
  }
  return render(request, 'accounts/login.html', context)
```
```html
<h1>Login</h1>
<form action="{% url 'accounts:login' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}  
  <input class="btn btn-dark" type="submit" value="로그인">
</form>
```
- login(request, user) : 인증된 사용자를 로그인하는 함수(세션 생성)

- get_user() : AuthenticationForm의 인스턴스 메서드로 유효성 검사 통과 시 사용자 객체를 반환

- 생성된 session은 DB의 django_session table에서 확인 가능


### Logout

> Session을 Delete하는 과정으로 session data를 DB에서 삭제 및 클라이언트 쿠키에서 session id 삭제

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]


# accounts/views.py

# logout 메서드를 import하고 이름이 겹치므로 as로 이름 지어주기
from django.contrib.auth import logout as auth_logout

def logout(request):
  # 메서드에 인자로 request 넣어주기
    auth_logout(request)
    return redirect('accounts:index')
```


<br>

## Template with Authentication data

```html
<!-- accounts/index.html -->

<h2>사용자 정보 - {{ user }}</h2> <br>
{% if request.user.is_authenticated %}
  <h3>{{ user }}님 안녕하세요!</h3>
  <form action="{% url 'accounts:logout' %}" method="POST">
    {% csrf_token %}
    <input class="btn btn-dark" type="submit" value="로그아웃">
  </form>
{% else %}
  <h3>로그인 후 이용 가능합니다.</h3>
  <a class="btn btn-dark" href="{% url 'accounts:login' %}" role="button">로그인</a>
```
- context processors : django에서 자주 사용하는 데이터 목록을 템플릿이 렌더링될 때 호출 가능하도록 컨텍스트 데이터 목록에 작성되어있음
  ```python
  # settings.py

  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [ BASE_DIR / 'templates' ],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

- context로 직접 작성하여 넘겨주지 않아도 user의 값을 불러올 수 있음

- request.user.is_authenticated : 인증된 사용자의 경우 True 반환