# Задание 4 по выбору : `Куча ли?`

Студент ИТМО, Барецкий Максим Степанович 465136

## Вариант 7

## Задание 4

В этой задаче вы преобразуете массив целых чисел в пирамиду. Это важнейший шаг алгоритма сортировки под названием HeapSort. Гарантированное время
работы в худшем случае составляет O(n log n), в отличие от среднего времени работы QuickSort, равного O(n log n). QuickSort обычно используется на
практике, потому что обычно он быстрее, но HeapSort используется для внешней сортировки, когда вам нужно отсортировать огромные файлы, которые не
помещаются в памяти вашего компьютера.
Первым шагом алгоритма HeapSort является создание пирамиды (heap) из
массива, который вы хотите отсортировать.
Ваша задача - реализовать этот первый шаг и преобразовать заданный массив целых чисел в пирамиду. Вы сделаете это, применив к массиву определенное
количество перестановок (swaps). Перестановка - это операция, как вы помните,
при которой элементы ai и aj массива меняются местами для некоторых i и j.
Вам нужно будет преобразовать массив в пирамиду, используя только O(n) перестановок. Обратите внимание, что в этой задаче вам нужно будет использовать
min-heap вместо max-heap

1. если 2i ≤ n, то ai ≤ a2i
   ,
2. если 2i + 1 ≤ n, то ai ≤ a2i+1.

## Input / Output

| Input     | Output |
| --------- | ------ |
| 5         | 3      |
| 5 4 3 2 1 | 1 4    |
|           | 0 1    |
|           | 1 3    |

## Ограничения по времени и памяти

- Ограничение по времени. 3 сек.
- Ограничение по памяти. 512 мб.

## Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/bareckij/algs_labs.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd algs_labs
   ```
3. Запустите программу:

   ```bash
   PYTHONPATH=. python3 alg_lab5/task1/src/task1.py
   ```

## Тестирование

Для запуска тестов выполните:

```bash
    pytest alg_lab5/task1/test/test_5_1.py
```