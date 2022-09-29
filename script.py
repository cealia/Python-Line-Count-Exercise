"""
The script for using LineCounter
required argument: path_to_directory
optional argument: file extension (default: .txt)
"""
import argparse
from linecounter import LineCounter

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('dir', type=str)
    parser.add_argument('--ext', default='.txt', type=str)

    args = parser.parse_args()
    dir_ = args.dir
    extension = args.ext

    lc = LineCounter(dir_, extension)
    lc.get_line()
