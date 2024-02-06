import unittest

from algorithms.Binary_search import binary


class TestBynarySearch(unittest.TestCase):

    def setUp(self):
        self.binary_search = binary()

    def test_search_binary_found(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 9

        self.binary_search.binary_search(array, target)
        result = self.binary_search.objective_index(target)

        self.assertEqual(result, "The number 9 is in the array at index: [8]")

    def test_search_binary_not_found(self):

        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 10

        self.binary_search.binary_search(array, target)
        result = self.binary_search.objective_index(target)

        self.assertEqual(result,"The number 10 wasn't in the array")

    def test_graph_generation_is_correct(self):

        array = [1, 2, 3, 3, 4, 5]
        objective = 3

        self.binary_search.binary_search(array, objective)

        val = len(self.binary_search.index)

        self.assertEqual(val,2)

    def test_graph_generations_not_works_by_invalid_input(self):

        array = [1, 2, 3, 4, 5, 3]
        objective = 6

        self.binary_search.binary_search(array, objective)

        val = len(self.binary_search.index)

        self.assertEqual(val,0)







if __name__ == '__main__':
    unittest.main()
