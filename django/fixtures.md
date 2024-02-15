# Fixtures

> 모델에 초기 데이터를 제공!

- Django가 데이터베이스로 가져오는 방법을 알고있는 데이터 모음

- Django가 직접 만들기 때문에 데이터베이스 구조에 맞춰 작성되어 있음

### dumpdata

- 데이터 베이스의 모든 데이터를 출력, 여러 모델을 하나의 json file로 만들 수 있음

- 명령어 : `python manage.py dumpdata --indent 4 app_name.model_name app_name.model_name ... > filename.json`

- indent 4를 통해 json file 생성시 들여쓰기가 적용되도록 함

- 모델을 나열하여 하나의 json file에 데이터 생성 가능

- 하지만 추후 관리를 위하여 각각 생성하는 것을 추천

### loaddata

- fixtures 데이터를 데이터베이스로 불러옴

- fixtures의 기본경로는 'app_name/fixtures/'로 되어있기 때문에 Django는 설치된 모든 app의 fixtures 폴더 이후의 경로로 파일을 찾아 load함

- fixtures 파일이 어떤 app의 fixtures 폴더에 있는지는 상관없음

- 명령어 : `python manage.py loaddata file_name.json file_name.json ...`

- loaddata를 한번에 실행하지 않고 하나씩 실행한다면 모델 관계에 따라 순서가 중요함(comment는 article에 대한 key 및 user에 대한 key가 필요한 것 처럼)

- 따라서 user → articles → comment 순으로 load해야 오류가 발생하지 않음

- loaddata 시 encoding codec error가 발생하는 경우 2가지 해결 방법
  - dumpdata 시 추가옵션 작성 : `python -Xutf8 manage.py dumpdata ....`

  - loaddata 후 메모장으로 json 파일을 열기 → 다른 이름으로 저장 클릭 후 인코딩을 UTF8로 선택 후 저장