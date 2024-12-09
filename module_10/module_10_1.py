import threading
from time import sleep, time
from datetime import timedelta


def wite_words(word_count, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for num in range(1, word_count + 1):
            file.write(f"Какое-то слово № {num}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


start_time = time()
wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")
end_time = time()
print(f'Работа потоков {timedelta(seconds=end_time - start_time)}')

start_time2 = time()
thread1 = threading.Thread(target=wite_words, args=(10, "example5.txt"))
thread2 = threading.Thread(target=wite_words, args=(30, "example6.txt"))
thread3 = threading.Thread(target=wite_words, args=(200, "example7.txt"))
thread4 = threading.Thread(target=wite_words, args=(100, "example8.txt"))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
end_time2 = time()
print(f'Работа потоков {timedelta(seconds=end_time2 - start_time2)}')