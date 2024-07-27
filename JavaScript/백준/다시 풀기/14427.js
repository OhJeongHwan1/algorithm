// 수열과 쿼리 15
const readline = require("readline");

(async () => {
  const rl = readline.createInterface({ input: process.stdin });

  let n, m, array;
  const querys = [];

  let codeLine = 0;

  for await (const line of rl) {
    codeLine++;

    if (codeLine === 1) n = parseInt(line);
    else if (codeLine === 2) array = line.split(" ").map(Number);
    else if (codeLine === 3) m = parseInt(line);
    else {
      querys.push(line);
      if (querys.length === m) rl.close();
    }
  }

  querys.forEach((query) => {
    if (query[0] === "2") {
      const the_min = Math.min(...array);
      for (let i = 0; i < n; i++) {
        if (the_min === array[i]) {
          console.log(i + 1);
          break;
        }
      }
    } else {
      const [command, index, change] = query.split(" ").map(Number);
      array[index - 1] = change;
    }
  });

  process.exit();
})();
