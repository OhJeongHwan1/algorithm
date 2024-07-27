// 줄세우기 골 4
const readline = require("readline");

(async () => {
  const rl = readline.createInterface({ input: process.stdin });
  let n;
  const numbers = [];
  for await (const line of rl) {
    if (n === undefined) n = parseInt(line);
    else {
      numbers.push(parseInt(line));
      if (numbers.length === n) rl.close();
    }
  }
  const dp = new Array(n).fill(1);

  for (let i = 1; i < n; i++) {
    for (let j = i; j > 0; j--) {
      if (numbers[i] > numbers[i - j] && dp[i] < dp[i - j] + 1) {
        dp[i] = dp[i - j] + 1;
      }
    }
  }

  console.log(n - Math.max(...dp));
  process.exit();
})();
