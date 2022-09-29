"""
The definition of LineCounter
"""
import glob
import os

class LineCounter:
    """
    LineCounter class that takes a directory and a file extension,
    outputs (the number of files found, the total number of lines, and the average lines per file)
    """
    def __init__(self, dir_: str, ext: str):
        """Init function"""
        self.dir_ = dir_
        self.ext = ext
    def get_line(self)->tuple:
        """Read in files recursively and count lines"""
        files = []
        for file in glob.glob(os.path.join(self.dir_, "**/*"+self.ext), recursive=True):
            files.append(file)
        num_of_files = len(files)
        lines = []
        for file in files:
            with open(file, "r") as f_file:
                try:
                    lines.append(sum(b.count("\n") for b in self.blocks(f_file)))
                    print(f'{file} {lines[-1]}')
                except UnicodeDecodeError:
                    print('Not utf-8 encoded')
        total_num_of_lines = sum(lines)
        if num_of_files:
            avg = total_num_of_lines/num_of_files
        else:
            avg = float('-inf')
        print('======================')
        print(f'Number of files found: {num_of_files}')
        print(f'Total number of lines: {total_num_of_lines}')
        print(f'Average lines per file:: {avg:3}')
        return (num_of_files, total_num_of_lines, avg)
    @staticmethod
    def blocks(file, size=1024 * 1024):
        """
        Use a generator to read blocks from a file one by one;
        Avoid oom on an extremely large file
        """
        while True:
            block = file.read(size)
            if not block:
                break
            yield block
