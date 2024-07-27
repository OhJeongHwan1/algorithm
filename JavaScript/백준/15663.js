// Run by Node.js
const readline = require("readline");

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let n = 0;
  let m = 0;
  let numbers;

  for await (const line of rl) {
    if (n === 0) {
      [n, m] = line.split(" ").map((num) => parseInt(num));
    } else {
      numbers = line.split(" ").map((num) => parseInt(num));
      rl.close();
    }
  }
  numbers.sort((a, b) => a - b);

  const chosen = new Array(n).fill(false);
  const permutation = [];
  const output = [];

  function backtracking() {
    if (permutation.length === m) output.push(permutation.join(" "));
    else {
      chosen.forEach((bool, i) => {
        if (!bool) {
          chosen[i] = true;
          permutation.push(numbers[i]);
          backtracking();
          chosen[i] = false;
          permutation.pop();
        }
      });
    }
  }
  backtracking();
  let result = [...new Set(output)].join("\n");
  console.log(result);

  process.exit();
})();
