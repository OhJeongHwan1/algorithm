// 11444 피보나치 수 6 골2 ...?

const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let n;

  for await (const line of rl) {
    n = parseInt(line);
    rl.close();
  }

  const fib = new Array(n + 1).fill(0);
  fib[0] = 0;
  fib[1] = 1;

  for (let i = 2; i < n + 1; i++) {
    fib[i] = (fib[i - 1] + fib[i - 2]) % 1000000007;
  }

  console.log(fib[n]);
  process.exit();
})();
