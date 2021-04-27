# TravelMate

코로나로 인해 세계 각국의 해외 입국 규정이 변경되었다. 입국 규정을 한 눈에 알아보기 위해 만든 웹 사이트다.

## Getting Started / 어떻게 시작하나요?

Docker-compose.yml 파일을 실행시키면 자동적으로 모든 것이 실행 될 것이다.
powershell을 관리자 모드로 실행 시킨 후 "Docker-compose up" 명령어를 입력해주면 된다.

### Prerequisites / 선행 조건

아래 사항들이 설치가 되어있어야합니다.

```
위에 폴더 중 database 폴더는 꼭 다운로드 받아야한다. (compose 시 필요하다.)
```

### Installing / 설치

아래 사항들로 현 프로젝트에 관한 모듈들을 설치할 수 있습니다.

```
(선택) Docker Desktop이 설치되어 있으면 좀 더 한 눈에 컨테이너들이 실행 되는 것을 확인할 수 있다.
```

## Running the tests / 테스트의 실행

관리자 권한으로 powershell 실행 후 docker-compose.yml 파일 경로로 들어가 "docker-compose up" 명령어만 입력해준다.

### 테스트는 이런 식으로 동작합니다

왜 이렇게 동작하는지, 설명합니다

```
1. 가장 먼저 MySQL 기반의 도커 컨테이너가 올라간다.
2. 컨테이너 이름은 database이고, 해당 컨테이너는 같은 경로의 db.env 파일을 통해 환경 변수를 설정한다.
3. 볼륨 설정으로 인해 좀 전에 다운로드 받은 database 폴더를 docker-compose.yml 파일과 같은 경로에 넣는다.
4. depends_on에 의해 python3 기반의 컨테이너인 crawler가 실행되고 외교부 사이트에 기록된 나라별 출입국 규정을 크롤링해서 DB컨테이너에 저장해준다.
5. 크롤링을 실행하는 주기는 crawler.py 파일을 통해 수정할 수 있다.
6. 마지막으로 webapp 컨테이너는 ubuntu 기반으로 flask를 통해 웹 사이트를 제작했다.
7. folium library를 통해 지도를 제작했고, 플라스크에서 제공하는 무료 템플릿을 통해 웹 페이지를 꾸밀 수 있었다.
8. 지도에 뜨는 아이콘을 클릭하면 각 나라별(50개국) 해당 출입국 규정을 볼 수 있는 웹 사이트로 넘어가는 것을 확인할 수 있다.
9. 원하는 나라를 클릭하여 출입국 규정을 살펴보자!
```

### 테스트는 이런 식으로 작성하시면 됩니다

```
혹시 자기만의 색깔로 커스터마이징을 하시고 싶은분들이 있을 수도 있어 컨테이너를 제작할 때 사용했던 코드도 전부 올렸다.
```

## Deployment / 배포

Add additional notes about how to deploy this on a live system / 라이브 시스템을 배포하는 방법

## Built With / 누구랑 만들었나요?

* [이름](링크) - 무엇 무엇을 했어요
* [Name](Link) - Create README.md

## Contributiong / 기여

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us. / [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) 를 읽고 이에 맞추어 pull request 를 해주세요.

## License / 라이센스

This project is licensed under the MIT License - see the [LICENSE.md](https://gist.github.com/PurpleBooth/LICENSE.md) file for details / 이 프로젝트는 MIT 라이센스로 라이센스가 부여되어 있습니다. 자세한 내용은 LICENSE.md 파일을 참고하세요.

## Acknowledgments / 감사의 말

* Hat tip to anyone whose code was used / 코드를 사용한 모든 사용자들에게 팁
* Inspiration / 영감
* etc / 기타
