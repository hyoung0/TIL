# GitGub profile readme
저장소의 이름을 내 github이름으로 설정하고, github 이용하기에서 한 것과 같이 하면 된다.

# Branch
## Branch란?
독립적인 작업흐름을 만들고 관리

각각의 버전의 상태로 작업할 수 있다. 다른 사람의 작업물 상태로 가서 작업할 수 있다.

각자 작업한 것을 합치는 것이merge

마스터 브런치로 가져올거면 마스터에서 merge해야됨

git checkout -b 하면 저절로 만들고 이동함

2단계 : 다른 파일 수정
master에는 머지한 fearur/report가 추가된다.  feature/report에는 머지하지 않았기 때문에 없다 master에서 만든 hotfitx가 없다

3단계 : 동일파일 수정

충돌이 나면? git status에서 both commit을 보면 무엇이 충돌 났는지 알 수 있다

     딥러닝으로 글자 비교해서 같은 분야끼리 합치면 편하겠는걸,,
충돌을 해결했다면, add, commit한다.
git log --oneline -graph
HEAD는 내가 있는 위치
독립적인 작업을 병합할 수 있게 해준다.

git flow

pull request로 github에 올라가는 것이 브랜치 만들기 전 상태인 master에 있던 것이고, 그 이후 merge를 해서 github에서 merge가 되는건가요??

master이 아닌 branch에서 push (merge 안 한 상태)

commit은 저장의 개념이 아니므로 완료된 걸 올려야 한다 ㅎ


git restore --staged b.txt
git commit --amend

restore 뒤로 가기