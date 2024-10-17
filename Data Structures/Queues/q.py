from queue import Queue
q = Queue(maxsize = 10)
p = input("Enter name: ")
q.put(p)
while q.qsize() > 0:
    c = int(input("Enqueue(0) or Dequeue(1)? "))
    match c:
        case 0:
            p = input("Enter name to be enqueued: ")
            q.put(p)