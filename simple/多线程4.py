import queue
import threading
import time

exitFlag = 0
threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
lock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

class myThread (threading.Thread):
    def __init__(self, threadID, threadName, q):
        super().__init__()
        self.threadID = threadID
        self.threadName = threadName
        self.q = q
    def run(self):
        print ("开启线程：" + self.threadName)
        process_data(self.threadName, self.q)
        print ("退出线程：" + self.threadName)

def process_data(threadName, q):
    while not exitFlag:
        try:
            lock.acquire()
            if not workQueue.empty():
                data = q.get()
                print("%s processing %s" % (threadName, data))
        finally:
            lock.release()
            time.sleep(1)

# 创建新线程
for threadName in threadList:
    thread = myThread(threadID, threadName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
lock.acquire()
for word in nameList:
    workQueue.put(word)
lock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")