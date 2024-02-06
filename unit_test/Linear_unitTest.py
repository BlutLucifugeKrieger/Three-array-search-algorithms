import unittest
import sys
from algorithms.Linear_search import linear


class TestLinearSearch(unittest.TestCase):

    def setUp(self):
        self.linear_search = linear()

    def test_search_found(self):
        array = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13]
        objective = 3
        self.linear_search.search(array, objective)
        result = self.linear_search.objective_index(objective)
        self.assertEqual(result, "The number 3 is in the array at index: [2]")

    def test_search_not_found(self):
        array = [1, 2, 3, 4, 5]
        objective = 6
        self.linear_search.search(array, objective)
        result = self.linear_search.objective_index(objective)
        self.assertEqual(result, "The number 6 wasn't in the array")

    def test_single_value_to_find(self):

        array = [1, 2, 3, 4, 5]
        objective = 3
        self.linear_search.search(array,objective)

        initial_elapsed_times = list(self.linear_search.elapsed_times)
        initial_memory_usages = list(self.linear_search.memory_usages)

        self.linear_search.single_value()

        expected_elapsed_times = initial_elapsed_times + [initial_elapsed_times[0]] * 5
        expected_memory_usages = initial_memory_usages + [initial_memory_usages[0]] * 5

        self.assertEqual(self.linear_search.elapsed_times, expected_elapsed_times)
        self.assertEqual(self.linear_search.memory_usages, expected_memory_usages)



    def test_graph_generation_is_correct(self):

        array = [1, 2, 3, 4, 5, 3]
        objective = 3

        self.linear_search.search(array, objective)
        self.linear_search.single_value()

        val = len(self.linear_search.index)

        self.assertEqual(val,2)

    def test_graph_generations_not_works_by_invalid_input(self):

        array = [1, 2, 3, 4, 5, 3]
        objective = 6

        self.linear_search.search(array, objective)
        self.linear_search.single_value()

        val = len(self.linear_search.index)

        self.assertEqual(val,0)


if __name__ == "__main__":
    unittest.main()
