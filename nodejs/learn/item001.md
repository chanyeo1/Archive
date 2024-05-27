[Go To Back](../nodejs.md)

# 환경변수 읽는 방법

- `process`는 프로세스가 시작될 때 설정되는 모든 환경 변수를 `env` 프로퍼티로 제공하는 `Node.js`의 코어 모듈이다.
- 아래의 코드는 `USER_ID`와 `USER_KEY`를 설정하고 `app.js`를 실행한다.

```
USER_ID=239482 USER_KEY=foobar node app.js
```
- 위의 코드는 테스트 환경에 적합하지만 프로덕션 환경에서는 환경변수를 설정하기 위해 배쉬 스크립트를 사용할 것이다.

> `process`는 `require`를 필요로 하지 않고 바로 사용가능하다.

- 아래 코드는 `USER_ID`와 `USER_KEY` 환경변수에 접근하는 예제다.
```
process.env.USER_ID;    // "239482"
process.env.USER_KEY;   // "foobar"
```

- `--env-file` 플래그를 사용하면 Node.js 애플리케이션이 실행될 때 환경변수 파일을 명시할 수 있다.
- 아래 코드는 `.env` 파일과 `process.env` 프로퍼티를 사용해 환경변수에 접근하는 방법을 보여준다.

```
# .env file
PORT=3000
```
```
process.env.PORT;
```
```
node --env-file=.env app.js
```
- 위의 코드는 `.env` 파일로부터 모든 환경변수를 로드하고 애플리케이션에서 이용가능하도록 만드는 명령어다.
- 또한 다수의 `--env-file` 인수를 전달할 수 있다. 후속 파일들은 이전 파일에 정의된 환경변수를 오버라이딩한다. 

```
node --env-file=.env --env-file=.development.env app.js
```

> 만약 환경과 파일에 동일한 변수가 정의된 경우 환경의 값이 우선 적용된다.

## 출처
- [How to read environment variables from Node.js](https://nodejs.org/en/learn/command-line/how-to-read-environment-variables-from-nodejs#how-to-read-environment-variables-from-nodejs)