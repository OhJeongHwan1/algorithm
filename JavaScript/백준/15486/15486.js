// 퇴사 2 골5
// dp 문제이다.
// 아마 탑다운 바텀업 두 가지 방식이 있을 것 같다.

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "15486.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(input[0]);
const consultings = input.slice(1).map((c) => c.split(" ").map(Number));
const times = consultings.map((list) => list[0]); // 시간 배열
const pays = consultings.map((list) => list[1]); // 금액 배열
const dp = new Array(N + 1).fill(0);

for (let i = 0; i < N; i++) {
  if (i !== 0) dp[i] = Math.max(dp[i - 1], dp[i]);
  const next = i + times[i];
  if (next <= N) {
    dp[next] = Math.max(dp[next], dp[i] + pays[i]);
  }
}

console.log(Math.max(dp[N], dp[N - 1])); // 하루 일을 마치고 금액이 추가되기 때문에 N+1 까지 확인
