import sys

FILENAME = "bigfile.txt"


def print_help():
    """
    Prints help on how to use the program.
    """
    print "****************************************************"
    print "* You should give a filename as an argument to the *"
    print "* program, or just run it directly (assuming there *"
    print "* is a \"bigfile.txt\" file in current directory.    *"
    print "* Make sure the file exists in your directory      *"
    print "****************************************************"


def get_filename():
    if len(sys.argv) == 2:
        return sys.argv[1]
    elif len(sys.argv) == 1:
        return FILENAME
    else:
        print_help()
        sys.exit(-1)


def calculate_len_of_strs(splitted_list):
    return ' '.join(str(lngth) for lngth in map(len, splitted_list))


def read_in_chunks(f_obj, chunk_size=3 * 4096):
    """
    Lazy function(Iterator) to read a file piece by piece
    with default chunk size 3 * 4K = 12K.
    """
    while True:
        data = f_obj.read(chunk_size)
        if not data:
            break
        yield data
