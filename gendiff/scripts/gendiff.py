import argparse


def main():
    """Creates gendiff cli tool instance."""
    gendiff = argparse.ArgumentParser(description='Generate diff')
    gendiff.add_argument('first_file', type=str)
    gendiff.add_argument('second_file', type=str)
    args = gendiff.parse_args()
    print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()
