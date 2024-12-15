def process_phonebook_queries(n, queries):
    # Словарь для хранения номера телефона и имени
    phonebook = {}

    # Список для хранения результатов команд find
    result = []

    # Обрабатываем каждый запрос
    for query in queries:
        parts = query.split()
        command = parts[0]

        if command == "add":
            number = parts[1]
            name = parts[2]
            phonebook[number] = name  # Добавляем или обновляем запись в телефонной книге

        elif command == "del":
            number = parts[1]
            if number in phonebook:
                del phonebook[number]  # Удаляем запись, если она существует

        elif command == "find":
            number = parts[1]
            if number in phonebook:
                result.append(phonebook[number])  # Добавляем имя в результат
            else:
                result.append("not found")  # Если номера нет, добавляем "not found"

    return result
    