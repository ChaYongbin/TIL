# [환경설정] iOS Crash Worker

> 이 내용은 로컬 셋팅과 관련된 내용입니다. 실제 인프라에서는 보안에 신경써야합니다. 

## 사전 설치 

```bash
sudo brew install mysql 
sudo brew install redis 
sudo brew install rabbitmq 
```

### Redis Setting 

비밀번호 설정 방법

```bash
sudo vi /usr/local/etc/redis.conf

# requirepass 부분을 주석을 지우고, 비밀번호를 설정 해 준다. 
requirepass password

redis-cli 
AUTH password
```

## 사전 실행 

```bash
brew services start mysql 
brew services start redis 
brew services start rabbitmq 
```

## 포트 확인 

mysql :: 3306 

rabbitmq :: 5672

redis :: 6379