from langchain import PromptTemplate 

prompt = PromptTemplate(
    template="{product}는 어느 회사에서 개발한 제품인가요?",    # {product} 변수를 포함하는 프롬프트
    input_variables=[
        "product",  # product에 입력할 변수 지정
    ]
)

print(prompt.format(product="아이폰"))
print(prompt.format(product="갤럭시"))