import json
import unittest
import requests

from common.config_read import read_conf
from common.csv_read import read_csv

class CasCase(unittest.TestCase):
    def setUp(self):
        print('run before every test')

    def tearDown(self):
        print('run after every test')

    def test_login(self):
        cas_url =  read_conf().get("web_url", "cas_url")
        cas_csv = [req for req in read_csv()if req[0] == '用户认证' ]
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
        url = cas_url + cas_csv[0][2] + cas_csv[0][3]
        print(url)
        data =cas_csv[0][4]
        print(data)
        response = requests.post(url=url, headers=headers, data=data)
        if response.status_code == 200:
            results = json.loads(response.text)
            self.assertEqual(response.status_code, 200)
            print(results)
        else:
            print(url + "http error info:%s" % response.status_code)

    def test_logout(self):
        cas_url = read_conf().get("web_url", "cas_url")
        cas_csv = [req for req in read_csv() if req[0] == '用户登出']
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
        url = cas_url + cas_csv[0][2] + cas_csv[0][3]
        print(url)
        data = cas_csv[0][4]
        print(data)
        response = requests.post(url=url, headers=headers, data=data)
        if response.status_code == 200:
            results = json.loads(response.text)
            self.assertEqual(response.status_code, 200)
            print(results)
        else:
            print(url + "http error info:%s" % response.status_code)



# if __name__ == "__main__":
#     unittest.main()