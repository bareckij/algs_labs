from collections import deque
import utils
def process_packets(S, n, packets):
    # Массив для хранения результатов
    results = []
    
    # Очередь для хранения времени завершения обработки пакетов
    finish_time = deque()
    
    # Время, когда процессор свободен
    current_time = 0
    
    # Обработка каждого пакета
    for Ai, Pi in packets:
        # Удаляем пакеты, которые уже были обработаны к моменту поступления нового пакета
        while finish_time and finish_time[0] <= Ai:
            finish_time.popleft()

        # Если буфер не переполнен
        if len(finish_time) < S:
            # Начало обработки пакета
            if current_time <= Ai:
                start_time = Ai
            else:
                start_time = current_time
            
            # Время завершения обработки пакета
            finish_time.append(start_time + Pi)
            results.append(start_time)
            
            # Обновляем время, когда процессор будет свободен
            current_time = start_time + Pi
        else:
            # Пакет отбрасывается
            results.append(-1)

    return results
if __name__ == "__main__":
    S, n = utils.read_data_from_file('alg_lab5/task3/textf/input.txt')[0]
    packets = utils.read_data_from_file('alg_lab5/task3/textf/input.txt')[1:]
    result = process_packets(S, n, packets)
    utils.write_data_to_file('alg_lab5/task3/textf/output.txt', result)
    print('lab5/task2')
    print(result)