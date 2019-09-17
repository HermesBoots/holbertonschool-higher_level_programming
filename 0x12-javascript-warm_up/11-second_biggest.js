#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  let first = Math.floor(Number(process.argv[2]));
  let second = Math.floor(Number(process.argv[3]));
  let val;
  if (second > first) {
    first ^= second;
    second ^= first;
    first ^= second;
  }
  for (let i = 4; i < process.argv.length; i++) {
    val = Math.floor(Number(process.argv[i]));
    if (val > first) {
      second = first;
      first = val;
    } else if (val > second) {
      second = val;
    }
  }
  console.log(second);
}
