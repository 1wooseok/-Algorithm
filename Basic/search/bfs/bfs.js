import Queue from "./queue.js";
import graph from "./graph.js";

function bfs(item) {
  const Q = new Queue();
  Q.enque(...graph["me"]);
  const visited = [];

  while (Q.queue.length !== 0) {
    const person = Q.deque();
    if (!person in visited) {
      if (person === item) {
        return item;
      } else {
        if (!graph[person]) {
          return false;
        }
        Q.enque(...graph[person]);
      }
    }
  }
  return false;
}
// 수소문해서 사람을 찾는과정과 비슷.
// 처음에는 가장 가까운 친구를 탐색
// 내 주변에서 찾지 못했으면 친구의 친구를 탐색
// 친구의 친구를 알기 위해 '큐'를 사용
// 친구가 찾는사람을 알지 못하면, 친구의 친구를 큐에 저장하고 다음 친구 탐색.

// 실행시간은 보통 O(V + E)로 표현
// 네트워크의 모든간선을 따라 탐색해야함 O(E).
// 큐에 정점을 추가해야함 O(V)
