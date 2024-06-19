from langchain.chat_models import ChatOpenAI    # 모듈 가져오기
from langchain.schema import HumanMessage, AIMessage 

chat = ChatOpenAI(  # 클라이언트를 만들고 chat에 저장
    model="gpt-3.5-turbo",  # 호출할 모델 지정
)

result = chat(  # 대화 형식의 상호작용을 표현하기 위해 HumanMessage, AIMessage 존재
    [   
        HumanMessage(content="계란찜 만드는 법을 알려줘"),
        AIMessage(content="{ChatModel의 답변인 계란찜 만드는 법}"),
        HumanMessage(content="안녕하세요!"),
    ]
)

print(result.content)