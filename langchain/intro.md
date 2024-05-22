[Go To Back](./langchain.md)

# 소개

- `LangChain`은 `LLM` 애플리케이션을 개발하기 위한 프레임워크다.
- `LangChain`은 `LLM` 애플리케이션 라이프사이클의 모든 단계를 간단하게 만들어준다.

|단계|설명|
|-|-|
|개발(Development)|`LangChain` 오픈소스 라이브러리와 서드 파티 라이브러리를 사용해서 애플리케이션을 빌드할 수 있다.|
|프로덕션(Productionization)|지속가능한 최적화와 배포를 위해 체인을 평가, 모니터링, 검사를 수행하는 `LangSmith`를 사용할 수 있다.|
|디플로이먼트(Deployment)|`LangServe`를 통해 어떠한 체인도 `API`로 전환할 수 있다.|

![LangChain Architecture](./img/001_lc_arch.svg)

|라이브러리|설명|
|-|-|
|langchain-core|인터페이스와 `LCEL(LangChain Expression Language)`를 제공한다.|
|langchain-community|서드 파티와의 통합을 지원한다.|
|langchain|애플리케이션의 인지 아키텍처를 위한 `체인(Chains)`, `에이전트(Agents)`, `검색 전략(retrieval strategies)`를 제공한다.|
|langgraph||
|langserve|랭체인의 체인을 `REST API`로 배포해준다.|
|LangSmith|LLM 애플리케이션의 `모니터링(monitor)`, `테스트(test)`, `평가(evaluate)`, `디버깅(debug)`을 위한 개발자 플랫폼을 제공한다.|