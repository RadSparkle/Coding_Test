import queue
import sys
n = int(sys.stdin.readline())
que = queue.Queue()

for i in range(1, n+1) :
    que.put(i)

while que.qsize() != 1 :
    que.get()
    que.put(que.get())
print(que.get())
