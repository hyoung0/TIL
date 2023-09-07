* 다양한 기능을 하나의 파일로 : 모듈(module)  
* 다양한 파일을 하나의 폴더로 : 패키지(package)  
* 다양한 패키지를 하나의 묶음으로 : 라이브러리(library)
* 이 것을 관리하는 관리자 : pip  
  
  
## 모듈과 패키지
* 모듈
    * 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
    * 활용  
        * import < module >
        * from < module > import < var, function, Class >
        * from < module >import *
  
* 패키지  
    * 특정 기능과 관련된 여러 모듈의 집합
    * 패키지 안에는 또 다른 서브 패키지를 포함
    * 활용  
        * from < package > import < module >
        * from < package.module > import < var, function, Class >

* 파이썬 패키지 관리자(pip)
    * pypi(python package index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템
    * 패키지 설치  
        * $ pip install SomePackage < > 
        > < >에는 버전 입력. pip는 패키지를 업그레이드 하는 경우 과거 버전을 자동으로 지워준다
    * 패키지 목록 및 특정 패키지 정보
        * $ pip list
        * $ pip show SomePackage