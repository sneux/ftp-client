import sys
import argparse

from interpreter import FtpInterpreter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args(sys.argv[1:])

    ftps_interpreter = FtpInterpreter(debug=args.debug)
    ftps_interpreter.cmdloop()


if __name__ == '__main__':
    main()
