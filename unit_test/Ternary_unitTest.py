import unittest

from algorithms.Ternary_search import ternary


class TestTernarySearch(unittest.TestCase):

    def setUp(self):
        self.ternary_search = ternary()


    def test_search_ternary_found(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 9

        self.ternary_search.ternary_search(array, target)
        result = self.ternary_search.objective_index(target)

        self.assertEqual(result, "The number 9 is in the array at index: [8]")

    def test_search_ternary_not_found(self):

        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 10

        self.ternary_search.ternary_search(array, target)
        result = self.ternary_search.objective_index(target)

        self.assertEqual(result,"The number 10 wasn't in the array")

    def test_graph_generation_is_correct(self):

        array = [1, 2, 3, 3, 4, 5]
        objective = 3

        self.ternary_search.ternary_search(array, objective)

        val = len(self.ternary_search.index)

        self.assertEqual(val,2)

    def test_graph_generations_not_works_by_invalid_input(self):

        array = [1, 2, 3, 4, 5, 3]
        objective = 6

        self.ternary_search.ternary_search(array, objective)

        val = len(self.ternary_search.index)

        self.assertEqual(val,0)



if __name__ == "__main__":
    unittest.main()
