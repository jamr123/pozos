from time import sleep
import lecturas
import signal
import sys

IO=lecturas.Data()


def signal_handler(sig, frame):
    sys.exit(1)

while True:

    signal.signal(signal.SIGINT, signal_handler)
    sleep(1)