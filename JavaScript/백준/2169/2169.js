// 로봇 조정하기 골2 dp
// 사실 이런 문제 처음에 아이디어 떠올리기 너무 어려움.

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "2169.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((s) => s.trim());

const [n, m] = input[0].split(" ").map(Number);
const marsMap = input.slice(1).map((line) => line.split(" ").map(Number));

const dp = Array.from({ length: n }, () => new Array(m).fill(-Infinity));
dp[0][0] = marsMap[0][0];

//첫 행은 오른쪽으로 이동하며 채우기
for (let j = 1; j < m; j++) {
  dp[0][j] = dp[0][j - 1] + marsMap[0][j];
}

for (let i = 1; i < n; i++) {
  // 왼쪽에서 오른쪽으로 이동하는 경우
  const leftToRight = Array(m).fill(-Infinity);
  leftToRight[0] = dp[i - 1][0] + marsMap[i][0];
  for (let j = 1; j < m; j++) {
    leftToRight[j] = Math.max(leftToRight[j - 1], dp[i - 1][j]) + marsMap[i][j];
  }

  // 오른쪽에서 왼쪽으로 이동하는 경우
  const rightToLeft = Array(m).fill(-Infinity);
  rightToLeft[m - 1] = dp[i - 1][m - 1] + marsMap[i][m - 1];
  for (let j = m - 2; j >= 0; j--) {
    rightToLeft[j] = Math.max(rightToLeft[j + 1], dp[i - 1][j]) + marsMap[i][j];
  }

  // 현재 행의 최종 값 결정
  for (let j = 0; j < m; j++) {
    dp[i][j] = Math.max(leftToRight[j], rightToLeft[j]);
  }
}

console.log(dp[n - 1][m - 1]);
