#!/usr/bin/env python
"""
A script that reads a very large text file,
outputs the length of char strings separated
by "$" sign.

This script uses lazy function for reading the file,
and does not trim the end of line characters, behaves '\n'
as a character too (that affects the lengths of strings.)
"""

from utils import (get_filename, read_in_chunks,
                   calculate_len_of_strs)


if __name__ == '__main__':
    # GRAB FILENAME
    filename = get_filename()

    final_str = ""

    with open(filename) as bigfile:
        for piece in read_in_chunks(bigfile):
            final_str += calculate_len_of_strs(piece.rstrip().split('$'))

    print final_str
