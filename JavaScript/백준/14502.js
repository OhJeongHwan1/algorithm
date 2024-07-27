// 연구소 골4
const readline = require("readline");
const MOVE = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

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
  size() {
    return this.size;
  }
}

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let n, m;
  const the_map = [];
  const map_set = new Set(); // 중복되는 맵을 제거하기 위해 set 을 사용
  const virus = [];
  const empty = [];
  const cases = [];
  let answer = 0;

  for await (const line of rl) {
    if (n === undefined) [n, m] = line.split(" ").map(Number);
    else {
      the_map.push(line.split(" ").map(Number));
      if (the_map.length === n) rl.close();
    }
  }

  for (let x = 0; x < n; x++) {
    for (let y = 0; y < m; y++) {
      if (the_map[x][y] === 2) virus.push([x, y]);
      if (the_map[x][y] === 0) empty.push([x, y]);
    }
  }

  function backTracking() {
    if (cases.length === 3) {
      const new_map = the_map.map((row) => [...row]);
      cases.forEach((the_case) => {
        const [x, y] = empty[the_case];
        new_map[x][y] = 1;
      });
      map_set.add(new_map);
    } else {
      for (let i = 0; i < empty.length; i++) {
        let length = cases.length;
        if (!cases.includes(i) && (length === 0 || cases[length - 1] < i)) {
          cases.push(i);
          backTracking();
          cases.pop();
        }
      }
    }
  }

  backTracking();

  function getCnt(map) {
    let cnt = 0;
    for (let x = 0; x < n; x++) {
      for (let y = 0; y < m; y++) {
        if (map[x][y] === 0) cnt++;
      }
    }
    return cnt;
  }

  function bfs(new_map, queue) {
    while (queue.size !== 0) {
      [cx, cy] = queue.pop();

      for (const [dx, dy] of MOVE) {
        [nx, ny] = [cx + dx, cy + dy];
        if (0 <= nx && nx < n && 0 <= ny && ny < m) {
          if (new_map[nx][ny] === 0) {
            new_map[nx][ny] = 2;
            queue.append([nx, ny]);
          }
        }
      }
    }
  }

  for (const new_map of map_set) {
    const queue = new Queue();
    virus.forEach((v) => queue.append(v));
    bfs(new_map, queue);
    const cnt = getCnt(new_map);

    answer = cnt > answer ? cnt : answer;
  }
  console.log(answer);
  process.exit();
})();
