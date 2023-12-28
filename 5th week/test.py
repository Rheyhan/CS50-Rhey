import argparse
import requests
import sys

try:
    parser=argparse.ArgumentParser()
    parser.add_argument("Value", help="Btc quantity")
    args = vars(parser.parse_args())
except:
    sys.exit("Missing command-line argument")
try:
    value = float(args["Value"])
except:
    sys.exit("Command-line argument is not a number")

r=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
curerentrate=r.json()["bpi"]["USD"]["rate"]
temp=f'{float(curerentrate.replace(",", ""))*value:.4f}'
print(f'${float(temp):,}')