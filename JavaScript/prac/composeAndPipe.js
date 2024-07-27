const compose =
  (...functions) =>
  (initialValue) =>
    functions.reduceRight((value, func) => func(value), initialValue);

const pipe =
  (...functions) =>
  (initialValue) =>
    functions.reduce((value, func) => func(value), initialValue);

const multiplyBy2 = (x) => x * 2;
const add3 = (x) => x + 3;
const subtract1 = (x) => x - 1;

const composedFunction = compose(subtract1, add3, multiplyBy2);
const pipedFunction = pipe(multiplyBy2, add3, subtract1);

console.log(composedFunction(5)); // (5 * 2) + 3 - 1 = 12
console.log(pipedFunction(5)); // ((5 * 2) + 3) - 1 = 12
