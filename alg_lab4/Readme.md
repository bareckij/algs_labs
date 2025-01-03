# Лабораторная работа №4: `Стек, очередь, связанный список.`

Студент ИТМО, Барецкий Максим Степанович 465136

## Вариант 7

### Навигация

- [ ] [Задача 1 - Стек](task1/)
- [ ] [Задача 2 - Очередь](task2/)
- [ ] [Задача 4 - Скобочная последовательность. Версия 2](task4/)
- [ ] [Задача 5 - Стек с максимумом](task5/)
- [ ] [Задача 7 - Максимум в движущейся последовательности](task7/)
- [ ] [Задача 8 - Постфиксная запись](task8/)

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
   for script in alg_lab4*/src/*.py; do PYTHONPATH=$(pwd) python3 "$script"; done

   ```

## Тестирование

Для запуска тестов выполните:

```bash
   pytest alg_lab4/task*/tests/*.py
```
