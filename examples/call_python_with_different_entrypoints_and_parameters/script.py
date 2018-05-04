#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse


if __name__ == '__main__':
    print("Hello")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--param1",
        type=str,
        help="Test param",
        required=True
    )
    args = parser.parse_args()

    print("{}".format(args.param1))


