import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--data", type = str, help = "input data")
_args = parser.parse_args()

assert _args.data != None, 'data should not be None'

while True:
    time.sleep(1)
    print(_args.data)
