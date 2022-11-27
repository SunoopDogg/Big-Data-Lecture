# Anno Domini Project - Bibler

## 1. main branch 코드 가져오기

- git branch -M <자신이 사용할 브랜치 명>
- git checkout <자신이 사용할 브랜치 명>
- git pull origin main

## 2. 각자의 branch에서 작업한 코드 merge 하기
- git add *
- git commit(이후 Commit Message 규칙에 따라 작성)
- git push origin <자신이 사용하는 브랜치 명>

## 3. 커밋 메시지 작성 방법
1. git commit 입력 
2. i 입력(INSERT 모드로 변경)
3. 다음 규칙에 따라 commit message 작성
```
<type>: <제목>
(개행)
<body>
(개행)
<footer>
```
4. ESC 후 :wq 입력

## 4. 커밋 메시지 작성 규칙
- 제목과 본문을 빈 행으로 구분합니다.
- 제목을 50글자 이내로 제한합니다.
- 제목의 첫 글자는 대문자로 작성합니다.
- 제목의 끝에는 마침표를 넣지 않습니다.
- 제목은 명령문으로! 과거형을 사용하지 않습니다.
- 본문의 각 행은 72글자 내로 제한합니다.
- 어떻게 보다는 무엇과 왜를 설명합니다.

## 5. type 종류
- feat : 새로운 기능 추가, 기존의 기능을 요구 사항에 맞추어 수정
- fix : 기능에 대한 버그 수정
- build : 빌드 관련 수정
- chore : 패키지 매니저 수정, 그 외 기타 수정 ex) .gitignore
- ci : CI 관련 설정 수정
- docs : 문서(주석) 수정
- style : 코드 스타일, 포맷팅에 대한 수정
- refactor : 기능의 변화가 아닌 코드 리팩터링 ex) 변수 이름 변경
- test : 테스트 코드 추가/수정
- release : 버전 릴리즈

## 6. footer 종류
- 해결/관련/참고

## 7. 커밋 메시지 작성 예시
```
Feat: 사용자 인증 기능 추가

Auth Screen에서 실행 가능한
카카오 기반 로그인 기능 추가

해결
```
