## Branch 상황  
우리가 Branch를 하는 상황은 세가지로 볼 수 있다.  
i) 하나의 이력(commit) 변경 사항 있음  

ii) 두개의 이력(commit) 변경 사항 있음, 그 둘은 다른 파일  

iii) 두개의 이력(commit) 변경 사항 있음, 그 둘이 같은 파일   
이제 각각의 상황을 만들고 이해해보자.  

---

i) 하나의 이력(commit) 변경 사항 있음
1. 브랜치 생성, 이동

        $ git brunch winter (master)
        $ git checkout winter (master)  

브랜치 winter을 생성하고 winter로 브랜치를 옮겼다. 이제 master 대신 winter가 뜰 것이다.  
브랜치 생성과 이동을 한번에 하고 싶다면,  

        $ git brunch -b winter

2. 브랜치에서 작업 후 버전 기록  
작업에는 여러가지가 있으며 지금은 snow라는 파일을 추가하는 상황을 생각해 보자.  

        $ touch snow (winter)
        $ git add . (winter)
        $ git commit -m 'Add snow' (winter)

3. master에 병합  
브랜치에서 작업한 것을 master로 가져와서 합치고 싶다면 master로 이동 후 merge해야 한다.   
만약 이동하지 않고 merge한다면 합병된 최종본이 master가 아닌 winter브랜치가 된다.  

        $ git checkout master (winter)
        $ git merge winter (master)  
    
4. log로 보기  

바로 위의 코드 중 첫번째 코드 입력 후 $ git log --oneline을 입력하면. merge전이므로 season만 나오는 것을 확인 할 수 있다. 

 두번쨰 코드 입력 후 $ git log --oneline을 입력하면 winter가 merge되어 Add snow, seaon이 나오는 것을 알 수 있다.

 즉, 이 상황에서는 winter에서 commit한 log기록과 master에서 merge한 것의 log기록이 같다. 

5. 브랜치 삭제  

        $ git branch -d 
 ---

 ii) 두개의 이력(commit) 변경 사항 있음, 그 둘은 다른 파일  
1. 상황2라는 branch 생성, 이동  

         $ git branch 상황2  (master)
         $ git checkout 상황2   (master)

         혹은 $ git checkout -b 상황2  (master)  

2. 상황2라는 branch에서 작업 후 버전 기록  
작업에는 여러가지가 있으며 지금은 2라는 파일을 추가하는 상황을 생각해 보자.  

        $ touch 2.md  (상황2)
        $ git add .  (상황2)
        $ git commit -m 'Add 2'  (상황2)

3. master로 이동
        $ git checkout master  (상황2)

4. master에서 작업을 했다 (master에서 추가 commit 발생)  
작업에는 여러가지가 있으며 지금은 상황-2라는 파일을 추가하는 상황을 생각해 보자.   

        $ touch 상황-2.md  (master)
        $ git add .  (master)
        $ git commit -m 'master 변경'  (master)

5. 추가 commit이 발생한 master와 branch 상황2를 master에 병합  

        $ git merge 상황2


6. log로 보기 ($ git log --oneline -graph 하면 그래프로도 볼 수 있다.)  

* 상황2라는 branch를 commit한 후 $ git log --oneline로 기록을 보면 'Add 2'이 있고 'master 변경' 이 없다,   
master에서 merge한 후 기록을 보면  'Add 2'와 'mster변경'이 모두 있다.  

* 전자의 경우 2 파일은 있고 상황-2 파일이 없다. 후자의 경우 2, 상황-2 파일이 모두 있다.   

* master로 이동 후 작업을 하고, merge했기 때문에 branch인 상황2에는 master에서 작업 한것은 commit되지 않는다. master에는 둘의 합본이 commit된다.

7. branch 삭제  

        $ git branch -d 상황2
        
---

iii) 두개의 이력(commit) 변경 사항 있음, 그 둘이 같은 파일  
> master에 A라는 파일이 있는 상황.
1. 상황3이라는 branch 생성, 이동  

         $ git branch 상황3  (master)
         $ git checkout 상황3   (master)

         혹은 $ git checkout -b 상황3  (master)  

2. 상황3이라는 branch에서 작업 후 버전 기록  
> A파일에 작업 함  

        $ git add .  (상황3)
        $ git commit -m 'Add 3'  (상황3)

3. master로 이동
        $ git checkout master  (상황3)

4. master에서 작업을 했다. (master에 추가 commit 발생)  
> 같은 파일인 A파일에 작업 함  

        $ git add .  (master)
        $ git commit -m 'master 변경'  (master)

5. master에 병합  

        $ git merge 상황3

* merge conflict 발생  
merge conflict가 발생했다는 것은 merge되지 않은 것이고 동시에 commit되지 않았다는 것을 의미한다. 따라서 git log가 아닌 git status를 이용하여 상태를 확인한다.  

6. git status로 보기

        (생략)
        unmerged paths:  
                        (생략)
                both modified: A

위와 같은 코드를 찾아볼 수 있을 것이다. 여기서 A라는 파일이 둘 다 수정되어 merge conflict가 발생했다는 것을 알 수 있다.

7. 해결

> A라는 파일로 가서 적당히 협의하여 수정한다.

8. merge 

        $ git add .
        $ git commit  
> vim 편집기 화면이 나타난다. 
:wq 를 입력하여 저장 및 종료한다  

9. log로 보기 ($ git log --oneline -graph 하면 그래프로도 볼 수 있다.)  

9. branch 삭제  

        $ git branch -d 상황3
        
---

