import argparse
import logging
import time

from complexityfinder.finder import log_setter, complexity_finder, FunctionFailure
from complexityfinder.demo import demo
from complexityfinder.complexity import BadArgument

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
        from complexityfinder.your_function import fun, setup, clean
        try:
            complexity_finder(fun, setup, clean).print_some_info()
        except BadArgument:
            print("Bad argument has been passed to the function")
        except FunctionFailure:
            print("Provided function has failed")
        except:
            print("Something terribly wrong has happened")


if __name__ == '__main__':
    main()
