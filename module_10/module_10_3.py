import threading
from random import randint
from time import sleep


class Bank(threading.Thread):

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        transaction_limit = 100
        for _ in range(transaction_limit):
            random_num = randint(50, 500)
            self.balance += random_num
            print(f"Пополнение: {random_num}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        transaction_limit = 100
        for _ in range(transaction_limit):
            random_num = randint(50, 500)
            print(f"Запрос на {random_num}")
            if random_num <= self.balance:
                self.balance -= random_num
                print(f"Снятие: {random_num}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
