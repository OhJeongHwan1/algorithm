// 구슬 탈출 2 골1
// 가장 어려웠던 시뮬레이션 문제
// bfs 를 사용한 풀이도 보자
const fs = require("fs");
const filePath = process.platform === "linux" ? 0 : "13460.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const [N, M] = input[0].split(" ").map(Number);
const board = input.slice(1).map((row) => row.trim().split(""));
let ans = Infinity;
let ansDirect;

function findBalls() {
  let [rx, ry, bx, by] = [0, 0, 0, 0];
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (board[i][j] === "R") [rx, ry] = [i, j];
      if (board[i][j] === "B") [bx, by] = [i, j];
    }
  }
  return [rx, ry, bx, by];
}

function moveTop(rx, ry, bx, by, b, num, direct) {
  if (num > Math.min(10, ans)) return;
  const board = b.map((row) => [...row]);
  [board[bx][by], board[rx][ry]] = [".", "."];

  if (ry === by) {
    if (rx > bx) {
      let len = 0;
      for (let i = 1; i <= bx; i++) {
        if (board[bx - i][by] === "O") return;
        if (board[bx - i][by] === "#") {
          len = i - 1;
          break;
        }
      }
      [board[bx - len][by], bx] = ["B", bx - len];

      for (let i = 1; i <= rx; i++) {
        if (board[rx - i][ry] === "O") {
          if (ans > num) {
            ans = num;
            ansDirect = direct;
          }

          return;
        }
        if (board[rx - i][ry] === "#" || board[rx - i][ry] === "B") {
          len = i - 1;
          break;
        }
      }
      [board[rx - len][ry], rx] = ["R", rx - len];
    }
    if (bx > rx) {
      let len = 0;
      let find = false;
      for (let i = 1; i <= rx; i++) {
        if (board[rx - i][ry] === "O") {
          find = true;
          break;
        }
        if (board[rx - i][ry] === "#") {
          len = i - 1;
          break;
        }
      }
      if (!find) [board[rx - len][ry], rx] = ["R", rx - len];
      for (let i = 1; i <= bx; i++) {
        if (board[bx - i][by] === "O") return;
        if (board[bx - i][by] === "#" || board[bx - i][by] === "R") {
          len = i - 1;
          break;
        }
      }
      if (find === true) {
        if (ans > num) {
          ans = num;
          ansDirect = direct;
        }

        return;
      }
      [board[bx - len][by], bx] = ["B", bx - len];
    }
  } else {
    let rlen = 0;
    let blen = 0;

    for (let i = 1; i <= bx; i++) {
      if (board[bx - i][by] === "O") return;
      if (board[bx - i][by] === "#") {
        blen = i - 1;
        break;
      }
    }
    for (let i = 1; i <= rx; i++) {
      if (board[rx - i][ry] === "O") {
        if (ans > num) {
          ans = num;
          ansDirect = direct;
        }

        return;
      }
      if (board[rx - i][ry] === "#") {
        rlen = i - 1;
        break;
      }
    }
    [board[bx - blen][by], board[rx - rlen][ry]] = ["B", "R"];
    [bx, rx] = [bx - blen, rx - rlen];
  }

  moveTop(rx, ry, bx, by, board, num + 1, direct + "U");
  moveBottom(rx, ry, bx, by, board, num + 1, direct + "D");
  moveLeft(rx, ry, bx, by, board, num + 1, direct + "L");
  moveRight(rx, ry, bx, by, board, num + 1, direct + "R");
}

function moveBottom(rx, ry, bx, by, b, num, direct) {
  if (num > Math.min(10, ans)) return;
  const board = b.map((row) => [...row]);
  [board[bx][by], board[rx][ry]] = [".", "."];

  if (ry === by) {
    if (rx > bx) {
      let len = 0;
      let find = false;
      for (let i = 1; i < N - rx; i++) {
        if (board[rx + i][ry] === "O") {
          find = true;
          return;
        }
        if (board[rx + i][ry] === "#") {
          len = i - 1;
          break;
        }
      }
      if (!find) [board[rx + len][ry], rx] = ["R", rx + len];

      for (let i = 1; i < N - bx; i++) {
        if (board[bx + i][by] === "O") return;
        if (board[bx + i][by] === "#" || board[bx + i][by] === "R") {
          len = i - 1;
          break;
        }
      }
      if (find === true) {
        if (ans > num) {
          ans = num;
          ansDirect = direct;
        }

        return;
      }
      [board[bx + len][by], bx] = ["B", bx + len];
    }
    if (bx > rx) {
      let len = 0;

      for (let i = 1; i < N - bx; i++) {
        if (board[bx + i][by] === "O") return;
        if (board[bx + i][by] === "#") {
          len = i - 1;
          break;
        }
      }

      [board[bx + len][by], bx] = ["B", bx + len];

      for (let i = 1; i < N - rx; i++) {
        if (board[rx + i][ry] === "O") {
          if (ans > num) {
            ans = num;
            ansDirect = direct;
          }

          return;
        }
        if (board[rx + i][ry] === "#" || board[rx + i][ry] === "B") {
          len = i - 1;
          break;
        }
      }
      [board[rx + len][ry], rx] = ["R", rx + len];
    }
  } else {
    let rlen = 0;
    let blen = 0;

    for (let i = 1; i < N - bx; i++) {
      if (board[bx + i][by] === "O") return;
      if (board[bx + i][by] === "#") {
        blen = i - 1;
        break;
      }
    }
    for (let i = 1; i < N - rx; i++) {
      if (board[rx + i][ry] === "O") {
        if (ans > num) {
          ans = num;
          ansDirect = direct;
        }

        return;
      }
      if (board[rx + i][ry] === "#") {
        rlen = i - 1;
        break;
      }
    }
    [board[bx + blen][by], board[rx + rlen][ry]] = ["B", "R"];
    [bx, rx] = [bx + blen, rx + rlen];
  }

  moveTop(rx, ry, bx, by, board, num + 1, direct + "U");
  moveBottom(rx, ry, bx, by, board, num + 1, direct + "D");
  moveLeft(rx, ry, bx, by, board, num + 1, direct + "L");
  moveRight(rx, ry, bx, by, board, num + 1, direct + "R");
}

function moveLeft(rx, ry, bx, by, b, num, direct) {
  if (num > Math.min(10, ans)) return;
  const board = b.map((row) => [...row]);
  [board[bx][by], board[rx][ry]] = [".", "."];

  if (rx === bx) {
    if (ry > by) {
      let len = 0;
      for (let i = 1; i <= by; i++) {
        if (board[bx][by - i] === "O") return;
        if (board[bx][by - i] === "#") {
          len = i - 1;
          break;
        }
      }
      [board[bx][by - len], by] = ["B", by - len];
      for (let i = 1; i <= ry; i++) {
        if (board[rx][ry - i] === "O") {
          if (ans > num) {
            ans = num;
            ansDirect = direct;
          }

          return;
        }
        if (board[rx][ry - i] === "#" || board[rx][ry - i] === "B") {
          len = i - 1;
          break;
        }
      }
      [board[rx][ry - len], ry] = ["R", ry - len];
    }
    if (by > ry) {
      let len = 0;
      let find = false;
      for (let i = 1; i <= ry; i++) {
        if (board[rx][ry - i] === "O") {
          find = true;
          break;
        }
        if (board[rx][ry - i] === "#") {
          len = i - 1;
          break;
        }
      }
      if (!find) [board[rx][ry - len], ry] = ["R", ry - len];
      for (let i = 1; i <= by; i++) {
        if (board[bx][by - i] === "O") return;
        if (board[bx][by - i] === "#" || board[bx][by - i] === "R") {
          len = i - 1;
          break;
        }
      }
      if (find === true) {
        if (ans > num) {
          ans = num;
          ansDirect = direct;
        }

        return;
      }
      [board[bx][by - len], by] = ["B", by - len];
    }
  } else {
    let rlen = 0;
    let blen = 0;

    for (let i = 1; i <= by; i++) {
      if (board[bx][by - i] === "O") return;
      if (board[bx][by - i] === "#") {
        blen = i - 1;
        break;
      }
    }
    for (let i = 1; i <= ry; i++) {
      if (board[rx][ry - i] === "O") {
        if (ans > num) {
          ans = num;
          ansDirect = direct;
        }

        return;
      }
      if (board[rx][ry - i] === "#") {
        rlen = i - 1;
        break;
      }
    }
    [board[bx][by - blen], board[rx][ry - rlen]] = ["B", "R"];
    [by, ry] = [by - blen, ry - rlen];
  }

  moveTop(rx, ry, bx, by, board, num + 1, direct + "U");
  moveBottom(rx, ry, bx, by, board, num + 1, direct + "D");
  moveLeft(rx, ry, bx, by, board, num + 1, direct + "L");
  moveRight(rx, ry, bx, by, board, num + 1, direct + "R");
}

function moveRight(rx, ry, bx, by, b, num, direct) {
  if (num > Math.min(10, ans)) return;
  const board = b.map((row) => [...row]);
  [board[bx][by], board[rx][ry]] = [".", "."];

  if (rx === bx) {
    if (ry > by) {
      let len = 0;
      let find = false;
      for (let i = 1; i < M - ry; i++) {
        if (board[rx][ry + i] === "O") {
          find = true;
          return;
        }
        if (board[rx][ry + i] === "#") {
          len = i - 1;
          break;
        }
      }
      if (!find) [board[rx][ry + len], ry] = ["R", ry + len];

      for (let i = 1; i < M - by; i++) {
        if (board[bx][by + i] === "O") return;
        if (board[bx][by + i] === "#" || board[bx][by + i] === "R") {
          len = i - 1;
          break;
        }
      }
      if (find === true) {
        if (ans > num) {
          ans = num;
          ansDirect = direct;
        }

        return;
      }
      [board[bx][by + len], by] = ["B", by + len];
    }
    if (by > ry) {
      let len = 0;

      for (let i = 1; i < M - by; i++) {
        if (board[bx][by + i] === "O") return;
        if (board[bx][by + i] === "#") {
          len = i - 1;
          break;
        }
      }

      [board[bx][by + len], by] = ["B", by + len];

      for (let i = 1; i < M - ry; i++) {
        if (board[rx][ry + i] === "O") {
          if (ans > num) {
            ans = num;
            ansDirect = direct;
          }

          return;
        }
        if (board[rx][ry + i] === "#" || board[rx][ry + i] === "B") {
          len = i - 1;
          break;
        }
      }
      [board[rx][ry + len], ry] = ["R", ry + len];
    }
  } else {
    let rlen = 0;
    let blen = 0;
    for (let i = 1; i < M - by; i++) {
      if (board[bx][by + i] === "O") return;
      if (board[bx][by + i] === "#") {
        blen = i - 1;
        break;
      }
    }
    for (let i = 1; i < M - ry; i++) {
      if (board[rx][ry + i] === "O") {
        if (ans > num) {
          ans = num;
          ansDirect = direct;
        }

        return;
      }
      if (board[rx][ry + i] === "#") {
        rlen = i - 1;
        break;
      }
    }
    [board[bx][by + blen], board[rx][ry + rlen]] = ["B", "R"];
    [by, ry] = [by + blen, ry + rlen];
  }
  moveTop(rx, ry, bx, by, board, num + 1, direct + "U");
  moveBottom(rx, ry, bx, by, board, num + 1, direct + "D");
  moveLeft(rx, ry, bx, by, board, num + 1, direct + "L");
  moveRight(rx, ry, bx, by, board, num + 1, direct + "R");
}

function solution() {
  let [rx, ry, bx, by] = findBalls();

  moveTop(rx, ry, bx, by, board, 1, "U");
  moveBottom(rx, ry, bx, by, board, 1, "D");
  moveLeft(rx, ry, bx, by, board, 1, "L");
  moveRight(rx, ry, bx, by, board, 1, "R");

  console.log(ans === Infinity ? -1 : ans);
  if (ansDirect) console.log(ansDirect);
}

solution();
