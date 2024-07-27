// 2225 합분해 dp
// dp 점화식 떠올리기가 너무 힘들다.
const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "2225.txt";
const [n, k] = fs.readFileSync(filePath).toString().split(" ").map(Number);

const dp = Array.from({ length: k + 1 }, () => new Array(n + 1).fill(0));
for (let i = 0; i < n + 1; i++) dp[1][i] = 1;
for (let i = 0; i < k + 1; i++) dp[i][0] = 1;

for (let i = 1; i < k + 1; i++) {
  for (let j = 1; j < n + 1; j++) {
    dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000;
  }
}

console.log(dp[k][n]);
