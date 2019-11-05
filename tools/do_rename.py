# coding: utf8

import argparse
import os
import re

def do_rename(path, src, dst, recursive):
    success_count = 0
    if not path.endswith('\\'):
        path = path + '\\'
    dir_list = os.listdir(path)
    for filename in dir_list:
        abs_path = os.path.join(path, filename) 
        if os.path.isdir(abs_path):
            if not recursive == None:
                success_count += do_rename(abs_path, src, dst, recursive)
        else:
            file_prefix = filename.split('.')[0:-1]
            file_prefix = '.'.join(file_prefix)
            file_ext = filename.split('.')[-1]

            if src.startswith('.') and dst.startswith('.'):
                if src[1:] == file_ext:
                    old_filename = path + filename
                    new_filename = path + file_prefix + dst
                    print ('%s ---> %s' % (old_filename, new_filename))
                    success_count += 1
                    os.rename(old_filename, new_filename)

    
    return success_count



def usage():
    desc = '''
        do_rename.py path src dst 
        do_rename.py path src dst -r 1
    '''
    parser = argparse.ArgumentParser(usage=desc)
    
    parser.add_argument("-r", help="recursive. apply to subdirectory.")
    parser.add_argument("path", help="path")
    parser.add_argument("src", help="source")
    parser.add_argument("dst", help="destination")
    args = parser.parse_args()
    success_count = do_rename(args.path, args.src, args.dst, args.r)
    print ('rename count: %d' % success_count)

def main():
    # todo 
    usage()

if __name__== "__main__":
    main()