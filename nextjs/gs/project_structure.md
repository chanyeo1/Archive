[Go To Back](./gs.md)

# 프로젝트 구조

## 최상위 루트 파일

- 최상위 루트 파일은 애플리케이션 설정, 의존성 관리, 미들웨어 실행, 모니터링 툴 통합, 그리고 환경 변수를 정의하기 위해 사용한다.

|파일명|설명|
|-|-|
|next.config.js|Next.js 설정 파일|
|package.json|프로젝트 의존성과 스크립트 파일|
|instrumentation.ts||
|middleware.ts|Next.js 요청 미들웨어|
|.env|환경 변수|
|.env.local|로컬 환경 변수|
|.env.production|프로덕션 환경 변수|
|.env.development|개발 환경 변수|
|.eslintrc.json|ESLint 설정 파일|
|.gitignore|Git이 무시할 파일과 폴더를 관리하는 파일|
|next-env.d.ts|Next.js 타입스크립트 선언 파일|
|tsconfig.json|타입스크립트 설정 파일|
|jsconfig.json|자바스크립트 설정 파일|

# 참고
- [instrumentation.js](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation)