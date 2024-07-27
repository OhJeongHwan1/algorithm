const TEST_NUMBER = 100000;

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }
  enqueue(value) {
    const newNode = new Node(value);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.size++;
  }
  dequeue() {
    if (!this.head) return null;
    const removeNode = this.head;
    this.head = this.head.next;
    if (!this.head) {
      this.tail = null;
    }
    this.size--;
    return removeNode.value;
  }
}

const linkedListQueue = new Queue();
const arrayQueue = [];
console.log("N:", TEST_NUMBER);
console.time("LinkedListQueue");
for (let i = 0; i < TEST_NUMBER; i++) {
  linkedListQueue.enqueue(i);
}
for (let i = 0; i < TEST_NUMBER; i++) {
  linkedListQueue.dequeue();
}
console.timeEnd("LinkedListQueue");

console.time("ArrayQueue");
for (let i = 0; i < TEST_NUMBER; i++) {
  arrayQueue.push(i);
}
for (let i = 0; i < TEST_NUMBER; i++) {
  arrayQueue.shift();
}
console.timeEnd("ArrayQueue");
