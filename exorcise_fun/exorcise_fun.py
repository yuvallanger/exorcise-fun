#!/usr/bin/env python3

import subprocess
import pathlib
import re
import argparse
import sys


# Ranges taken from <https://donald-barclay.com/2022/01/11/removing-emojis-from-text-data/>.
evil = re.compile(
    "["
    "\U000024c2-\U0001f251"
    "\U00002702-\U000027b0"
    #'\U00010000-\U0010ffff' # Wouldn't this range just match all the ones underneath it?
    "\U0001f1e0-\U0001f1ff"
    "\U0001f300-\U0001f5ff"
    "\U0001f600-\U0001f64f"
    "\U0001f680-\U0001f6ff"
    "]+",
)


def get_argparse_options() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input-file")
    parser.add_argument("-o", "--output-file")
    parser.add_argument("-e", "--stderr", help="Output to standard error.")

    args = parser.parse_args()

    return args


def exorcise(input_file, output_file) -> None:
    for line in input_file:
        if isinstance(line, bytes):
            new_line = evil.sub("", line.decode())
        else:
            new_line = evil.sub("", line)
        output_file.write(new_line)


def main() -> None:
    commandline_args = get_argparse_options()

    input_file = sys.stdin

    if commandline_args.stderr:
        output_file = sys.stderr
    else:
        output_file = sys.stdout

    if commandline_args.input_file is None and commandline_args.output_file is None:
        exorcise(input_file, output_file)

    elif (
        commandline_args.input_file is not None and commandline_args.output_file is None
    ):
        with open(commandline_args.input_file, "r") as input_file:
            exorcise(input_file, output_file)

    elif (
        commandline_args.input_file is None and commandline_args.output_file is not None
    ):
        with open(commandline_args.output_file, "w") as output_file:
            exorcise(input_file, output_file)

    else:
        with open(commandline_args.input_file, "r") as input_file, open(
            commandline_args.output_file, "w"
        ) as output_file:
            exorcise(input_file, output_file)


if __name__ == "__main__":
    main()
