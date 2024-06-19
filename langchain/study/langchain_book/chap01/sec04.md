[Go To Back](../../study.md)

## 환경 변수에 API 키 설정하기

### 윈도우
- [시작] 메뉴 → **"PowerShell"** 실행
- 아래 명령어 입력
```
[System.Environment]::SetEnvironmentVariable('OPENAI_API_KEY', 'sk-xxxxxxxxxx', 'User')
```
- **PowerShell** 재실행 후 아래 명령어 입력
```
echo $env:OPENAI_API_KEY
```

### macOS
- `.zshrc` 파일은 `zsh` 셸이 실행될 때마다 읽히는 설정 파일
- [응용프로그램] 폴더 → [유틸리티] 폴더 → [터미널] 실행
- 아래 명령어 입력
```
touch ~/.zshrc  # 존재하지 않으면 새로운 파일을 생성
```
- `OPENAI_API_KEY` 환경 변수를 `.zshrc` 파일에 추가
```
echo 'export OPENAI_API_KEY="sk-xxxxxxxxxx"' >> ~/.zshrc
```
- `.zshrc` 파일에 변경 사항을 적용하기 위해 `Z` 셸 리로드
```
source ~/.zshrc
```
- `OPENAI_API_KEY` 환경 변수 확인
```
echo $OPENAI_API_KEY
```

### 랭체인과 필요한 라이브러리 준비하기
- `pip` 명령어는 파이썬 라이브러리 설치 도구

**윈도우**
```
wget https://raw.githubusercontent.com/wikibook/langchain/master/requirements.txt -OutFile requirements.txt

python3 -m pip install -r requirements.txt

# 랭체인에서 OpenAI의 언어 모델을 호출하기 위해 openai 패키지 설치
python3 -m pip install openai==0.28 
```
