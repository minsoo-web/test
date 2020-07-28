new Vue({
  el: "#app",
  data: function () {
    return {
      myChoice: null,
      count: 3,
      gameStart: false,
      comChoice: null,
      winner: "",
      lifeOfMe: 3,
      lifeOfCom: 3,
      logs: [],
      selects: [
        {
          name: "가위",
          value: "scissors",
        },
        {
          name: "바위",
          value: "rock",
        },
        {
          name: "보",
          value: "paper",
        },
      ],
    };
  },
  computed: {
    myChoiceImg: function () {
      return this.myChoice == null
        ? "images/question.jpg"
        : `images/${this.myChoice}.jpg`;
    },
    comChoiceImg: function () {
      return this.comChoice == null
        ? "images/question.jpg"
        : `images/${this.comChoice}.jpg`;
    },
    leftLifeOfMe: function () {
      return 3 - this.lifeOfMe;
    },
    leftLifeOfCom: function () {
      return 3 - this.lifeOfCom;
    },
  },
  watch: {
    count: function (newVal) {
      if (newVal === 0) {
        this.selectCom();
        this.whoisWin();
        this.updateLogs();

        // 다음게임
        this.gameStart = false;
        this.count = 3;
      }
    },
    lifeOfMe: function (newVal) {
      if (newVal === 0) {
        this.endGame("안타깝습니다, 당신이 졌습니다.");
      }
    },
    lifeOfCom: function (newVal) {
      if (newVal === 0) {
        this.endGame("축하드립니다, 당신이 승리하였습니다.");
      }
    },
  },
  methods: {
    startGame() {
      if (this.myChoice == null) {
        alert("가위 / 바위 / 보 중 하나를 선택해주세요");
      } else {
        if (!this.gameStart) {
          this.gameStart = true;
          let countDown = setInterval(() => {
            this.count--;
            if (this.count == 0) {
              clearInterval(countDown);
            }
          }, 1000);
        } else {
          alert("실행중");
        }
      }
    },
    selectCom() {
      // 컴퓨터가 가위바위보를 선택
      let number = Math.random(); // 0 ~ 1
      if (number < 0.33) {
        this.comChoice = "rock";
      } else if (number < 0.66) {
        this.comChoice = "scissors";
      } else {
        this.comChoice = "paper";
      }
    },
    whoisWin() {
      // 가위바위보 승패 결정
      if (this.myChoice == this.comChoice) this.winner = "no one";
      else if (this.myChoice == "rock" && this.comChoice == "paper")
        this.winner = "com";
      else if (this.myChoice == "rock" && this.comChoice == "scissors")
        this.winner = "me";
      else if (this.myChoice == "paper" && this.comChoice == "rock")
        this.winner = "me";
      else if (this.myChoice == "paper" && this.comChoice == "scissors")
        this.winner = "com";
      else if (this.myChoice == "scissors" && this.comChoice == "rock")
        this.winner = "com";
      else if (this.myChoice == "scissors" && this.comChoice == "paper")
        this.winner = "me";
      else this.winner = "error";
      // 몫이 차감
      if (this.winner == "me") {
        this.lifeOfCom--;
      } else if (this.winner == "com") {
        this.lifeOfMe--;
      }
    },
    updateLogs() {
      let log = {
        winner: this.winner,
        msg: `You : ${this.myChoice} VS Com : ${this.comChoice}`,
      };
      this.logs.unshift(log);
    },
    endGame(msg) {
      setTimeout(() => {
        confirm(msg);
        // 초기화
        this.lifeOfMe = 3;
        this.lifeOfCom = 3;
        this.myChoice = null;
        this.comChoice = null;
        this.winner = null;
        this.logs = [];
      }, 500);
    },
  },
});
