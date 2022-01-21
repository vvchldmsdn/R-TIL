# 1. Git

GUI, CLI = ex) 탐색기, git bash

"무언가를 알고 싶으면 명령을 하고 결과를 읽어야한다."

"CLI 할 때 항상 경로 확인"

원격 저장소에서 직접 수정 X

모든 파일변경 수정 삭제 생성 => 로컬에서 합시다.  커밋 열심히 합시다.

* test 파일 2개 만드려고 할때 -> GUI에서는 경고문 넘어가야 입력가능

  ​												 -> CLI에서는 경고 메세지만 나오고 다른 것 입력가능

* 인터페이스 = 접면 : 컴퓨터에 명령을 내리는 매개

  * 스마트폰은 터치 인터페이스

* CLI 명령어

  * **ls** : 경로 안에 폴더와 파일들 보겠다
* **mkdir** " ~~":  " ~~ " 폴더 만들기
  * **cd "~~"**: " ~~ " CLI 현재 디렉토리 " ~~ " 로 변경 (Change Directory)

    * cd .. : CLI 현재 디렉토리 상위 폴더로 이동
* **touch " ~~ ".md(txt, ...)**: 파일 생성
  * **pwd**: 내가 작업하고 있는 디렉토리 출력 명령어 (Print Working Directory)
* **rm**: 폴더, 파일 지우기
    * **rm -r " ~~ "**: " ~~ " 폴더 다 지우기
  

* **git 기초 흐름**: 1. 작업을 하고 / 2. 변경된 파일을 모아(add) / 3. 버전으로 기록한다. (commit)
  * **git add**: working directory 에서 staging area 로 버전 기록
  * **git commit**: staging area에서 repository로 커밋(버전) 기록
    * working directory에서 작업한 것 따로 버전만들어서 commit하기 위해 staging area와 repository 두 단계로 나뉨
    * 유튜브 질문 답변: (질문: staging area에 있는 버전을 따로 commit 할 수 있나요?)
      * git restore --staged <file명>으로 특정 파일만 내리시면 되요. stash는 staging area 자체를 임시저장 해놓고 비우는거라 그대로 stash를 다시 안가져오시면 다 제거된다고 보시면 될거에요.
      * 스테이지에는 버전이 존재하는것이 아니라 파일들의 변경사항만 존재합니다. 만약 변경사항들 전체가 아니라 부분만 커밋 하고 싶다면, 필요한 변경사항들만 스테이지에 두고 커밋을 하시면 됩니다. (git add <filename> 으로 원하는 파일들의 변경사항만 취사선택하여 스테이지에 올릴 수 있습니다.
  * **git status** 
    * untracked files: 커밋 안되는(wd에 있는) 파일
    * Changes not staged for commit: 커밋 될수 있는 파일
    * ('git' 이라는 명령어 치면 git명령문 다 볼 수 있음) 
    * **git log**: 'git log --oneline': commit 한 번에 보기
  * **git clone**: 원격 저장소에서 가져옴 (로컬 저장소와 원격 저장소 둘다 생기게 됨)
  * **git pull**: 원격 저장소에 연결된 로컬 저장소에서 원격 저장소로 부터 변경사항 가져옴
  * 
