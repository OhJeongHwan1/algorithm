// 9663 N-QUEEN

const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let n = 0;
  let answer = 0;
  const queens = [];

  for await (const line of rl) {
    n = parseInt(line);
    rl.close();
  }

  function check(row, i) {
    for (const [x, y] of queens) {
      if (x === row || y === i) return false;
      if (Math.abs(x - row) === Math.abs(y - i)) return false;
    }
    return true;
  }

  function backtracking(row) {
    if (row === n) {
      answer += 1;
      return;
    }
    for (let i = 0; i < n; i++) {
      if (check(row, i)) {
        queens.push([row, i]);
        backtracking(row + 1);
        queens.pop();
      }
    }
  }

  backtracking(0);

  console.log(answer);

  process.exit();
})();
