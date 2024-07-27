// 1005 ACM Craft

const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "1005.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

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

function solution(N, buildTimes, graph, inDegree, W) {
  const dp = new Array(N + 1).fill(0);

  const queue = new Queue();
  for (let i = 1; i <= N; i++) {
    if (inDegree[i] === 0) queue.append(i); // 먼저 지을 수 있는 건물 추가
    dp[i] += buildTimes[i - 1];
  }

  while (queue.size !== 0) {
    const start = queue.pop();
    if (start === W) break;

    for (const next of graph[start]) {
      inDegree[next]--;
      dp[next] = Math.max(dp[start] + buildTimes[next - 1], dp[next]);
      if (inDegree[next] === 0) queue.append(next);
    }
  }
  console.log(dp);
  console.log(dp[W]);
}

const T = parseInt(input[0]);
let index = 1;

for (let i = 1; i <= T; i++) {
  const [N, K] = input[index].split(" ").map(Number);
  index++;
  const buildTimes = input[index].split(" ").map(Number);
  index++;
  const graph = Array.from({ length: N + 1 }, () => []);
  const inDegree = new Array(N + 1).fill(0);
  for (let j = 0; j < K; j++) {
    const [start, end] = input[index].split(" ").map(Number);
    graph[start].push(end);
    inDegree[end]++;
    index++;
  }
  // 그래프와 각 노드별 간선의 수 초기화
  const W = parseInt(input[index]);
  index++;

  solution(N, buildTimes, graph, inDegree, W);
}
