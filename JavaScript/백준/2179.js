// 2179 비슷한 단어 골4

const readline = require("readline");

(async () => {
  const rl = readline.createInterface({
    input: process.stdin,
  });

  let n;
  const wordsIndex = [];
  let index = 0;
  for await (const line of rl) {
    if (n === undefined) n = parseInt(line);
    else {
      wordsIndex.push([line, index]);
      index++;
      if (wordsIndex.length === n) rl.close();
    }
  }

  wordsIndex.sort();
  const words = wordsIndex.map((list) => list[0]);
  let resultList = [];
  let maxLen = 0;

  for (let i = 0; i < words.length - 1; i++) {
    for (let j = i + 1; j < words.length; j++) {
      if (words[i][0] !== words[j][0]) break;
      let cnt = 0;
      for (let k = 0; k < words[i].length; k++) {
        if (words[i][k] === words[j][k]) cnt++;
        else break;
      }
      if (cnt > maxLen) {
        maxLen = cnt;
        resultList = [[wordsIndex[i], wordsIndex[j]].sort((a, b) => a[1] - b[1])];
      } else if (cnt == maxLen) {
        resultList.push([wordsIndex[i], wordsIndex[j]].sort((a, b) => a[1] - b[1]));
      }
    }
  }
  resultList.sort((a, b) => {
    if (a[0][1] === b[0][1]) return a[1][1] - b[1][1];
    else return a[0][1] - b[0][1];
  });
  const result = resultList[0].map((list) => list[0]).join("\n");
  console.log(result);

  process.exit();
})();
