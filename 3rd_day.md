GET /v1/current?city=Seoul&unit=celsius HTTP/1.1  # [시작줄] GET 메서드 / 요청 경로 및 쿼리 스트링 / HTTP 버전
Host: api.weather.com                             # [헤더] 요청을 받는 목적지 서버의 도메인 주소
Authorization: Bearer sk-weather-abc123           # [헤더] 서버 인증을 위한 Bearer 토큰 (API 키)
Accept: application/json                          # [헤더] JSON 형식의 응답을 받겠다는 클라이언트의 요구사항