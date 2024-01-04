import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match:= re.search(r'^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$', ip):
        for i in re.split(r'\.', match[0]): 
            if int(i)<0 or int(i)>255: return False
        return True     
    return False

if __name__ == "__main__":
    main()