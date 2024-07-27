const { hostname } = require("os");
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let n = 0;
  let houses = [];

  for await (const line of rl) {
    if (n === 0) n = parseInt(line);
    else {
      const input = line.split(" ").map((num) => parseInt(num));
      houses.push(input);
      n--;
      if (n === 0) rl.close();
    }
  }
  const the_len = houses.length;
  let dp = Array.from({ length: the_len }, () => new Array(3).fill(0));
  dp[0] = houses[0];
  dp[1] = houses[1];
  dp[2] = houses[2];

  for (let i = 1; i < the_len; i++) {
    dp[i][0] = Math.min(dp[i - 1][1], dp[i - 1][2]) + houses[i][0];
    dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][2]) + houses[i][1];
    dp[i][2] = Math.min(dp[i - 1][0], dp[i - 1][1]) + houses[i][2];
  }
  console.log(Math.min(...dp[the_len - 1]));

  process.exit();
})();
