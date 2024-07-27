const readline = require("readline");
const MOVES = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

function spreadDust(r, c, map) {
  const blankMap = Array.from({ length: r }, () => new Array(c).fill(0)); // 빈 배열 선언
  for (let x = 0; x < r; x++) {
    for (let y = 0; y < c; y++) {
      if (map[x][y] >= 5) {
        const spreadAmount = Math.floor(map[x][y] / 5); //확산될 값
        // 상하좌우로 반복
        MOVES.forEach((move) => {
          const nx = x + move[0];
          const ny = y + move[1];
          if (0 <= nx && nx < r && 0 <= ny && ny < c) {
            if (map[nx][ny] !== -1) {
              map[x][y] -= spreadAmount;
              blankMap[nx][ny] += spreadAmount;
            }
          }
        });
      }
    }
  }

  for (let x = 0; x < r; x++) {
    for (let y = 0; y < c; y++) {
      map[x][y] += blankMap[x][y]; // 두 배열을 더함
    }
  }
}
function getAirCleanerIndex(map) {
  for (let x = 0; x < map.length; x++) {
    if (map[x][0] === -1) return [x, x + 1];
  }
}

function operateAirCleaner(map, r, c, top, bottom) {
  for (let x = top - 1; x > 0; x--) map[x][0] = map[x - 1][0];
  for (let y = 0; y < c - 1; y++) map[0][y] = map[0][y + 1];
  for (let x = 0; x < top; x++) map[x][c - 1] = map[x + 1][c - 1];
  for (let y = c - 1; y > 1; y--) map[top][y] = map[top][y - 1];
  map[top][1] = 0;

  for (let x = bottom + 1; x < r - 1; x++) map[x][0] = map[x + 1][0];
  for (let y = 0; y < c - 1; y++) map[r - 1][y] = map[r - 1][y + 1];
  for (let x = r - 1; x > bottom; x--) map[x][c - 1] = map[x - 1][c - 1];
  for (let y = c - 1; y > 1; y--) map[bottom][y] = map[bottom][y - 1];
  map[bottom][1] = 0;
}

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  let r, c, t;
  let codeLine = 0;
  const map = [];

  for await (const line of rl) {
    codeLine++;
    if (codeLine === 1) [r, c, t] = line.split(" ").map(Number);
    else {
      map.push(line.split(" ").map(Number));
      if (codeLine === r + 1) rl.close();
    }
  }
  const [top, bottom] = getAirCleanerIndex(map);

  for (let i = 1; i <= t; i++) {
    spreadDust(r, c, map);
    operateAirCleaner(map, r, c, top, bottom);
  }
  let cnt = 0;
  for (let x = 0; x < map.length; x++) {
    for (let y = 0; y < map[0].length; y++) {
      if (map[x][y] !== -1) cnt += map[x][y];
    }
  }

  console.log(cnt);
  process.exit();
})();
