const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "21276.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((s) => s.trim());

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }
  append(value) {
    const newNode = new Node(value);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.size++;
  }
  pop() {
    if (!this.head) return null;
    const reMoveNode = this.head;
    this.head = this.head.next;
    if (!this.head) {
      this.tail = null;
    }
    this.size--;
    return reMoveNode.value;
  }
}

function showAncestor(ancestors) {
  return console.log(ancestors.length + "\n" + [...ancestors].sort().join(" "));
}

function showResult(resultList) {
  return console.log(resultList.sort().join("\n"));
}
let n, m, peoples;
const relations = new Map();
const inDegree = new Map();
let cnt = 0;

for (const line of input) {
  if (!n) n = parseInt(line);
  else if (!peoples) {
    peoples = line.split(" ");
    peoples.forEach((people) => {
      relations.set(people, []);
      inDegree.set(people, 0);
    });
  } else if (!m) m = parseInt(line);
  else {
    const [descendants, ancestor] = line.split(" ");

    const list = relations.get(ancestor);
    list.push(descendants);
    relations.set(ancestor, list);

    const num = inDegree.get(descendants);
    inDegree.set(descendants, num + 1);
  }
}

const queue = new Queue();
const ancestors = [];

for (const [key, value] of inDegree) {
  if (value === 0) {
    queue.append(key);
    ancestors.push(key);
  }
}

showAncestor(ancestors);
const resultList = [];

while (queue.size !== 0) {
  const sup = queue.pop();
  const subs = [];
  for (const sub of relations.get(sup)) {
    inDegree.set(sub, inDegree.get(sub) - 1);
    if (inDegree.get(sub) === 0) {
      subs.push(sub);
      queue.append(sub);
    }
  }
  resultList.push(`${sup} ${subs.length} ${subs.sort().join(" ")}`);
}
showResult(resultList);
