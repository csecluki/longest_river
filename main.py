#!/usr/bin/env python3

import argparse
import time

from land import Land


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file-path', type=str, help=".csv file path with land data. If not specified random "
                                                            "land will be generated. ")
    parser.add_argument('--hide-stats', action='store_true', help="Do not show execution statistics. ")
    parser.add_argument('--hide-land', action='store_true', help="Do not show graphical representation of land. ")
    parser.set_defaults(hide_stats=False)
    return parser.parse_args()


def main():
    args = parse_args()

    start = time.process_time()

    land = Land(args.file_path)
    land_created = time.process_time()

    length, river_number = land.find_longest_river()
    problem_solved = time.process_time()

    if not args.hide_stats:
        print(
            f"Land creation: {int((land_created - start) * 10 ** 3)}ms",
            f"Solving problem: {round(problem_solved - land_created, 2)}s",
            f"Rivers found: {river_number}",
            f"Longest river: {length}",
            sep='\n'
        )

    if not args.hide_land:
        print(land)


if __name__ == '__main__':
    main()
