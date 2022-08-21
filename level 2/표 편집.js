// 첫번쨰
function solution(n, k, cmd) {
  const garbage = [];
  let table = createTable(n);

  for (let command of cmd) {
    let cnt = 0;
    let [char, num] = command.split(" ");
    num = Number(num);

    switch (char) {
      case "U":
        while (table[k].left !== undefined && cnt < num) {
          k = table[k].left;
          cnt++;
        }
        break;
      case "D":
        while (table[k].right !== undefined && cnt < num) {
          k = table[k].right;
          cnt++;
        }
        break;
      case "C":
        garbage.push(k);
        table[k].label = 'X';

        if (table[k].right === undefined) {
          k = table[k].left;
          table[k].right = undefined;
        } else if (table[k].left === undefined) {
          k = table[k].right;
          table[k].left = undefined;
        } else {
          table[k - 1].right = table[k].right;
          table[k + 1].left = table[k].left;
          k = table[k].right;
        }
        break;
      case "Z":
        const back = garbage.pop();
        table[back].label = 'O';

        if (back === 0) {
          table[back].right = table[back + 1].idx;
        } else if (back === n - 1) {
          table[back].left = table[back - 1].idx;
        } else {
          table[back].left = table[back - 1].idx;
          table[back].right = table[back + 1].idx;
        }
        break;
      default:
        throw new Error("Invalid Command");
    }
  }

  let result = '';
  for (let t of table) {
    result += t.label;
  }
  return result;
}

function createTable(n) {
  const table = [];

  for (let i = 0; i < n; i++) {
    let idx = i;
    let label = 'O';
    let left = i ? i - 1 : undefined;
    let right = i === n - 1 ? undefined : i + 1;

    table.push({ idx, label, left, right });
  }

  return table;
}

////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////

// 두번쨰 시도
function solution(n, k, cmd) {
  const del = [];
  const rows = createRows(n);

  for (let command of cmd) {
    let cnt = 0;
    let [char, num] = command.split(" "); // [U 2], [C undefined]
    num = Number(num);

    switch (char) {
      case "U":
        while (rows[k].up !== undefined && cnt < num) {
          k = rows[k].up;
          cnt++;
        }
        break;
      case "D":
        while (rows[k].down !== undefined && cnt < num) {
          k = rows[k].down;
          cnt++;
        }
        break;
      case "C":
        rows[k].label = 'X';
        del.push(k);

        if (rows[k].up === undefined) {
          k = rows[k].down;
          rows[k].up = undefined;
        } else if (rows[k].down === undefined) {
          k = rows[k].up;
          rows[k].down = undefined;
        } else {
          rows[rows[k].down].up = rows[k].up;
          rows[rows[k].up].down = rows[k].down;
          k = rows[k].down;
        }
        break;
      case "Z":
        const back = del.pop();
        rows[back].label = 'O';

        // Bug!
        if (k > back && rows[k].up === undefined) {
          rows[k].down = rows[back].data;
          rows[back].up = rows[k].data;
          rows[back].down = undefined;
        } else if (k < back && rows[k].dowm === undefined) {
          rows[cnt].up = rows[back].data;
          rows[back].down = rows[k].data;
          rows[back].up = undefined;
        } else if (k < back) {
          cnt = k;
          while (rows[cnt].down && back > rows[cnt].down) {
            cnt = rows[cnt].down;
          }
          rows[back].up = rows[cnt].data;
          rows[back].down = rows[cnt].down.data;

          rows[cnt].down.up = rows[back].data;
          rows[cnt].down = rows[back].data;
        } else if (k > back) {
          cnt = k;
          while (rows[cnt].up && back < rows[cnt].up) {
            cnt = rows[cnt].up;
          }
          rows[back].up = rows[cnt].up;
          rows[back].down = rows[cnt].data;
          rows[cnt].up = rows[back].data;
        }
        break;
      default:
        throw new Error(`"${char}" is Invalid Command`);
    }
  }
  let result = '';
  for (let row of rows) {
    result += row.label;
  }
  return result
}

function createRows(n) {
  const rows = [];

  for (let i = 0; i < n; i++) {
    let data = i;
    let label = 'O';
    let up = i > 0 ? i - 1 : undefined;
    let down = i !== n - 1 ? i + 1 : undefined;

    rows.push({ data, label, up, down });
  }

  return rows;
}
