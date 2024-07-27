// 진우의 달 여행(LARGE)
// 골 5
// dp
const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "17485.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const [N, M] = input[0].split(" ").map(Number);
const space = input.slice(1).map((row) => row.split(" ").map(Number));

function makeDp() {
  const dp = Array.from({ length: N }, () => new Array(M).fill(0));
  for (let i = 0; i < M; i++) dp[0][i] = space[0][i];

  return dp;
}

function isValid(x, y) {
  return 0 <= x && x < N && 0 <= y && y < M;
}

const downDp = makeDp();
const leftDp = makeDp();
const rightDp = makeDp();

for (let i = 1; i < N; i++) {
  for (let j = 0; j < M; j++) {
    const downToHere = [i - 1, j];
    const LeftToHere = [i - 1, j + 1];
    const rightToHere = [i - 1, j - 1];

    if (isValid(...LeftToHere) && isValid(...rightToHere)) {
      downDp[i][j] = Math.min(leftDp[i - 1][j + 1], rightDp[i - 1][j - 1]) + space[i][j];
    } else if (isValid(...LeftToHere) && !isValid(...rightToHere)) {
      downDp[i][j] = leftDp[i - 1][j + 1] + space[i][j];
    } else if (!isValid(...LeftToHere) && isValid(...rightToHere)) {
      downDp[i][j] = rightDp[i - 1][j - 1] + space[i][j];
    }

    if (isValid(...rightToHere) && isValid(...downToHere)) {
      leftDp[i][j] = Math.min(rightDp[i - 1][j - 1], downDp[i - 1][j]) + space[i][j];
    } else if (isValid(...rightToHere) && !isValid(...downToHere)) {
      leftDp[i][j] = rightDp[i - 1][j - 1] + space[i][j];
    } else if (!isValid(...rightToHere) && isValid(...downToHere)) {
      leftDp[i][j] = downDp[i - 1][j] + space[i][j];
    }

    if (isValid(...LeftToHere) && isValid(...downToHere)) {
      rightDp[i][j] = Math.min(leftDp[i - 1][j + 1], downDp[i - 1][j]) + space[i][j];
    } else if (isValid(...LeftToHere) && !isValid(...downToHere)) {
      rightDp[i][j] = leftDp[i - 1][j + 1] + space[i][j];
    } else if (!isValid(...LeftToHere) && isValid(...downToHere)) {
      rightDp[i][j] = downDp[i - 1][j] + space[i][j];
    }
  }
}

console.log(Math.min(...downDp[N - 1], ...leftDp[N - 1], ...rightDp[N - 1]));
