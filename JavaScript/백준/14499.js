// 주사위 굴리기 골4 시뮬
const readline = require("readline");
const MOVE = { 1: "EAST", 2: "WEST", 3: "NORTH", 4: "SOUTH" };

(async () => {
  const rl = readline.createInterface({ input: process.stdin });
  let n, m, x, y, k;
  const the_map = [];
  let commands;

  let codeLine = 0;
  for await (const line of rl) {
    codeLine++;
    if (codeLine === 1) [n, m, x, y, k] = line.split(" ").map(Number);
    else if (codeLine <= 1 + n) the_map.push(line.split(" ").map(Number));
    else {
      commands = line.split(" ").map(Number);
      rl.close();
    }
  }
  // 여기까지 입력

  const dice = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 }; // 주사위 0으로 초기화

  for (let i = 0; i < commands.length; i++) {
    const command = commands[i];
    let nx, ny;
    if (MOVE[command] === "EAST") [nx, ny] = [x, y + 1];
    if (MOVE[command] === "WEST") [nx, ny] = [x, y - 1];
    if (MOVE[command] === "NORTH") [nx, ny] = [x - 1, y];
    if (MOVE[command] === "SOUTH") [nx, ny] = [x + 1, y];

    if (!(0 <= nx && nx < n && 0 <= ny && ny < m)) continue; // 이동 불가능한 경우 continue
    [x, y] = [nx, ny]; // 가능한 경우 이동

    let arr;
    if (MOVE[command] === "EAST") arr = [dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]; //방향에 맞도록 주사위 굴림
    if (MOVE[command] === "WEST") arr = [dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]];
    if (MOVE[command] === "NORTH") arr = [dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]];
    if (MOVE[command] === "SOUTH") arr = [dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]];

    [dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]] = arr; // 굴린 주사위로 dice 변경

    if (the_map[x][y] === 0) the_map[x][y] = dice[6]; // 바닥이 0 인 경우 바닥으로 복사
    else {
      dice[6] = the_map[x][y]; //아닌 경우 주사위 밑면으로 복사
      the_map[x][y] = 0;
    }

    console.log(dice[1]);
  }
})();
