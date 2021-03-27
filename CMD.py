import threading
import os
import time

exitFlag = 0
fllag = 0
class start_Thread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print ("开始线程：" + self.name)
        os.system(str(os.getcwd()) + "\python_blockchain_app_" + str(self.threadID) + "\\node_server.py")

# 启动节点
thread0 = start_Thread(0, "Thread-0")
thread1 = start_Thread(1, "Thread-1")
thread2 = start_Thread(2, "Thread-2")
# 开启新线程
thread0.start()
thread1.start()
thread2.start()
#链接各节点
time.sleep(5)
os.system("curl -X POST http://127.0.0.1:8001/register_with -H \"Content-Type:application/json\" -d \"{\\\"node_address\\\": \\\"http://127.0.0.1:8000\\\"}\"")
os.system("curl -X POST http://127.0.0.1:8002/register_with -H \"Content-Type:application/json\" -d \"{\\\"node_address\\\": \\\"http://127.0.0.1:8000\\\"}\"")
os.system("curl -X POST http://127.0.0.1:8002/register_with -H \"Content-Type:application/json\" -d \"{\\\"node_address\\\": \\\"http://127.0.0.1:8001\\\"}\"")
print ("退出主线程")