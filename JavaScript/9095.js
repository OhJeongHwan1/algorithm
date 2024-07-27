const fs = require("fs");

// 입력 파일을 동기적으로 읽어와서 문자열로 변환
const input = fs.readFileSync(0);

console.log(input);
