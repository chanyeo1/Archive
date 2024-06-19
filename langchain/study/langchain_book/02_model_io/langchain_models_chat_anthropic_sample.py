from langchain.chat_models import ChatAnthropic    # 앤트로픽의 Chat 모델을 가져오도록 변경
from langchain.schema import HumanMessage, SystemMessage 

chat = ChatAnthropic()  # 클라이언트를 만들고 chat에 저장

result = chat(  # 언어에 대한 직접적인 지시를 위해 SystemMessage 존재
    [   
        SystemMessage(content="당신은 친한 친구입니다. 존댓말을 쓰지 말고 솔직하게 답해주세요."),
        HumanMessage(content="안녕!"),
    ]
)

print(result.content)