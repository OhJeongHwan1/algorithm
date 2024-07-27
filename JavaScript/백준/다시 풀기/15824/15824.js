const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "15824.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((s) => s.trim());

const n = Number(input[0]);
const scobills = input[1].split(" ").map(Number);
scobills.sort((a, b) => a - b);

console.log(n, scobills);
