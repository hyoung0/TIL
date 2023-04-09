# django shell_plus 가이드

1. [터미널 입력] 패키지 설치

```
pip install ipython
pip install django_extensions
```


2. [터미널 입력] 패키지 설치 했으므로 requierments 추가 

```
pip freeze > requirements.txt
```

3. froject의 App에 등록.

```
# settings.py
# INSTALLED_APPS 리스트에 django_extensions 추가
INSTALLED_APPS = [
  # 생략 ...
  "django_extensions",
]
```

4. [터미널 입력] shell 진입

```
python manage.py shell_plus
```

