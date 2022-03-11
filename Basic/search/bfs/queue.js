class Queue {
  constructor() {
    this.queue = [];
  }

  enque(item) {
    this.queue.push(item);
  }

  deque() {
    return this.queue.shift();
  }
}

export default Queue;