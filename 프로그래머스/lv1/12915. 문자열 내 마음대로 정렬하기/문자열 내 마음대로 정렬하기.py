from queue import PriorityQueue

def solution(strings, n):
    que = PriorityQueue()
    result = []
    for i in range(len(strings)) :
        m_list = list(strings[i])
        que.put((ord(m_list[n]),strings[i]))

    for k in range(que.qsize()) :
        result.append(que.get()[1])
    return result