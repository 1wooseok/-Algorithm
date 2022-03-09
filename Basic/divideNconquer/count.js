// 분할 정복을 이용한 배열 요수 갯수
function get_length(arr) {
  if(arr.length === 0) {
    return 0;
  }
  return 1 + get_length(arr.filter((x, idx) => idx > 0))
}