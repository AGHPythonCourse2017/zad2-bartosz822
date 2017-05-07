import argparse
import logging
import time

from complexityfinder import log_setter
from demo import demo

log = False

def main():
    parser = argparse.ArgumentParser(description='Parse generator options')

    parser.add_argument('--log', '-l', action='store_true',
                        help='If set, complexity finder will log its work')

    parser.add_argument('--demo', '-d', action='store_true',
                        help='Run a demo showing how the module works')

    args = parser.parse_args()

    if args.log:
        logging.basicConfig(level=logging.DEBUG, format='%(levelname)s %(asctime)s %(message)s',
                            filename=time.asctime() + ' complexity_finder.log')
        log_setter(True)

    if args.demo:
        demo()
    else:
        from your_function import fun, setup, clean
        from complexityfinder import complexity_finder
        complexity_finder(fun, setup, clean).print_some_info()


if __name__ == '__main__':
    main()