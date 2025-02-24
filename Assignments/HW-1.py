import unittest


def double(y: int) -> int:
    return y * 2


def greet(x: str) -> str:
    for _ in range(0, 10):
        print(x)
    return f"Hello, {x}"


print(double(5))
test = greet("Matthew")
print(test)


class TestDoubleMethod(unittest.TestCase):
    def test_Double(self):
        self.assertEqual(double(3), 6)
        self.assertEqual(double(0), 0)
        self.assertEqual(double(-2), 4)

    # test case for invalid type
    def test_invalidtype(self):
        with self.assertRaises(TypeError):
            double("Stuff")

# ensures tests run
if __name__ == "__main__":
    unittest.main()
