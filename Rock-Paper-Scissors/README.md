# 가위바위보 게임 만들기

[맨땅에 개발하기님 유튜브 채널](https://www.youtube.com/watch?v=rhzpf8h66ri&list=plzzsdj89scn38keadqvtiha8gz-kgptoc&index=1)의 재생 목록을 보며 따라 만들어 봤습니다.

## 프로젝트 세팅

CSS, images 그리고 index.html 은 _맨땅에 개발하기_ 님이 공유해주신 코드를 그대로 이용한 것입니다.

## 3강 Vue Instance 생성 및 data binding

1. Vue Instance 생성
2. 선택한 radio에 따라 image를 변경하는 작업

radio에 `v-model` 속성을 주어 data를 변경할 수 있게 해주고  
image 태그의 src 속성에 `v-bind:src` 로 선택된 radio 값을 받아 binding 해주었습니다.

## 4강 Methods 내 게임 시작 함수 생성

1. 선택완료 버튼을 누르면 countDown을 하게 한다.

button 태그에 `v-on:click (@click)` 속성을 통해 Methods를 실행시키게 연결합니다.  
count 데이터를 선언 한 뒤 `setInterval()` 메서드를 활용해 count를 1초마다 감소시키게 해주었습니다.

> 여기서 button을 더블클릭, 또는 실행중 클릭을 한 번 더 하게 되면 1초에 2씩 감소가 됩니다.
> 또한 0이 되어도 count를 계속 깎아 버리는 오류가 발견되어 영상과는 조금 다르게 작성했습니다.

우선 gameStart 변수를 false로 설정해 !this.gameStart 일때만 실행되게 설정한 뒤  
count가 0이 되면 `clearInterval()` 을 통해 음수 값을 출력하지 않게 했습니다.

## 5강 컴퓨터의 선택 watch로 실행하기

1. count가 0이 되면 컴퓨터의 선택을 보여주는 작업

count가 0이 되었을때 함수를 정의해서 clearInterval()이 있는 코드에 사용해도 되지만  
Vue.js의 `watch` 기능을 활용해 0이 되는 것을 감지하여 함수를 실행하도록 하였습니다.

`Math.random()` 을 사용해 0.33 ~ 0.66 ~ 1 의 구간 별로 가위 바위 보를 정해주었습니다.

## 6강 count 리셋 및 v-for를 활용한 로그 리스트 출력

1. count를 0으로 바꿔줍니다.
2. 선택을 하고 나면 `선택 완료` 버튼을 다시 누를 수 없도록 하고 `기다리는 중` 을 보여줍니다.
3. 결과들을 담을 데이터를 선언해주고 배열에 담고 데이터를 바인딩해서 `v-for`로 보여줍니다.

4강에서 발견한 에러를 6강에서 해결해주셨습니다.  
제가 해결한 방식과 유사한 방법으로 주셔서 ~~살짝 뿌듯했습니다.~~

## 7강 클래스 바인딩을 활용한 스타일링

1. 내가 이겼을때와 컴퓨터가 이겼을때의 로그 색상을 구별하고 싶습니다.
2. log를 스트링에서 객체 타입으로 변경
3. 클래스 바인딩을 통해 데이터를 클래스 이름으로 변경해주었습니다.

this.winner = 'me' 를  
this.result = 'win' 으로 바꿔서  
:class="log.result" + '-log' 이렇게 하는 방법을 생각했는데

```html
<li
  v-for="log in logs"
  :class="{
        'win-log' : log.winner == 'me'
        'draw-log' : log.winner == 'no one'
        'defeat-log' : log.winner == 'com'
        }"
>
  {{log.msg}}
</li>
```

## 8강 게임 마치기

1. watch 를 사용해 life가 0이 되면 초기화 해주는 작업을 해주었습니다.

## 9강 리펙토링

1. 어떤 조건에 따라서 다른 값을 보여주면 된다 => computed 도입
2. 반복되는 코드 -> v-for
3. 함수 코드 모듈화 -> methods:{}
