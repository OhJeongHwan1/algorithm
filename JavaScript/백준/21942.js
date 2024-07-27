// 21942 부품 대여장 문자열 파싱 구현 문제

const readline = require("readline");
const MONTHDAYS = Object.freeze({
  1: 31,
  2: 28,
  3: 31,
  4: 30,
  5: 31,
  6: 30,
  7: 31,
  8: 31,
  9: 30,
  10: 31,
  11: 30,
  12: 31,
}); // 달에 대한 날짜를 저장하는 객체

// 입력 시간을 분으로 변환하는 함수
function getAllMinute(the_time) {
  const [date, time] = the_time.split(" ");
  const [year, month, day] = date.split("-").map(Number);
  const [hour, minute] = time.split(":").map(Number);
  let monthDays = 0;
  for (let i = 1; i <= month - 1; i++) {
    monthDays += MONTHDAYS[i];
  }
  return (monthDays + day) * 24 * 60 + hour * 60 + minute;
}

(async () => {
  const rl = readline.createInterface({
    input: process.stdin,
  });
  let n, l, f;
  const infoList = [];

  for await (const line of rl) {
    if (n === undefined) [n, l, f] = line.split(" ").map((x, i) => (i !== 1 ? Number(x) : x));
    else {
      infoList.push(line);
      if (infoList.length === n) rl.close();
    }
  }

  const lday = parseInt(l.split("/")[0]);
  const [lhour, lminute] = l.split("/")[1].split(":").map(Number);
  const standardMin = lday * 24 * 60 + lhour * 60 + lminute; // 기준이 되는 값을 분으로 변환
  const timeMap = new Map();
  const resultMap = new Map();

  infoList.forEach((info) => {
    const [date, time, tool, name] = info.split(" ");
    const toolAndBorrower = `${tool}/${name}`; // 맵의 키 값으로 사용하기 위해 물품과 사람을 한 문자열로
    const fullTime = `${date} ${time}`;

    if (!timeMap.has(toolAndBorrower)) timeMap.set(toolAndBorrower, fullTime); // 시작 시간 저장
    else {
      // 종료 시간 만난 경우
      const startTime = timeMap.get(toolAndBorrower);
      timeMap.delete(toolAndBorrower); // 반납했으니 삭제

      const startMin = getAllMinute(startTime);
      const endMin = getAllMinute(fullTime);
      const diff = endMin - startMin; // 두 날짜 사이의 분

      if (diff > standardMin) {
        let fine = (diff - standardMin) * f;
        resultMap.set(name, (resultMap.get(name) || 0) + fine); // 만약 이미 벌금을 내는 사람이면 벌금 추가
      }
    }
  });

  const resultList = []; // 정렬을 위한 배열 선언
  if (resultMap.size === 0) console.log(-1);
  else {
    for (const [key, value] of resultMap) {
      resultList.push(`${key} ${value}`);
    }
    resultList.sort((a, b) => a.localeCompare(b)).forEach((result) => console.log(result));
  }
})();
