#!/usr/bin/env python
import argparse


parser = argparse.ArgumentParser("Training script")
parser.add_argument("path")
parser.add_argument("--type", default="file-md5sum", choices=["file-md5sum"])


def main(args):
    if args.type == "file-md5sum":
        from src.md5sum import MD5SUMBabySitter
        MD5SUMBabySitter(args.path).start()


if __name__ == "__main__":
    main(parser.parse_args())
