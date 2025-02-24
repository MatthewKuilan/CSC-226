import unittest


def double(y: int) -> int:
    return y * 2


class TestDoubleMethod(unittest.TestCase):
    def test_Double(self):
        self.assertEqual(double(3), 6)
        self.assertEqual(double(0), 0)
        self.assertEqual(double(-2), 4)

    # context manager, ensures error is raised if wrong type is used
    def test_invalidtype(self):
        with self.assertRaises(TypeError):
            double("Stuff")


def greet(x: str) -> str:
    for _ in range(10):
        print("hi")
    return f"Hello, {x}"


print(double(5))
test = greet("Matthew")
print(test)


if __name__ == "__main__":
    unittest.main()
