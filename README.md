# Python Line Count Exercise

a Python program that takes a directory as a required argument and a filename extension as optional argument that defaults to “.txt”. The program should locate all files with the given extension in the given directory and all its subdirectories to produce a list of all matching files with the numbers of lines within the file. The program should also output the total number of lines and the average number of lines per file. 

For example:

./file1.txt		10

./file2.txt		25

./d1/d1fa.txt	5

./d1/d1fb.txt	37

===============

Number of files found: 	4

Total number of lines:		77

Average lines per file:	19.25


## Requirements

python==3.7+


## Usage
+ Script usage: python script.py <path_to_directory> --ext <file_extension>

  * required argument: path_to_directory

  * optional argument: file_extension (default: .txt)

```bash
$ cd <this git repo>
$ python script.py ./mydir2 --ext .txt
./mydir2/b.txt 3
./mydir2/dir1/a.txt 0
./mydir2/dir1/dir1/b.txt 1
======================
Number of files found: 3
Total number of lines: 4
Average lines per file:: 1.3333333333333333
```

+ Module usage

Init function
```python
LineCounter(dir_: str, ext: str) -> None
```

Read in files recursively and count lines
```
LineCounter.get_line() -> tuple
```
 * example:
```python
from linecounter.linecounter import LineCounter

lc = LineCounter('./mydir2', '.txt')
lc.get_line()
```



## Implementation tips
* Using generators to count lines of large files (lazy evaluation):
   
   Instead of loading everything in the memory at once, I read a file by blocks to avoid OOM. Block sizes can be configured based on server environment.
```python
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
```

## unit tests
```python
python -m unittest    
```
1. Test for a 2-layer recursive directory listing .txt extension files
2. Test for a 3-layer recursive directory listing .txt extension files
3. Test for a 3-layer recursive directory listing .py extension (something other than .txt) files
4. Test for directory listing when there's no file of the same extension: should be able to handle division by zero

## pylint