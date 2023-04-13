# 2023-03-24

## django modles
( urls, view, html 작성 전에 미리 해놓기를..)
1. django-admin startproject <플젝이름> .
2. python manage.py runserver
3. python manage.py startapp <앱이름>
4. app폴더 안의 models.py에 설계도 초안 작성
5. python manage.py makemigrations 설계도 작성
6. python manage.py migrate 설계도 DB에 전달하여 반영

## 관리자 계정 생성 및 등록
> 반드시 첫 migration을 하고 만들어야됨.  
 테이블이 만들어져 있어야 테이블에 계정이 저장되기 때문
1. python manage.py createsuperuser
2. DB에 생성된 admin 계정 확인
3. admin에 모델 클래스 등록. 등록하지 않으면 admin site에서 확인 할 수 없음
  * app폴더의 admin.py에서 아래와 같은 코드 입력
  
  from .models import Article

  admin.site.register(Article)

## 모델 필드 수정
1. 처음 작성했던 app폴더 안의 models.py에 필드 추가하여 작성
2. python manage.py makemigrations 설계도 작성
  * 이 때 기존 테이블에 수정을 하는 것이기 때문에 django와의 소통이 필요.
    (특히 날짜 데이터는 신경써야 할 것이 많으니 django의 도움을 받자. 1번 -> enter)
3. migrations폴더에 추가 되었는지 확인
4. python manage.py migrate 설계도 DB에 전달하여 반영
5. dp.sqlite에 필드 추가 되었는지 확인
