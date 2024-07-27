// 수열과 쿼리 15
const readline = require("readline");

(async () => {
  const rl = readline.createInterface({ input: process.stdin });
  let numbers;
  for await (const line of rl) {
    numbers = line.split(" ").map(Number);
    rl.close();
  }
  console.log(numbers);
  process.exit();
})();
