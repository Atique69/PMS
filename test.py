import unittest
import database_manager
import hash


class BasicTests(unittest.TestCase):

    def setUp(self) -> None:
        self.testing = True

    def tearDown(self):
        # clean up everything
        pass

    def test_database_connection(self):
        self.assertTrue(database_manager.connect())

    def test_make_pass(self):
        self.assertTrue(hash.make_password('gmail', 'gmail1234'))

    def test_get_hexdigest(self):
        self.assertTrue(hash.get_hexdigest('user', 'gmail'))

    def test_password(self):
        self.assertTrue(hash.password('gamail1234', 'gmail', 16))


if __name__ == '__main__':
    unittest.main()
