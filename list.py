import unittest

def append(list, value):
    #TODO(implement this function pretty please \(^_^)/ )
    return None # this does not work, do it correctly please

class TestStringMethods(unittest.TestCase):

    def test_append_5_to_empty_list(self):
        self.assertEqual(append(None, 5), (5, None))

    def test_append_6_to_list_containing_5(self):
        self.assertEqual(append((5, None), 6), (5, (6, None)))

    def test_append_999_to_list_containing_1_2_3(self):
        self.assertEqual(append((1, (2, (3, None))), 999), (1, (2, (3, (999, None)))))

if __name__ == '__main__':
    unittest.main()

# How to test it? Just run
# python3 list.py
