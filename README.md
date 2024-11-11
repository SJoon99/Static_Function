# 정적 함수 추출 

### 소개
<img src="https://github.com/SJoon99/Static_Function/blob/main/image%20(1).png"  width="400" height="300"/>

StaticFunction은 **데이터셋(패키지 모음) 디렉토리**를 받아 각 파일의 확장자에 맞게 압축을 해제하고, 각 패키지의 모든 소스코드를 AST(추상 구문 트리) 분석후 **주요 유형의 함수만 추출하여 새로운 데이터셋을 만드는 툴**

---
### 주요 기능 및 목적

- 데이터셋 디렉토리 처리: 지정된 디렉토리 내의 모든 패키지를 탐색하고 처리
- 패키지 압축 해제: 파일의 확장자에 따라 적절한 방식으로 패키지를 자동으로 압축 해제
- 지원하는 확장자: .zip, .tar.gz, .tgz, .tar, .gem
- AST 분석: 해제된 패키지 내의 모든 소스코드를 AST로 파싱하여 분석
- 함수 추출: 네트워크, 파일, 프로세스 관련 주요 함수만을 추출
- 데이터셋 생성: 추출된 함수 정보를 CSV 파일로 저장하여 데이터셋 생성

---
### 각 코드 간단 설명 

- **main.py**: 프로그램의 시작점으로, dataset_dir과 outputfile을 인자로 받음.
- **dataset_processor.py**: 패키지 내의 모든 소스코드 파일을 읽어 AST를 생성하고, 패턴 매칭을 수행.
- **parser_utils.py**: AST 노드를 순회하며 지정된 패턴과 매칭되는 함수를 찾아내고, 그 결과를 저장.
- **patterns.py**: 각 프로그래밍 언어별 각 유형별 함수 패턴들을 정의.
- **config.py**: Tree-sitter 언어별 파서를 설정.
- **entrypoint.sh**: Docker 컨테이너 실행 시 가장 먼저 호출되는 스크립트, 데이터셋의 압축을 해제하고 main.py를 실행.
- **package_unpack.sh**: 데이터셋 디렉토리 내의 모든 패키지를 확장자에 따라 적절하게 압축 해제.

---
### 설치방법

1. Repository clone
   
   ```bash
   git clone https://github.com/yourusername/StaticFunction.git
   cd StaticFunction

2. Docker 이미지 빌드
   
   ```bash
   sudo docker build -t static .
---
### 사용
도커 컨테이너로 프로그램 실행
```bash
sudo docker run --rm \
  -v /path/to/your/dataset:/static/dataset \
  -v $(pwd)/output:/static/output \
  static \
  /static/dataset \
  /static/output/result.csv
```
- **/path/to/your/dataset**: 분석할 데이터셋 디렉토리의 절대 경로.
- **$(pwd)/output:/static/output**: 결과 CSV 파일이 저장될 디렉토리의 절대 경로 ( git clone시 같이 다운받아지는 현재 디렉토리의 output 디렉토리 추천 )
- **result.csv**: 데이터셋 결과 파일명은 원하는 대로 변경 가능.

---
### 윈도우 환경
1. 윈도우 WSL 환경에서 실행
   - WSL(리눅스 환경)에서 실행

2. Docker Desktop설치 후( WSL 연동 ) PowerShell에서 진행
   - PowerShell에서 리눅스와 마찬가지로 이미지 빌드, 컨테이너 실행
   - Docker Desktop사용시 윈도우 경로 그대로 사용 가능함.

```bash
docker run --rm `
  -v C:/users/tkdwn/test/Dataset:/static/dataset `
  -v ${PWD}/output:/static/output `
  static `
  /static/dataset `
  /static/output/result.csv
```
   
