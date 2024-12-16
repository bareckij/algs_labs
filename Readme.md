# Практика по Алгоритмам и Cтруктурам Данных ИТМО

Студент(ка) ИТМО, Барецкий Максим Степанович 465136

## Вариант 7

### Навигация

[Лабораторная 0 - Введение](https://github.com/bareckij/algs_labs/tree/main/alg_lab0)

[Лабораторная 1 - Сортировка вставками, выбором, пузырьковая](https://github.com/bareckij/algs_labs/tree/main/alg_lab1)

[Лабораторная 2 - Сортировка слиянием. Метод декомпозиции](https://github.com/bareckij/algs_labs/tree/main/alg_lab2)

[Лабораторная 3 - Быстрая сортировка, сортировка за линейное время](https://github.com/bareckij/algs_labs/tree/main/alg_lab3)

[Лабораторная 4 - Стек, очередь, связанный список](https://github.com/bareckij/algs_labs/tree/main/alg_lab4)

[Лабораторная 5 - Деревья. Пирамида, пирамидальная сортировка. Очередь с приоритетами.](https://github.com/bareckij/algs_labs/tree/main/alg_lab5)

[Лабораторная 6 - Хеширование. Хеш-таблицы.](https://github.com/bareckij/algs_labs/tree/main/alg_lab6)

[Лабораторная 7 - Динамическое программирование №1](https://github.com/bareckij/algs_labs/tree/main/alg_lab7)

### Описание

### Цели и задачи

- Изучить основные команды Git
- Научиться создавать и управлять репозиториями
- Освоить работу с ветками и слияниями
- Понять основы работы с удаленными репозиториями

### Технологии и инструменты

- **Git** — система контроля версий
- **GitHub** — платформа для хостинга репозиториев
- **Markdown** — язык разметки для оформления документации

### Инструкция по запуску

1. Клонируйте репозиторий:

```bash
git clone https://github.com/bareckij/algs_labs.git
```

2. Перейдите в папку с проектом:

```bash
cd alg_lab
```

3. Запуск всех лабараторных

```bash
for script in alg_lab*/*/src/*.py; do PYTHONPATH=$(pwd) python "$script"; done
```

4. Запуску всех тестов

```bash
pytest alg_lab*/task*/test/*.py

```
