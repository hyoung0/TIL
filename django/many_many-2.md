# Many to Many relationship 02

## 동일한 모델과의 N : M 관계

User와 User의 관계 예시

### profile 페이지 구현
```python
# accounts/urls.py

urlpatterns = [
  ...
    path('<str:username>/', views.profile, name='profile'),
]
```
- 여기서 주의할 점은 url주소의 `<str:username>/`은 str 타입으로 다른 index, create도 모두 str으로 인식해버림

- django는 url을 위에서부터 아래로 읽으면서 해당하는 url이 나오면 그 url로 가므로 profile url을 맨 아래에 두거나 `profile/<str:username>/`와 같이 앞에 profile을 붙여줘야 함

```python
# accounts/views.py

# username도 유일한 값이므로 pk와 같은 역할을 할 수 있음
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```
```html
<!-- accounts/profile.html -->

<div>
  <h1>
    {{ person }}님의 프로필 페이지
  </h1>
</div>
```


### User간의 Follow 구현
```python
# accounts/models.py

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```
- 대체만 했던 User model에 필요한 field를 추가하여 커스텀

- 동일한 모델의 ManyToManyField의 'to'인자는 'self'

- symmetrical
  - '팔로우'와 같이 동일한 모델에서의 ManyToMany관계에서 사용됨

  - 기본값은 True이며 이는 source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델의 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)

  - 대칭을 원하지 않는 경우 False로 설정

```python
# accounts/urls.py

urlpatterns = [
    ...
    path('<int:you_pk>/follow/', views.follow, name='follow'),
    path('<str:username>/', views.profile, name='profile'),
]
```
- 상대 user의 pk값을 인자로 받음

```python
# accounts/views.py

@login_required
def follow(request, you_pk):
    you = get_user_model().objects.get(pk=you_pk)
    me = request.user
    if you != me:
        if me in you.followers.all():
            you.followers.remove(me)
        else:
            you.followers.add(me)
    return redirect('accounts:profile', you)
```
- User 모델은 get_user_models()을 통해 받아옴

```html
<!-- accounts/profile.html -->

<div class="d-flex align-items-center">
  <div class="me-3">
    <!-- Button trigger modal -->
    <!-- 버튼을 누르면 팔로잉, 팔로우 목록이 모달로 뜨도록 함 -->
    <button type="button" class="border-0 bg-transparent" data-bs-toggle="modal" data-bs-target="#following">
      팔로잉 {{person.followings.all|length}}
    </button>
    <button type="button" class="border-0 bg-transparent" data-bs-toggle="modal" data-bs-target="#follower">
      팔로워 {{person.followers.all|length}}
    </button>
  </div>
  
  <!-- 로그인 되어있고 자신의 계정이 아닌 경우 팔로우 버튼이 보이도록 함 -->
  {% if request.user.is_authenticated and request.user != person %}
    {% if request.user in person.followers.all %}
      <form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
        <button type="submit" class="btn btn-primary" style="heigh: 30px;">
          팔로우
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check2-circle" viewBox="0 0 16 16">
            <path d="M2.5 8a5.5 5.5 0 0 1 8.25-4.764.5.5 0 0 0 .5-.866A6.5 6.5 0 1 0 14.5 8a.5.5 0 0 0-1 0 5.5 5.5 0 1 1-11 0z"/>
            <path d="M15.354 3.354a.5.5 0 0 0-.708-.708L8 9.293 5.354 6.646a.5.5 0 1 0-.708.708l3 3a.5.5 0 0 0 .708 0l7-7z"/>
          </svg>
        </button>
      </form>
    {% else %}
      <form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" class="btn btn-outline-primary" value="팔로우">
      </form>
    {% endif %}
  {% else %}
    <button class="btn btn-secondary" disabled>팔로우</button>
  {% endif %}
</div>
</div>

<!-- Modal -->
<!-- 팔로잉, 팔로우 목록이 뜨는 모달창, 누르면 해당 user profile로 가도록 설계 -->
<div class="modal fade" id="following" tabindex="-1" aria-labelledby="followingLabel" aria-hidden="true">
<div class="modal-dialog">
  <div class="modal-content">
    <div class="modal-header">
      <h1 class="modal-title fs-5" id="followingLabel">팔로잉</h1>
      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
    </div>
    <div class="modal-body">
      {% for following in person.followings.all %}
        <a href="{% url 'accounts:profile' following %}" class="text-decoration-none text-black">{{followings}}</a>
      {% endfor %}
    </div>
  </div>
</div>
</div>
<div class="modal fade" id="follower" tabindex="-1" aria-labelledby="followerLabel" aria-hidden="true">
<div class="modal-dialog">
  <div class="modal-content">
    <div class="modal-header">
      <h1 class="modal-title fs-5" id="followerLabel">팔로워</h1>
      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
    </div>
    <div class="modal-body">
      {% for follower in person.followers.all %}
        <a href="{% url 'accounts:profile' follower %}" class="text-decoration-none text-black">{{follower}}</a>
      {% endfor %}
    </div>
  </div>
</div>
```

<br>

