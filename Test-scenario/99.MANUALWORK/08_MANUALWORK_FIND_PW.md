# MANUALWORK

## FIND_PW

 `05_MANUALWORK_SINGUP.md` 절차를 먼저 진행하여 회원가입 완료 후 진행할 것

### Test Case

#### 08_MANUALWORK_FIND_PW

- 메인화면 우측 상단 로그인 클릭
- 비밀번호 입력창 하단 비밀번호 찾기 클릭
- 아이디에 qa.mobigen@gmail.com 입력
- 이름에 QA 입력
- 전화번호 국가 코드를 82 (korea) 로 설정 (기본값임)
- 전화번호에 01000000000 입력
- 비밀번호 찾기 클릭
- '고객님의 정보와 일치하는 이메일로 임시 비밀번호를 발송하였습니다' 문구 확인
- 지메일 로그인
  - id: qa.mobigen@gmail.com
  - pw: qa25251@
- 임시 비밀번호 안내 메일 확인
- 임시 비밀번호로 로그인이 성공하는지 확인
