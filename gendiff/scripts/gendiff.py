import argparse

from gendiff import generate_diff


def main():
    args = parse_args()
    diff = generate_diff(args.first_file, args.second_file, output_format=args.format)
    print(diff)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument(
        "-f",
        "--format",
        metavar="format",
        type=str,
        help="set the format of output",
        default="stylish",
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
