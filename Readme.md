# Алгоритмы и структуры данных 

Барецкий Максим | K3141 | 465136

----

Описание

Цели и задачи
-   Изучить основные команды Git
-   Научиться создавать и управлять репозиториями
-   Освоить работу с ветками и слияниями
-   Понять основы работы с удаленными репозиториями

Технологии и инструменты
-   Git — система контроля версий
-   GitHub — платформа для хостинга репозиториев
-   Markdown — язык разметки для оформления документации

----

### Инструкция по запуску

1. Клонируйте репозиторий:
```bash
git clone https://github.com/bareckij/algs_labs.git
```

2. Перейдите в папку с проектом:
```bash
cd alg_lab3
```

3. Запуск всех лабараторных
```bash
for script in alg_lab*/*/src/*.py; do PYTHONPATH=$(pwd) python "$script"; done
```

4. Запуску всех тестов
```bash
pytest alg_lab*/task*/test/*.py

for script in alg_lab*/*/test/*.py; do PYTHONPATH=$(pwd) python "$script"; done
```


[Лабораторная 0 - Введение](https://github.com/bareckij/algs_labs/tree/main/alg_lab0)

[Лабораторная 1 - Сортировка вставками, выбором, пузырьковая](https://github.com/bareckij/algs_labs/tree/main/alg_lab1)

[Лабораторная 2 - Сортировка слиянием. Метод декомпозиции](https://github.com/bareckij/algs_labs/tree/main/alg_lab2)

[Лабораторная 3 - Быстрая сортировка, сортировка за линейное время](https://github.com/bareckij/algs_labs/tree/main/alg_lab3)

[Лабораторная 4 - Стек, очередь, связанный список](https://github.com/bareckij/algs_labs/tree/main/alg_lab4)
