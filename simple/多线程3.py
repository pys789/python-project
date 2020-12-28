import threading
import time

lock = threading.Lock()
threads = []


class myThread(threading.Thread):

    def __init__(self, threadID, threadName, delay):
        super().__init__()
        self.threadID = threadID
        self.threadName = threadName
        self.delay = delay

    def run(self):
        print("开启线程{}".format(self.threadName))
        try:
            lock.acquire()
            print_time(self.threadName, self.delay, 3)
        finally:
            lock.release()



def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print('%s:%s' % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
