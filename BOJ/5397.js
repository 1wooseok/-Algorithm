const left = [];
const right = [];



function action(char) {
  switch (char) {
    case "<":
      if (left.length === 0) return;
      right.push(left.pop());
      break;
    case ">":
      if (right.length === 0) return;
      left.push(right.pop());
      break;
    case "-":
      left.pop();
      break;
    default:
      left.push(char);
      break;
  }
}
