FROM python:3.9-slim

WORKDIR /static

# 필요한 시스템 패키지 설치
RUN apt-get update && \
    apt-get install -y git gcc ruby-full && \
    rm -rf /var/lib/apt/lists/*

# Python 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . /static

# 실행 권한 부여
RUN chmod +x /static/entrypoint.sh /static/package_unpack.sh

# ENTRYPOINT 설정
ENTRYPOINT ["/static/entrypoint.sh"]
