# Slack Chat GPT

슬랙의 특정 채널에서 /gpt 명령으로 openai의 completions api를 이용할 수 있도록 구현한 프로젝트입니다. Chat GPT와 유사한 기능을 슬랙에서 사용할 수 있습니다.

<div align="center">

<img src="https://github.com/WooilJeong/slack-chat-gpt/blob/main/img/ex1.png?raw=true" width="800" />

<img src="https://github.com/WooilJeong/slack-chat-gpt/blob/main/img/ex2.png?raw=true" width="800" />

</div>


## 개발환경

- Oracle Cloud Infrastructure(OCI)
- docker
- python 3.9.12
- fastapi 0.89.1
- slack_sdk 3.19.5
- openai 0.26.4


## 사용방법

- slack bot 생성
- slack app 설치
- openai api key 발급
- `app/config.py` 작성

```python
API_KEYS = {
    "slack": "슬랙 토큰",
    "openai": "오픈AI API키",
}

SLACK = {
    "channel": "슬랙채널명",
}
```

- slack app - Features - Slash Commands 설정
    - `Create New Command` 버튼 클릭
    - Request URL에 FastAPI URL 입력 (ex. https://****.com/chatgpt/)
- slack app 재설치
- 서버 실행
- 슬랙 채널에 질문 입력

```
/gpt 안녕하세요.
```

## 서버 실행 방법

- 로컬실행

```bash
uvicorn app.main:app --host 0.0.0.0 --port 11650 --reload
```

- 도커실행

(추가 예정)