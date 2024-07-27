// 괄호 제거 골4
const readline = require("readline");

// 스택의 사용하여 괄호쌍을 저장
function getBrackets(expression) {
  const bracketList = [];
  const stack = [];

  for (let i = 0; i < expression.length; i++) {
    if (expression[i] === "(") stack.push(i);
    if (expression[i] === ")") bracketList.push([stack.pop(), i]);
  }

  return bracketList;
}

(async () => {
  const rl = readline.createInterface({ input: process.stdin });

  let expression;

  for await (const line of rl) {
    expression = line;
    rl.close();
  }

  const bracketList = getBrackets(expression);
  const bracketCnt = bracketList.length;
  const resultSet = new Set();

  for (let i = 1; i < 1 << bracketCnt; i++) {
    let expressionArray = expression.split("");

    for (let j = 0; j < bracketCnt; j++) {
      if (i & (1 << j)) {
        const pos = bracketList[j];
        expressionArray[pos[0]] = ".";
        expressionArray[pos[1]] = ".";
      }
    }
    expressionArray = expressionArray.filter((ch) => ch !== ".").join("");
    resultSet.add(expressionArray);
  }

  Array.from(resultSet)
    .sort()
    .forEach((result) => console.log(result));

  process.exit();
})();
