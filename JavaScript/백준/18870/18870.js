const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "18870.txt";
const input = fs.readFileSync(filePath).toString().split("\n");
const N = parseInt(input[0]);
const array = input[1].split(" ").map(Number);

const numsMap = new Map();
const sortedArray = [...array].sort((a, b) => a - b);

let num = 0;
numsMap.set(sortedArray[0], num);

for (let i = 1; i < sortedArray.length; i++) {
  if (sortedArray[i] > sortedArray[i - 1]) num++;
  numsMap.set(sortedArray[i], num);
}

for (let i = 0; i < array.length; i++) {
  array[i] = numsMap.get(array[i]);
}

console.log(array.join(" "));
