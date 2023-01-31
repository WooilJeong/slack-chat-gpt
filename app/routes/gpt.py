from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import urllib.parse
from app.config import API_KEYS, SLACK
from app.src.api import SlackAPI, OpenaiAPI

_SLACK_API_KEY = API_KEYS["slack"]
_OPENAI_API_KEY = API_KEYS["openai"]
_SLACK_CHANNEL = SLACK["channel"]

slack_api = SlackAPI(_SLACK_API_KEY)
openai_api = OpenaiAPI(_OPENAI_API_KEY)
router = APIRouter()


@router.post("/chatgpt/")
async def send_to_chatgpt(request: Request):
    # request 결과를 JSON으로 반환
    request_body = await request.body()
    request_body = request_body.decode("utf-8")
    # 키값이 text인 항목 추출
    request_body = request_body.split("&")
    request_body = list(filter(lambda x: "text" in x, request_body))[0]
    prompt = request_body.split("=")[1]
    # + 문자열 디코딩
    prompt = prompt.replace("+", " ")
    # utf-8 디코딩
    prompt = urllib.parse.unquote(prompt)
    # GPT 결과
    response_message = openai_api.ChatGPT(prompt)
    channel_id = slack_api.get_channel_id(_SLACK_CHANNEL)
    # 문구 작성
    msg = f"""*질문*:\n{prompt}\n\n*답변*: {response_message}"""
    # 전송
    slack_api.post_message(channel_id, msg)
