const readline = require("readline");
const DIRECTIONS = Object.freeze(["right", "bottom", "left", "top"]);

///////////////////////////
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}
// 연결 리스트로 큐 구현
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
///////////////////////////
(async () => {
  let rl = readline.createInterface({ input: process.stdin });
  let n = 0;
  let k = 0;
  let l = 0;
  const apples = [];
  const moves = [];

  let lineCount = 0; // 입력을 돕기 위한 변수

  for await (const line of rl) {
    lineCount++;
    if (lineCount === 1) {
      n = parseInt(line);
    } else if (lineCount === 2) {
      k = parseInt(line);
    } else if (lineCount >= 3 && lineCount < 3 + k) {
      apples.push(line.split(" ").map((n) => parseInt(n) - 1));
    } else if (lineCount === 3 + k) {
      l = parseInt(line);
    } else if (lineCount > 3 + k && lineCount <= 3 + k + l) {
      moves.push(line.split(" ").map((n, i) => (i === 0 ? parseInt(n) : n)));
    }
    if (lineCount === 3 + k + l) rl.close();
  }

  const map = Array.from({ length: n }, () => new Array(n).fill(null)); // map 초기화
  const moveSet = new Set(moves.map((move) => move[0])); // 움직일 시간 set 선언

  map[0][0] = "S"; // 시작 위치 설정
  // 사과 위치 설정
  apples.forEach((apple) => {
    const [row, column] = apple;
    map[row][column] = "A";
  });

  let direction = 0; // 방향 변수 선언
  const queue = new Queue(); //뱀의 몸통을 요소로 가질 큐 선언
  queue.append([0, 0]);
  let x = 0;
  let y = 0;
  let time = 0;

  while (true) {
    time++;
    if (DIRECTIONS[direction] === "right") y++;
    else if (DIRECTIONS[direction] === "bottom") x++;
    else if (DIRECTIONS[direction] === "left") y--;
    else if (DIRECTIONS[direction] === "top") x--;

    if (!(0 <= x && x < n && 0 <= y && y < n)) break;

    if (map[x][y] === "S") break; // 자기 자신을 만나는 경우

    if (map[x][y] === "A") {
      queue.append([x, y]); // 사과를 먹고 길이 증가
      map[x][y] = "S";
    } else {
      queue.append([x, y]); // 사과를 먹지 못하는 경우 이동
      map[x][y] = "S";
      const [rX, rY] = queue.pop(); // 큐에서 제거하는 값이 뱀의 꼬리의 위치
      map[rX][rY] = null;
    }
    if (moveSet.has(time)) {
      const move = moves.shift(); // 현재 시간이 방향을 전환하는 시간이면 방향 전환
      if (move[1] === "D") direction = direction + 1 > 3 ? 0 : direction + 1;
      if (move[1] === "L") direction = direction - 1 < 0 ? 3 : direction - 1;
    }
  }

  console.log(time);

  process.exit();
})();
