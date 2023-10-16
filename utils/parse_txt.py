# parse the wiki.txt file by space line
# the article title line followed by the space line
# the article content followed by the article title line

import time

# common ways to read by lines
def read_lines(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        print("read lines successfully")
        print("total lines: ", len(lines))
        return lines

# to read very large file, we use generator
def read_file(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line
        
def parse_txt(file_path):
    count = 0
    for line in read_file(file_path):
        if line == '\n':
            count += 1
    return count

if __name__ == '__main__':

    start = time.time()
    print("total articles: ", parse_txt('data/wiki.txt'))
    end = time.time()
    print("time: ", end - start)