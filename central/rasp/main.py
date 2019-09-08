from time import sleep
import serialData
import signal
import sys

ser=serialData.Data()


def signal_handler(sig, frame):
    sys.exit(1)

while True:

    signal.signal(signal.SIGINT, signal_handler)
    sleep(1)