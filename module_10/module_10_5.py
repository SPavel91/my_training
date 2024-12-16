import multiprocessing
import datetime

def read_info(name):
    all_data = []
    with open(name, "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if line.strip() == "":
                break
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start_time = datetime.datetime.now()
read_info(filenames[0])
read_info(filenames[1])
read_info(filenames[2])
read_info(filenames[3])
end_time = datetime.datetime.now()
execution_time = end_time - start_time
print(f"{execution_time} (линейный)")

# Многопроцессный
if __name__ == '__main__':
    start_time2 = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(read_info, filenames)
    end_time2 = datetime.datetime.now()
    execution_time2 = end_time2 - start_time2
    print(f"{execution_time2} (многопроцессный)")





