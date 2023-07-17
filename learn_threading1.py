import threading
import time
"""
Thread类，创建多线程
方法
    1、threading.current_thread()  获取当前线程的信息
    2、thread.name 获取线程名字
    3、threading.enumerate() 获取所有的线程信息
"""


# 了解多线程是什么东西
def fun1():
    for i in range(5):
        print('【func1】=', i)
        time.sleep(0.5)


def fun2():
    for i in range(5):
        print('【func2】=', i)
        time.sleep(0.5)


def main():
    #  函数式创建
    #  创建线程
    thread1 = threading.Thread(target=fun1)
    thread2 = threading.Thread(target=fun2)
    #  启动线程
    thread1.start()
    thread2.start()
    print(threading.enumerate())

if __name__ == '__main__':
    main()

