const one = () => Promise.resolve("One!");

async function myFunc() {
  console.log("In function!");
  const res = await one();
  console.log(res);
}

console.log("Before Function!");
await myFunc();
console.log("After Function!");
