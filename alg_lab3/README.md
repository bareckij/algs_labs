# Лабораторная работа №3: `Быстрая сортировка, сортировки за линейное время.`

Студент ИТМО, Барецкий Максим Степанович 465136

## Вариант 7

### Навигация

- [ ] [Задача 1 - Улучшение Quick sort](task1/)
- [ ] [Задача 3 - Сортировка пугалом](task3/)
- [ ] [Задача 4 - Точки и отрезки](task4/)
- [ ] [Задача 5 - Индекс Хирша](task5/)
- [ ] [Задача 6 - Сортировка целых чисел](task6/)
- [ ] [Задача 8 - K ближайших точек к началу координат](task8/)

## Описание

Лабораторная работа посвящена разбору элементарных структур данных, таких как стек, очередь и связанный список.

## Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/bareckij/algs_labs.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd algs_labs
   ```
3. **Запуску всех задач**

   ```bash
   for script in alg_lab3/src/*.py; do PYTHONPATH=$(pwd) python3 "$script"; done

   ```

## Тестирование

Для запуска тестов выполните:

```bash
   pytest alg_lab4/task*/tests/*.py
```
