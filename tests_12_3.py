import unittest
from pythonProject.Lessons.Module12.tests_12_2.tests.runner import Runner
from pythonProject.Lessons.Module12.tests_12_2.tests.runner_and_tournament import Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner('Den')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner('Den')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = Runner('Den')
        runner2 = Runner('Max')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_a = Runner('Усэйн', 10)
        self.runner_b = Runner('Андрей', 9)
        self.runner_c = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_name, result in cls.all_results.items():
            print(f'Тест: {test_name}')
            for position, runner in result.items():
                print(f'{position}: {runner.name}')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_first_tournament(self):
        tournament = Tournament(90, self.runner_a, self.runner_c)
        results = tournament.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_first_tournament'] = results

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_second_tournament(self):
        tournament = Tournament(90, self.runner_b, self.runner_c)
        results = tournament.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_second_tournament'] = results

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_third_tournament(self):
        tournament = Tournament(90, self.runner_a, self.runner_b, self.runner_c)
        results = tournament.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_third_tournament'] = results


if __name__ == "__main__":
    unittest.main()
