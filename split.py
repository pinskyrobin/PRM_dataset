import sys


def split(filename: str, chunk_size: int):
    line_cnt = 0
    file_cnt = 0
    curr_file = filename + '_' + str(file_cnt)
    with open(filename, 'r', encoding='utf-8') as rf:
        for line in rf:
            with open(curr_file, "a") as wf:
                wf.write(line)
            line_cnt += 1
            if line_cnt == chunk_size:
                file_cnt += 1
                curr_file = filename + '_' + str(file_cnt)
                line_cnt = 0


"""
Run like this:
    python split.py bigfile.txt 1024
    which means this script can split bigfile.txt into small files with 1024 lines
"""
if __name__ == '__main__':
    chunk_size = 65535
    if sys.argv[2] is not None:
        print(sys.argv[2])
        chunk_size = int(sys.argv[2])
    split(sys.argv[1], chunk_size)
