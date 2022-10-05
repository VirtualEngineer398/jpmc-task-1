import unittest
import client

class Testing(unittest.TestCase):
    def test_client_ratio(self):
        self.assertEqual(client.getRatio(20.3,0),0)
        self.assertGreater(client.getRatio(20.3,22.3),0)

if __name__ == '__main__':
    unittest.main()