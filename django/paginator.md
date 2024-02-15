# django Paginator
☆ [공식문서 참고](https://docs.djangoproject.com/en/4.2/ref/paginator/)

```python
# articles/views.py
from django.core.paginator import Paginator

def index(request):
    articles = Article.objects.order_by('-pk')  # 최신순 정렬
    page = request.GET.get('page', '1')         # page번호 get, 없으면 1
    per_page = 5                                # 페이지에 포함할 최대항목 수
    pagination = Paginator(articles, per_page)  # Paginator 객체 생성
    page_obj = pagination.get_page(page)        # pagination 객체에서 해당 page의 개체 목록

    context = {
        'articles': page_obj,
        'last_page': pagination.num_pages,   # .num_pages = 페이지의 길이 = 마지막페이지
    }
    return render(request, 'articles/index.html', context)
```
```html
<!-- articles/index.html -->

<ul class="pagination justify-content-center">
  <li class="page-item">
    <!-- 첫 페이지이므로 page=1 -->
    <a class="page-link" href="?page=1">처음</a>
  </li>
  <!-- 이전 페이지가 있는 경우 -->
  {% if articles.has_previous %}
    <li class="page-item">
      <a class="page-link" href="?page={{ articles.previous_page_number }}">
        <span aria-hidden="true">&laquo;</span>
      </a>
    </li>
  <!-- 없는 경우 비활성화 -->
  {% else %}
    <li class="page-item disabled">
      <a class="page-link" tabindex="-1" aria-disabled="true" href="#">
        <span aria-hidden="true">&laquo;</span>
      </a>
    </li>
  {% endif %}

  <!-- 페이지 버튼을 차례로 구현 -->
  {% for page_number in articles.paginator.page_range %}
    <!-- 페이지 수가 많을 경우를 대비해 +-5까지만 생성되도록 함 -->
    {% if page_number >= articles.number|add:-5 and page_number <= articles.number|add:5 %}
      {% if page_number == articles.number %}
        <li class="page-item active" aria-current="page">
          <a class="page-link" href="?page={{ page_number }}">{{ page_number }}</a>
        </li>
      {% else %}
        <li class="page-item">
          <a class="page-link" href="?page={{ page_number }}">{{ page_number }}</a>
        </li>
      {% endif %}
    {% endif %}
  {% endfor %}

  {% if articles.has_next %}
    <li class="page-item">
      <a class="page-link" href="?page={{ articles.next_page_number }}">
        <span aria-hidden="true">&raquo;</span>
      </a>
    </li>
  {% else %}
    <li class="page-item disabled">
      <a class="page-link" tabindex="-1" aria-disabled="true" href="#">
        <span aria-hidden="true">&raquo;</span>
      </a>
    </li>
  {% endif %}
  <li class="page-item">
    <a class="page-link" href="?page={{ last_page }}">마지막</a>
  </li>
</ul>
```

<br>
