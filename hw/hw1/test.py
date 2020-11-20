from main import fibo, root_5, prime, seek_unique, find_names
import unittest


class TestHM1(unittest.TestCase):

    def test_single_arg(self):
        functions = [fibo, prime, seek_unique]
        inputs = [
            [1, 2, 3, 4, 5, 6, 100],
            [*range(1, 9), 10000],
            [[1, 2, 3], [1, 1, 2, 3, 3], [], [1], [3, 3]],
        ]
        results = [
            [1, 1, 2, 3, 5, 8, 354224848179261915075],
            [2, 3, 5, 7, 11, 13, 17, 19, 104729],
            [[1, 2, 3], [2], [], [1], []],
        ]
        for func, x, result in zip(functions, inputs, results):
            for every_x, every_result in zip(x, result):
                assert func(
                    every_x) == every_result, f'{func.__name__}({every_x}) should be {every_result}, get {func(every_x)}'

    def test_root5(self):
        for x in range(0, 10):
            assert abs(root_5(x)-x**(1/5)
                       ) < 0.01, f'{x}, {root_5(x)}, {x**(1/5)}'

    def test_multi_arg(self):
        functions = [find_names]
        inputs = [
            [[['alice', 'bob'], 'ace'], [['alice', 'bob'], 'clair'], [[], 'alice']],
        ]
        results = [
            [['alice'], [], []]
        ]
        for func, x, result in zip(functions, inputs, results):
            for every_x, every_result in zip(x, result):
                assert func(
                    *every_x) == every_result, f'{func.__name__}({every_x}) should be {every_result}, get {func(*every_x)}'


if __name__ == '__main__':
    unittest.main()
