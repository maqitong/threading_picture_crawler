import time
import threading

"""
创建进程锁
lock = threading.Lock()

lock的方法：
1、上锁 lock.acquire()
2、解锁 lock.release()

"""

ticket = 100
lock = threading.Lock()


def man_buy_ticket():
    global ticket

    for i in range(10000):
        if ticket > 0:
            lock.acquire()
            print(f'{threading.current_thread().name}当前在购买{ticket}')
            ticket -= 1
            time.sleep(0.5)
            lock.release()


def main():
    # 创建进程
    t1 = threading.Thread(target=man_buy_ticket)
    t2 = threading.Thread(target=man_buy_ticket)
    t1.name = '1'
    t2.name = '2'
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
