import unittest
from python_repos import user_request

class ReposTestCase(unittest.TestCase):
    """ Тесты для python_repos.py """

    def test_status(self):
        """ Тест статуса """
        r = user_request()
        status = r.status_code
        print (f"Status: {status}")
        self.assertEqual(status, 200)

if __name__ == '__main__':
    unittest.main()
