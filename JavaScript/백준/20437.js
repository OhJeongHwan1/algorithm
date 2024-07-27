// 문자열 게임 2 골드 5
const readline = require("readline");

(async () => {
  const rl = readline.createInterface({ input: process.stdin });

  let t;
  const testCase = [];
  let input = [];
  // 입력
  for await (const line of rl) {
    if (t === undefined) t = parseInt(line);
    else {
      input.push(input.length === 0 ? line : parseInt(line));
      if (input.length === 2) {
        testCase.push(input);
        input = [];
      }
      if (testCase.length === t) rl.close();
    }
  }
  //
  const resultList = [];

  for (const [w, k] of testCase) {
    const map = new Map();
    let min = 10001;
    let max = 0;
    for (let i = 0; i < w.length; i++) {
      if (!map.has(w[i])) map.set(w[i], [i]);
      else {
        const alp_list = map.get(w[i]);
        alp_list.push(i);
        map.set(w[i], alp_list);
      }
    }
    console.log("map:", map);
    const filterdMap = new Map([...map].filter(([key, value]) => value.length >= k));
    console.log("filterdMap:", filterdMap);
    if (filterdMap.size === 0) resultList.push(-1);
    else {
      filterdMap.forEach((list) => {
        for (let i = list.length - 1; i >= k - 1; i--) {
          const len = list[i] - list[i - k + 1] + 1;
          min = min > len ? len : min;
          max = max < len ? len : max;
        }
      });
      resultList.push([min, max].join(" "));
    }
  }
  resultList.forEach((result) => console.log(result));

  process.exit();
})();
