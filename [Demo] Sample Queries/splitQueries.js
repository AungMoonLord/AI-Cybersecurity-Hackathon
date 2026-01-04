const fs = require("node:fs");
fs.readFile("queries-logs-100A.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data.split("\n").map((line) => ({ query: line.trim() })));
});
