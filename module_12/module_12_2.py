import unittest
import Runner


class TournamentTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner.Runner("Усэйн", 10)
        self.runner2 = Runner.Runner("Андрей", 9)
        self.runner3 = Runner.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_usain_and_nik(self):
        tournament = Runner.Tournament(90, self.runner1, self.runner3)
        result = tournament.start()
        self.all_results[1] = result
        self.assertEqual(list(result.values())[-1], "Ник")

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_andrey_and_nik(self):
        tournament = Runner.Tournament(90, self.runner2, self.runner3)
        result = tournament.start()
        self.all_results[2] = result
        self.assertTrue(list(result.values())[-1] == "Ник")

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_usain_andrey_and_nik(self):
        tournament = Runner.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament.start()
        self.all_results[3] = result
        self.assertTrue(list(result.values())[-1] == "Ник")


if __name__ == "__main__":
    unittest.main()