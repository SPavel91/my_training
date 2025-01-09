import logging
import rt_with_exceptions
import unittest

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = rt_with_exceptions.Runner("Ivan", -5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно', exc_info=True)
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}", exc_info=True)

    def test_run(self):
        try:
            runner = rt_with_exceptions.Runner(2)
            runner.run()
            logging.info('"test_run" выполнен успешно', exc_info=True)
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}", exc_info=True)

    def test_challenge(self):
        runner_1 = rt_with_exceptions.Runner("Pavel")
        runner_2 = rt_with_exceptions.Runner("Egor")
        for _ in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == "__main__":
    unittest.main()




