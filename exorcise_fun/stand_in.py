#!/usr/bin/env python3

import shutil
import pathlib
import sys
import subprocess

from exorcise_fun import exorcise


def main() -> None:
    which_process = subprocess.Popen(
        ["which", "-a", pathlib.Path(sys.argv[0]).name], stdout=subprocess.PIPE
    )

    command_list = [line.decode().strip() for line in which_process.stdout][
        1:2
    ] + sys.argv[1:]

    our_process = subprocess.Popen(
        " ".join(command_list),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    exorcise(input_file=our_process.stdout, output_file=sys.stdout)
    exorcise(input_file=our_process.stderr, output_file=sys.stderr)

    our_process.wait()


if __name__ == "__main__":
    main()
