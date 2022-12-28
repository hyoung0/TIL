# 깃허브
## 원격저장소를 알아보자.
git은 원격저장소 역할을 해 주며 내가 사용하고 있는 것을 local이라 할 수 있다. 내가 작업한 내용을 원격저장소에 올릴 수도 있고, 원격저장소에 있는 것을 가져올 수도 있다. 
### push : 원격저장소에 저장소를 만들고 반영

1. 오른쪽 상단 + 모양
2. new repositoty 클릭 
git remote add origin https://github.com/hyoung0/test1.git
(git아 원격저장소 추가해 origin으로 url을) 
을 복사하여 *terminal에 입력*한다.
이는 저장할 원격저장소가 어디인지 지정해 주는 과정이다.
어디로 push할지(원격저장소)를 정함
3. $ git remote -v
4. $ git push origin master


git commit에서 이전 것이 저장 안되었을 떄 ==> :wq

* 수정 사항이 생겼다.

1. ctrl + s로 저장한다
2. $ git add .
3. $ git commit -m '수정 사항1'
4. $ git log --oneline
5. $ git push origin master


pull
$ git pull origin master

clone
다른 사람의 것(저장소를)을 아예 새롭게 가져올 경우
(원격에 있는 프로젝트 시작)
1. 초록색 code 클릭
2. download ZIP 은 가장 최신 버전의 상태의 파일만 받는 것

3. clone은 $ git clone은 git 저장소를 받아오는 것. 모든 버전을 받는다.
 (협업 작업을 원하면 clone)

.gitignore : git 파일/폴더 등을 관리 x
이미 커밋된 것은 무시하지 않는다. 그러니 미리 .gitignore를 설정하자.