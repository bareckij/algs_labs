import unittest
from alg_lab4.task2.src.task2 import process_commands

class TestTask2(unittest.TestCase):

    def test_process_commands(self):
        # Given
        commands = [
            ["+", 1],
            ["+", 10],
            ["-"],
            ["-"],
        ]
        # When
        result = process_commands(commands)
        # Then
        expected = [1, 10]
        self.assertEqual(result, expected)

    def test_empty(self):
        # Given
        commands = [
            ["+", 5],
            ["-",],
            ["-",],  # Не должно быть извлечений
        ]
        # When
        result = process_commands(commands)
        # Then
        expected = [5]
        self.assertEqual(result, expected)

    def test_not_extract(self):
        # Given
        commands = [
            ["+", 1],
            ["+", 2],
            ["+", 3],
        ]
        # When
        result = process_commands(commands)
        # Then
        expected = []
        self.assertEqual(result, expected)

    def test_delete(self):
        # Given
        commands = [
            ["+", 1],
            ["+", 2],
            ["+", 3],
            ["-",],  # Извлекаем 1
            ["-",],  # Извлекаем 2
            ["-",],  # Извлекаем 3
        ]
        # When
        result = process_commands(commands)
        # Then
        expected = [1, 2, 3]
        self.assertEqual(result, expected)

    def test_add_extract(self):
        # Given
        commands = [
            ["+", 1],
            ["+", 10],
            ["-",],  # Извлекаем 1
            ["+", 20],
            ["-",],  # Извлекаем 10
            ["-",],  # Извлекаем 20
        ]
        # When
        result = process_commands(commands)
        # Then
        expected = [1, 10, 20]
        self.assertEqual(result, expected)

    def test_a_lot(self):
        # Given
        commands = [["+", i] for i in range(1, 10001)] + [["-"] for _ in range(10000)]
        # When
        result = process_commands(commands)
        # Then
        expected = list(range(1, 10001))
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
