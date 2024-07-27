function partial(fn, ...presetArgs) {
  return function partiallyApplied(...laterArgs) {
    return fn(...presetArgs, ...laterArgs);
  };
}

const adder = (a, b) => a + b;
const add10 = partial(adder, 10);

console.log(add10(20));
