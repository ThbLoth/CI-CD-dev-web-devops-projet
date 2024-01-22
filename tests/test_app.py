from app import app
import unittest

class TestApp(unittest.TestCase):

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World! This is my web app.')

if __name__ == '__main__':
    unittest.main()