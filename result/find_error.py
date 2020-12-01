# !/usr/bin/python
# -*-coding:utf-8 -*-
import glob2


def count(filepath):
    """
    filepath: 文件所在目录
    """
    for file in glob2.glob(filepath+'weibo2.train.bmes'):
        is_find_entity = False

        with open(file, 'r', encoding='utf-8') as fin:
            lines = fin.readlines()
            for idx, line in enumerate(lines):
                if len(line.strip()) < 3:
                    continue
                if ' B-' in line:
                    is_find_entity = True
                elif ' E-' in line:
                    is_find_entity = False
                elif ((' O' in line or ' S-' in line) and is_find_entity)  or (' M-' in line and not is_find_entity):
                    print(idx, line)
                else:
                    pass


if __name__ == "__main__":
    bmesdir = './'
    count(bmesdir)
