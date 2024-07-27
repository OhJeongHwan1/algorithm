const readline = require("readline");
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

(async () => {
  const rl = readline.createInterface({
    input: process.stdin,
  });
  let n, m;
  const orders = [];

  for await (const line of rl) {
    if (n === undefined) [n, m] = line.split(" ").map(Number);
    else {
      orders.push(line.split(" ").map(Number));
      if (orders.length === m) rl.close();
    }
  }
  const graph = Array.from({ length: n + 1 }, () => []);
  const inDegree = new Array(n + 1).fill(0);

  orders.forEach((order) => {
    for (let i = 1; i < order[0]; i++) {
      graph[order[i]].push(order[i + 1]);
      inDegree[order[i + 1]]++;
    }
  });

  const queue = new Queue();
  const answer = [];

  for (let i = 1; i <= n; i++) {
    if (inDegree[i] === 0) queue.append(i);
  }

  while (queue.size !== 0) {
    const curr = queue.pop();
    answer.push(curr);

    graph[curr].forEach((next) => {
      inDegree[next]--;
      if (inDegree[next] === 0) queue.append(next);
    });
  }

  if (answer.length === n) answer.forEach((n) => console.log(n));
  else console.log(0);

  process.exit();
})();
