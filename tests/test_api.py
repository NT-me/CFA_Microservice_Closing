import unittest
import requests


class ApiTest(unittest.TestCase):

    def setUp(self):
        self.BASE_URL = 'http://127.0.0.1:8093/'

    def test_01_ClosinngContract(self):
        data = {
            "code_contract" : "L12345",
            "user_name" : "quentin"
        }
        r = requests.post(self.BASE_URL + "closing", json=data)
        print("testPostClosing" + r.text)
        self.assertEqual(r.status_code, requests.codes.ok)

    def test_02_getClosing(self):
        r = requests.get(self.BASE_URL + "closing")
        print("testGetContract" + r.text)
        self.assertEqual(r.status_code, requests.codes.ok)

    def test_03_GetClosingId(self):
        r = requests.get(self.BASE_URL + "closing/" + str(1))
        print("testGetClosingId :" + r.text)
        self.assertEqual(r.status_code, requests.codes.ok)


if __name__ == '__main__':
    unittest.main()
