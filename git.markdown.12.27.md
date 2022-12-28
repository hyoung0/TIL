# git markdown. 12.27

## cli
- ls : 목록(list)
- mkdir : 디렉토리 생성(make directory)
- cd : 디렉토리 이동(change directory)
- . : 현재 디렉토리
- .. : 상위 디렉토리
- touch 파일명 : 새로운 파일을 생성
- rm 파일명 : 파일 삭제(remove)
- rm -r b 폴더명: 폴더 삭제하기
 (폴더는 안에 있는 파일을 다 지워야 되므로 바로 지우기 힘드므로)

## git terminal
### add, commit의 의미
- (1통) untracked files : 트래킹되지 않은 파일들
    
    1.txt를 만들었지만, add를 하지 않음
- (2통) changes to be committed : 커밋될 변경사항들

    보고서.txt 만들고 add함
### 입력해야될 설정
- git config --global user.email "you@example.com"
- git config --global user.name "Your Name"

1. git config --global user.email "choyoung1034@naver.com"
2. git config --global user.name "hyoung0"
3. 입력 후 방향키 위 버튼을 두번 누른다.

nothing to commit, working tree clean ==> 1통, 2통 비어있음!