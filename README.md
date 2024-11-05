# 🌱기초 백엔드 스터디 #

`2024년 2학기 GDSC Hongik 기초 백엔드 스터디` 강의 자료 및 소스코드 리포지토리 입니다.   
- [노션 소개 페이지 바로가기](https://www.gdschongik.com/basic-backend-study/introduce)   
- [공지사항 및 과제 명세](https://www.gdschongik.com/basic-backend-study)

### 학습 목표 ###
- Django를 이용해 가장 간단한 글 작성, 댓글 작성이 가능한 게시판을 직접 만들어 볼 예정입니다.
- RDB, ORM과 같은 백엔드에서 중요한 기본 지식들을 Django를 통해 배워 봅니다.
- 웹개발에 대한 적성이나 흥미를 찾고 나중에 스스로 깊게 학습할 수 있는 방향을 제공하는 것이 목적입니다.

### 커리큘럼 ###
|주차|내용|키워드|
|------|---|---|
|1주차 (9월 10일)|OT & 웹 기초 학습|장고란 무엇인가|
|2주차 (9월 24일)|MVT 패턴이란,장고 설치|Django MVT(1)|
|3주차 (10월 1일)|View와 Template,간단한 페이지 띄워보기|Django MVT(2)|
|4주차 (10월 7일)|Model과 ORM|DB 생성,조회|
|5주차 (11월 5일)|form을 이용한 질문 생성|데이터 저장|
|6주차 (11월 12일)|수정과 삭제|수정, 삭제 구현
|7주차 (11월 19일)|댓글 기능 구현하기|Relation,FK|
|8주차 (11월 26일)|검색,페이징|ORM 심화|

---
### 예전 강의자료 확인하기 ###

리포지토리 메인 화면에서 코드 왼쪽 상단 branch 변경 버튼 클릭

<img width="932" alt="스크린샷 2024-11-06 오전 12 01 29" src="https://github.com/user-attachments/assets/177aa1ef-ce52-46ca-ab92-b29f9b94eeb4">

원하는 주차 선택 후 주차별 소스 코드 확인

<img width="912" alt="스크린샷 2024-11-06 오전 12 01 47" src="https://github.com/user-attachments/assets/4aa82eca-d184-41b1-a04f-1599bf95b161">

### 예전 강의록 확인 ###
[주차별 공지사항에서 강의록 pdf 다운이 가능합니다](https://www.gdschongik.com/basic-backend-study)   

---

### 강의 자료와 다른 사항 ###
- `__pycache__` 폴더와 폴더 내의 캐시 파일은 강의 진행과 무관해 업로드하지 않았습니다.
- `.gitignore`는 깃허브 리포지토리에 불필요한 파일(위의 캐시 파일, DB 등)이 올라가지 않도록 설정해주는 파일입니다.   
  강의 자료에는 존재하지 않으며, 강의 진행과 무관합니다.
- `config/settings.py`의 `SECRET_KEY` 항목은 보안상 이유로 퍼블릭 리포지토리에는 올리지 않는 것이 원칙입니다.   
  실제 사용하는 서비스는 아니지만 원칙을 지키기 위해  `config/settings.py`에 몇가지 로직을 추가했습니다.   
  배포 공부를 하실때 참고해 보시면 좋을 것 같습니다.
