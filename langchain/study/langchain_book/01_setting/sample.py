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