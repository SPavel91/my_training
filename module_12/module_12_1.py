import Runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner.Runner("Ivan")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner.Runner("Denis")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner_1 = Runner.Runner("Pavel")
        runner_2 = Runner.Runner("Egor")
        for _ in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == "__main__":
    unittest.main()

