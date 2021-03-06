import json

from app import app
import unittest


class FlaskrTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        result = self.app.get('/')

        self.assertEqual(result.status_code, 200)

    def test_posting_new_data(self):
        d = dict(title="User1First", body="User1Last")
        result = self.app.post('/add', data=d)

        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
