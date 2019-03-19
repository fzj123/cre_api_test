
import csv
import os


def read_csv():
    request_path = 'E:\PycharmProjects\cre_api_test\date'
    print(request_path)

    with open(request_path + '/request_case.csv', "r") as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        return rows


if __name__ == '__main__':
    cas_req = [req for req in read_csv() if req[0] == '用户登出']
    print(cas_req)


