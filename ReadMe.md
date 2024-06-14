# Kakaotalk ChatBot MealData for Flask

----
## 프로젝트 소개
급식 정보를 가져오는 [카카오톡 챗봇](https://business.kakao.com/info/chatbot/)의 콜백 서버
## 사용법
### 서버 세팅
- 최초 실행시, config.json 생성, 필수 데이터 작성 후 재실행
### 챗봇 설정
- 챗봇 생성 후, 스킬 생성
- 스킬에 /meal을 연결
- 시나리오에 스킬을 연결 후, 데이터 불러오기

## Response Example
### 급식이 있을때
```
{
  "meal_allergy": "난류, 우유, 대두, 밀, 돼지고기, 아황산류, 쇠고기, 복숭아, 토마토, 새우",
  "meal_menu": "자장밥, 단무지, 수제탕수육, 배추김치, 구슬아이스크림"
}
```
### 급식이 없을때
```
{
  "meal_allergy": "오늘의 급식이 없습니다!",
  "meal_menu": "오늘의 급식이 없습니다!"
}
```
## Requirements
**[Flask](https://pypi.org/project/Flask/)**

**[requests](https://pypi.org/project/requests/)**
