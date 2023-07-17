import time
import threading


"""
1、继承Thread类
2、实现run方法
3、实例化线程，启动线程
"""


class MyClass1(threading.Thread):

    def run(self):

        for i in range(5):
            print('MyClass1 =', i)
            time.sleep(1)


class MyClass2(threading.Thread):

    def run(self):

        for i in range(5):
            print('MyClass2 =', i)
            time.sleep(1)


def main():

    #  创建你自己定义的线程类
    thread1 = MyClass1()
    thread2 = MyClass2()

    thread1.start()
    thread2.start()


if __name__ == '__main__':
    main()
