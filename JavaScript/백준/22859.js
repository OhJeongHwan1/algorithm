// 22859 HTML 파싱 골3

const readline = require("readline");

// main 삭제
function deleteMain(input) {
  return input.slice(6, -7);
}
// div 의 title 파싱
function getTitle(divBlock) {
  return divBlock.split('"')[1];
}
// p 태그 안의 문자열 반환
function getPtag(divBlock) {
  return divBlock
    .split("<p>")
    .slice(1)
    .map((ptag) => ptag.split("</p>")[0]);
}

function deleteTags(pBlock) {
  let isTag = false;
  const pBlockArray = pBlock.split("");

  // 태그 제거.
  for (let i = 0; i < pBlockArray.length; i++) {
    if (pBlockArray[i] === "<") isTag = true;
    if (pBlockArray[i] === ">") {
      isTag = false;
      pBlockArray[i] = null;
    }
    if (isTag === true) pBlockArray[i] = null;
  }

  const deleteTagArray = pBlockArray.filter((str) => str !== null);

  let isBlank = false;
  // 중복되는 공백 제거: 공백은 문자 사이 1번만 존재할 수 있음.
  for (let i = 0; i < deleteTagArray.length - 1; i++) {
    if (isBlank === true && deleteTagArray[i] === " ") deleteTagArray[i] = null;
    else if (deleteTagArray[i] === " ") isBlank = true;
    else isBlank = false;
  }

  return deleteTagArray
    .filter((str) => str !== null)
    .join("")
    .trim();
}

(async () => {
  const rl = readline.createInterface({
    input: process.stdin,
  });

  let input;

  for await (const line of rl) {
    input = line;
    rl.close();
  }

  const divArray = deleteMain(input).split("</div>");
  const resultString = divArray
    .map((divBlock) => {
      if (divBlock.length === 0) return "";
      let outString = `title : ${getTitle(divBlock)}\n`;

      const pArray = getPtag(divBlock);

      outString += pArray.map((pBlock) => deleteTags(pBlock)).join("\n");

      return outString;
    })
    .join("\n");

  process.stdout.write(resultString);

  process.exit();
})();
