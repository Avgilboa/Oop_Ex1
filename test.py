import unittest


from main import student

class Testing (unittest.TestCase):

    def test_name(self):
        std = student('yossi', 22, ['oop'])
        self.assertEqual(std.name, "yossi")
        self.assertEqual(std.id, 111)

if __name__ == '__main__':
    unittest.main()