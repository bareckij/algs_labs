import unittest
import time
import tracemalloc
from alg_lab4.task5.src.task5 import process_commands

class test_shouldTask5(unittest.TestCase):

    def test_should_stack_operations(self):
        # Given
        input_data = """5\npush 1\npush 2\nmax\npop\nmax\n"""
        expected_output = """2\n1\n"""
        with open('alg_lab4/task5/textf/input.txt', 'w') as f:
            f.write(input_data)
        # When
        process_commands('alg_lab4/task5/textf/input.txt', 'alg_lab4/task5/textf/output.txt')
        with open('alg_lab4/task5/textf/output.txt', 'r') as f:
            result = f.read().strip()
        # Then
        self.assertEqual(result, expected_output.strip())

    def test_should_empty(self):
        # Given
        input_data = """3\npush 5\npop\nmax\n"""
        expected_output = ""
        with open('alg_lab4/task5/textf/input.txt', 'w') as f:
            f.write(input_data)
        # When
        process_commands('alg_lab4/task5/textf/input.txt', 'alg_lab4/task5/textf/output.txt')
        with open('alg_lab4/task5/textf/output.txt', 'r') as f:
            result = f.read().strip()
        # Then
        self.assertEqual(result, expected_output.strip())

    def test_should_maxs(self):
        # Given
        input_data = """6\npush 1\npush 3\nmax\npush 2\nmax\npop\nmax\n"""
        expected_output = """3\n3\n"""
        with open('alg_lab4/task5/textf/input.txt', 'w') as f:
            f.write(input_data)
        # When
        process_commands('alg_lab4/task5/textf/input.txt', 'alg_lab4/task5/textf/output.txt')
        with open('alg_lab4/task5/textf/output.txt', 'r') as f:
            result = f.read().strip()
        # Then
        self.assertEqual(result, expected_output.strip())

    def test_should_max(self):
        # Given
        input_data = """4\npush 100000\npush 50000\npush 200000\nmax\n"""
        expected_output = """200000\n"""
        with open('alg_lab4/task5/textf/input.txt', 'w') as f:
            f.write(input_data)
        # When
        process_commands('alg_lab4/task5/textf/input.txt', 'alg_lab4/task5/textf/output.txt')
        with open('alg_lab4/task5/textf/output.txt', 'r') as f:
            result = f.read().strip()
        # Then
        self.assertEqual(result, expected_output.strip())

    def test_performance_stack_operations(self):
        # Given
        input_data = """10000\n""" + "\n".join([f"push {i}" for i in range(10000)]) + "\nmax\n"
        # When
        start_time = time.time()
        process_commands('alg_lab4/task5/textf/input.txt', 'alg_lab4/task5/textf/output.txt')
        end_time = time.time()
        execution_time = end_time - start_time
        # When
        tracemalloc.start()
        process_commands('alg_lab4/task5/textf/input.txt', 'alg_lab4/task5/textf/output.txt')
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        # Then
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10**6, 256)

if __name__ == "__main__":
    unittest.main()
