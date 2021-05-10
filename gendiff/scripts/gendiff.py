"""Main script of the project."""
import argparse


def main():
    """Start cli tool instance."""
    gendiff = argparse.ArgumentParser(description='Generate diff')
    gendiff.add_argument('first_file', type=str)
    gendiff.add_argument('second_file', type=str)
    gendiff.add_argument(
        '-f',
        '--f',
        metavar='FORMAT',
        type=str,
        help='set format of output',
    )
    args = gendiff.parse_args()
    print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()
