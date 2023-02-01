import openai
from slack_sdk import WebClient
from PyKakao import KoGPT


class SlackAPI:
    """
    슬랙 API 클래스
    """

    def __init__(self, token=None):
        self.client = WebClient(token)

    def get_channel_id(self, channel_name):
        """
        슬랙 채널ID 조회
        """
        # conversations_list() 메서드 호출
        result = self.client.conversations_list()
        # 채널 정보 딕셔너리 리스트
        channels = result.data['channels']
        # 채널 명이 'test'인 채널 딕셔너리 쿼리
        channel = list(
            filter(lambda c: c["name"] == channel_name, channels))[0]
        # 채널ID 파싱
        channel_id = channel["id"]
        return channel_id

    def get_message_ts(self, channel_id, query):
        """
        슬랙 채널 내 메세지 조회
        """
        # conversations_history() 메서드 호출
        result = self.client.conversations_history(channel=channel_id)
        # 채널 내 메세지 정보 딕셔너리 리스트
        messages = result.data['messages']
        # 채널 내 메세지가 query와 일치하는 메세지 딕셔너리 쿼리
        message = list(filter(lambda m: m["text"] == query, messages))[0]
        # 해당 메세지ts 파싱
        message_ts = message["ts"]
        return message_ts

    def post_thread_message(self, channel_id, message_ts, text):
        """
        슬랙 채널 내 메세지의 Thread에 댓글 달기
        """
        # chat_postMessage() 메서드 호출
        result = self.client.chat_postMessage(
            channel=channel_id,
            text=text,
            thread_ts=message_ts
        )
        return result

    def post_message(self, channel_id, text):
        """
        슬랙 채널에 메세지 보내기
        """
        # chat_postMessage() 메서드 호출
        result = self.client.chat_postMessage(
            channel=channel_id,
            text=text
        )
        return result


class OpenaiAPI:
    """
    OpenAI API 클래스
    """

    def __init__(self, api_key=None):
        self.api_key = api_key

    def completion(self, prompt):
        """
        OpenAI completion API 호출
        """
        openai.api_key = self.api_key
        response = openai.Completion.create(
            engine="text-davinci-003",  # https://platform.openai.com/docs/models/gpt-3
            prompt=prompt,
            temperature=0.5,
            max_tokens=1024,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        return response['choices'][0]['text']


class KakaoAPI:
    """
    Kakao API 클래스
    """

    def __init__(self, api_key=None):
        self.api_key = api_key

    def kogpt(self, prompt):
        """
        Kakao OpenGPT API 호출
        """
        kogpt = KoGPT(self.api_key)
        response = kogpt.generate(prompt, max_tokens=256, temperature=0.1)
        response = response['generations'][0]['text']
        return response
