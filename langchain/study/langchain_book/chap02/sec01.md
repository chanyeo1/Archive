[Go To Back](../../study.md)

## Model I/O를 구성하는 3개의 서브모듈

**Language models**

- 다양한 언어 모델을 동일한 인터페이스에서 호출할 수 있는 기능 제공

**Prompts**

- 언어 모델을 호출하기 위한 프롬프트를 구축하는 데 유용한 기능 제공
- 프롬프트를 쉽게 만들 수 있도록 하는 것이 목적

**Output parsers**

- 언어 모델에서 얻은 출력을 분석해 애플리케이션에서 사용하기 쉬운 형태로 변환하는 기능 제공
- 출력 문자열을 정형화하거나 특정 정보를 추출하는 데 사용

## Language models를 사용해 gpt-3.5-turbo 호출하기
```
# 02_model_io/language_models.py

from langchain.chat_models import ChatOpenAI    # 모듈 가져오기
from langchain.schema import HumanMessage   # 사용자의 메세지인 HumanMessage 가져오기

chat = ChatOpenAI(  # 클라이언트를 만들고 chat에 저장
    model="gpt-3.5-turbo",  # 호출할 모델 지정
)

result = chat(
    [
        HumanMessage(content="안녕하세요!"),
    ]
)

print(result.content)
```
```
안녕하세요! 무엇을 도와드릴까요? :)
```

```
# 02_model_io/language_models_ai_message_sample.py

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
```
```
안녕하세요! 계란찜을 만드는 법에 대해 궁금하신가요? 저는 여러분이 계란찜을 만드는 데 도움이 될 수 있습니다. 계란찜은 간단하면서도 맛있는 한국 요리입니다. 준비물과 순서에 대해 설명해 드릴까요?
```

### SystemMessage를 사용해 언어 모델의 성격과 설정을 정의한다.
```
# 02_model_io/language_models_system_message_sample.py

from langchain.chat_models import ChatOpenAI    # 모듈 가져오기
from langchain.schema import HumanMessage, SystemMessage 

chat = ChatOpenAI(  # 클라이언트를 만들고 chat에 저장
    model="gpt-3.5-turbo",  # 호출할 모델 지정
)

result = chat(  # 언어에 대한 직접적인 지시를 위해 SystemMessage 존재
    [   
        SystemMessage(content="당신은 친한 친구입니다. 존댓말을 쓰지 말고 솔직하게 답해주세요."),
        HumanMessage(content="안녕!"),
    ]
)

print(result.content)
```
```
안녕! 어떻게 지내? 무슨 일 있어?
```

### 언어 모델 교체 가능
```
# 02_model_io/langchain_models_chat_anthropic_sample.py

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
```

## PromptTemplate로 변수를 프롬프트에 전개하기
```
# 02_model_io/prompt.py

from langchain import PromptTemplate 

prompt = PromptTemplate(
    template="{product}는 어느 회사에서 개발한 제품인가요?",    # {product} 변수를 포함하는 프롬프트
    input_variables=[
        "product",  # product에 입력할 변수 지정
    ]
)

print(prompt.format(product="아이폰"))
print(prompt.format(product="갤럭시"))
```
```
아이폰는 어느 회사에서 개발한 제품인가요?
갤럭시는 어느 회사에서 개발한 제품인가요?
```

## Language models와 PromptTemplate의 결합
```
# 02_model_io/prompt_and_language_model.py

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

prompt = PromptTemplate(
    template="{product}는 어느 회사에서 개발한 제품인가요?",

    input_variables=[
        "product"
    ]
)

result = chat(
    [
        HumanMessage(content=prompt.format(product="아이폰")),
    ]
)

print(result.content)
```
```
아이폰은 미국의 애플(Apple)사에서 개발한 제품입니다.
```
