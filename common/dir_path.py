
import os

def print_directory_contents(sPath):
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents()
        else:
            print(sChildPath)



if __name__ == '__main__':
    print_directory_contents('E:\PycharmProjects\cre_api_test\config')