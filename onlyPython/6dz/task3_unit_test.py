import unittest, time

from task3 import factorial

class TestFactorial(unittest.TestCase):
    def setUp(self) -> None:
        print("setUp")
        self.startTime = time.time()

    def test_factorial(self):
        time.sleep(1)
        self.assertEqual(factorial(6), 720)
        time.sleep(1)
        self.assertEqual(factorial(6), 520)

        time.sleep(1)
        self.assertRaises(ValueError, factorial, 7000000)
        time.sleep(1)
        self.assertRaises(ValueError, factorial, -6)

        time.sleep(1)
        self.assertRaises(TypeError, factorial, 5.5)
        time.sleep(1)
        self.assertRaises(TypeError, factorial, "a")
        

    def tearDown(self) -> None:
        print("tearDown")

        t = time.time() - self.startTime
        print(f"Время выполнения тестов: {t}")