# GitHub
## 원격저장소를 알아보자.
github은 원격저장소 역할을 해 주며 내가 사용하고 있는 것을 local이라 할 수 있다. 내가 작업한 내용을 원격저장소에 올릴 수도 있고, 원격저장소에 있는 것을 가져올 수도 있다. 

---

## push : 로컬 저장소의 버전을 원격저장소(github)로 보낸다
보통 내가 한 로컬 프로젝트 개발을 공유할 때 사용 

        $ git push <원격저장소이름> <브랜치이름>  
<원격저장소이름>을 보통 origin으로, <브랜치이름>을 보통 master로 설정한다. 
### push 하는 순서
1. github 오른쪽 상단 + 모양
2. new repositoty 클릭   
3. 어디로 push할지(원격저장소)를 정한다.  
git remote add origin https://github.com/hyoung0/test1.git  
(git아 원격저장소 추가해 origin으로 url을) 
을 복사하여 *terminal에 입력*한다.
이는 저장할 원격저장소가 어디인지 지정해 주는 과정이다.
3. $ git remote -v
4. $ git push origin master  

---
## pull : 원격저장소(github)의 버전을 로컬 저장소로 가져오기
보통 다른 사람의 커밋을 받아올 때 사용  

        $ git pull <원격저장소이름> <브랜치이름>  
<원격저장소이름>을 보통 origin으로, <브랜치이름>을 보통 master로 설정한다.   

        $ git pull origin master
---

## clone : 원격저장소 복제  
다른 사람의 것(저장소를)을 아예 새롭게 가져올 경우
(원격에 있는 프로젝트 시작)  

         $ git clone

*   download ZIP 은 가장 최신 버전의 상태의 파일만 받는 것으로 다르다.

* clone은 git 저장소를 받아오는 것. 모든 버전을 받는다.
 (협업 작업을 원하면 clone)
* 새로운 프로젝트를 시작할 때 저장소를 생성하기 위해 git init을 사용한다. 그런데 clone은 모든 버전을 가져오고 당연히 저장소도 가져오므로 git clone을 할 때에는 git init을 하지 않는다.

---

## .gitignore : git 파일/폴더 등을 관리하지 않는다. 무시한다.
* 이미 커밋된 것은 무시하지 않는다. 그러니 미리 .gitignore를 설정하자.

---

## *기존 파일에서 수정사항이 생겼을 때는?*
**git의 의미**에서 말했던 것과 같은 논리이다. 버전을 관리하기 위해서는 add, commit이 선행되어야 한다. 그러나 기존 파일은 버전 기록(commit)까지 되었을 지언정 수정한 파일은 버전되지 않은 1통에 있다. 따라서 add, commit을 한 후 push해야 한다.
* 파일 수정 후 push하려고 할 때
1. ctrl + s로 저장한다
2. $ git add .
3. $ git commit -m '수정 사항1'
4. $ git log --oneline
5. $ git push origin master