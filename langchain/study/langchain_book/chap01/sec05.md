[Go To Back](../../study.md)

# 5. OpenAI의 API를 호출해 작동을 확인한다.

```
# 01_setting/sample.py

import json
import openai   # OpenAI에서 제공하는 파이썬 패키지 가져오기

response = openai.ChatCompletion.create(    # OpenAI API를 호출해 언어 모델을 호출
    model="gpt-3.5-turbo",  # 호출할 언어 모델의 이름
    messages=[
        {
            "role": "user",
            "content": "iPhone8 출시일을 알려주세요"    # 입력할 문장(프롬프트)
        },
    ]
)

print(json.dumps(response, indent=2, ensure_ascii=False))
```
```
{
  "id": "chatcmpl-9bmSm9k10ZzNn1ovNzE4ZwMAjLaUj",   # API의 호출 로그를 관리하거나 특정 호출을 추적할 때 사용하는 고유한 ID
  "object": "chat.completion",  # API가 반환하는 객체의 종류
  "created": 1718791456,    # API를 호출한 시간의 UNIX 타임스탬프
  "model": "gpt-3.5-turbo-0125",    # 사용한 모델의 이름
  "choices": [  # 반환된 결과의 배열
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "아이폰 8은 2017년 9월 22일에 출시되었습니다."   # AI의 답변
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {    # API 사용량
    "prompt_tokens": 19,        # 입력 토큰 수
    "completion_tokens": 28,    # 출력 토큰 수
    "total_tokens": 47          # 총 토큰 수
  },
  "system_fingerprint": null
}
```

### API는 매개변수를 지정해 작동을 변경할 수 있다.
```
# 01_setting/sample.py

import json
import openai   # OpenAI에서 제공하는 파이썬 패키지 가져오기

response = openai.ChatCompletion.create(    # OpenAI API를 호출해 언어 모델을 호출
    model="gpt-3.5-turbo",  # 호출할 언어 모델의 이름
    messages=[
        {
            "role": "user",
            "content": "냉면의 원재료를 알려줘"    # 입력할 문장(프롬프트)
        },
    ],
    max_tokens=100,     # 생성할 문장의 최대 토큰 수
    temperature=1,      # 생성할 문장의 다양성을 나타내는 매개변수
    n=2,                # 생성할 문장 수
)

print(json.dumps(response, indent=2, ensure_ascii=False))
```
```
{
  "id": "chatcmpl-9bmZEwzrvTGGjv0deUbboQKGtD8Yg",
  "object": "chat.completion",
  "created": 1718791856,
  "model": "gpt-3.5-turbo-0125",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "물, 면발, 김가루, 닭고기, 달걀, 각종 야채(오이, 무, 파, 깻잎 등), 고추가루, 설탕, 식초, 간장, 소금 등이 냉면의 주된 원재료입니다."
      },
      "logprobs": null,
      "finish_reason": "stop"   # 모델이 응답을 종료한 이유 (자연스로운 끝)
    },
    {
      "index": 1,
      "message": {
        "role": "assistant",
        "content": "냉면의 주요 원재료는 밀가루, 소금, 물로 만든 면발 및 냉면 국물이며, 채썬 오이, 당근, 양파, 부추, 호박, 생략, 달걀, 소고기, 고명 등 다양한 재"
      },
      "logprobs": null,
      "finish_reason": "length" # 모델이 응답을 종료한 이유 (max_tokens에 도달한 경우)
    }
  ],
  "usage": {
    "prompt_tokens": 23,
    "completion_tokens": 193,   # n 매개변수로 인해 max_tokens 초과
    "total_tokens": 216 
  },
  "system_fingerprint": null
}
```

### Complete 모델의 API를 호출해 본다.
```
# 01_setting/sample_complete.py

import json
import openai

response = openai.Completion.create(    # ChatCompletion 대신 Completion 사용
    engine="gpt-3.5-turbo-instruct",    # model 대신 engine을 지정
    prompt="오늘 날씨가 매우 좋고 기분이",  # prompt를 지정
    stop=".",   # 문자가 나타나면 문장 종료
    max_tokens=100, # 최대 토큰 수
    n=2,    # 생성할 문장 수
    temperature=0.5 # 다양성을 나타내는 매개변수
)

print(json.dumps(response, indent=2, ensure_ascii=False))
```
```
{
  "id": "cmpl-9bmjRclVBFJCzR6v6ZpcDGz6lKaH4",
  "object": "text_completion",  # 'Complete 모델의 API 호출
  "created": 1718792489,
  "model": "gpt-3.5-turbo-instruct",
  "choices": [
    {
      "text": " 좋습니다",  # 모델이 생성한 응답
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    },
    {
      "text": " 좋습니다",
      "index": 1,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 18,
    "completion_tokens": 6,
    "total_tokens": 24
  }
}
```