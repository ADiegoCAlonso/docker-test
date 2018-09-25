#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--your-name",
        type=str,
        help="Test param",
        required=True
    )
    args = parser.parse_args()

    name = args.your_name

    print("Hello, {name}!".format(name=name))
    print("Bye, {name}!".format(name=name))
