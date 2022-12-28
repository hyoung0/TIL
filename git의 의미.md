# git 

        분산 버전 관리 시스템    
: 원격 저장소를 만들어 로컬에서도 버전을 기록하고 관리한다.

* 상단의 Terminal -> New Terminal -> TERMINAL창에서 Git Bash 클리 후 진행
---

## 기본적으로 입력해야될 설정
### 이메일과 이름입력
- git config --global user.email "you@example.com"
- git config --global user.name "Your Name"
#### 내가 입력한 이메일과 이름
1. $ git config --global user.email "choyoung1034@naver.com"
2. $ git config --global user.name "hyoung0"
3. 입력 후 방향키 위 버튼을 두번 누른다.
---
## 상태 확인
commit을 하려다 보면 오류가 종종 발생 하는데, 그 때 현 상황을 파악하기 위해 사용하는 방법이 있다.
* $ git status  
: 현재 상태를 알려준다. 1통(파일 작업)과 2통(버전 기록을 위한 add)상태에서 사용한다.
* $ git log
: 버전의 기록을 확인할 수 있다. 즉 3통 상태인 것을 알 수 있다.
---

## 1. 저장소 생성
버전을 기록을 하든 관리를 하든, 우선 저장소가 있어야 한다.

    $ git init    
 => (master)이 추가됨.

## 2. 버전 기록
버전을 기록하기 위해서는 add, commit의 단계를 거쳐야 한다.  
파일을 작업하면, add는 commit을 하기 위한 준비를 해준다고 생각한다. add를 하여 commit을 위한 준비가 되었다면, commit으로 버전을 기록한다.
## add : 커밋 대상 기록  
* commit을 위해 꼭 필요한 징검다리 역할(?)  

        $ git add <file>  

* 그런데 경험상 저 file이 이름이 적절하지 않으면 file이 발견되지 않는 다는 에러가 자주 뜬다. 그럴 떄는 *현재 파일*을 add한다고도 할 수 있다.  

        $ git add .  

### add 관련 error  
- (1통) untracked files : 트래킹되지 않은 파일들  
파일을 만들었지만, add를 하지 않음

## commit : 버전 기록
        $ git commit -m '<커밋메시지>
### commit 관련 error
- (2통) changes to be committed : 
---

## *상황을 생각해보자*
 * A라는 파일을 만들었고 이를 분산 버전 관리하고 싶다. 다음과 같이 하면 된다.
1. $ git init  (저장소 생성)
2. $ git status   (현재 상태 확인. 생략 가능)
3. $ git add A    (커밋 대상 기록)

    혹은 $ git add .
4. $ git commit -m 'A파일'     (버전 기록)
5. $ git log  (버전 기록 확인. 생략 가능)

 * A라는 파일을 commit했는데 이후에 수정 했다면?  
 :기존 A는 commit 되어 3통에 있지만 수정한 A는 1통에 담겨 있다. 즉, 수정한 A의 버전을 관리하고 싶다면, add와 commit을 다시 해주어야 한다.

 1. ctrl + s 로 수정한 A파일 저장
 2. $ git add A
 3. $ git commit -m 'A파일 수정'
 4. $ git log

 * B라는 파일을 추가하고 버전 관리하고 싶다면?  
        => $ touch B 한 이후 위 과정에서 A대신 B를 써주면 됨.



커밋될 변경사항들  
파일을 만들고 add함.


nothing to commit, working tree clean ==> 1통, 2통 비어있음!