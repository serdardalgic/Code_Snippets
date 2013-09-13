import mmap
import os
import struct
import time


def main():
    # Open the file for reading
    fd = os.open('/tmp/mmaptest', os.O_RDONLY)

    # Memory map the file
    buf = mmap.mmap(fd, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_READ)

    i = None
    s = None

    while 1:
        new_i = struct.unpack('i', buf[:4])
        new_s = struct.unpack('3s', buf[4:7])

        if i != new_i or s != new_s:
            print "i: {} => {}".format(i, new_i)
            print "s: {} => {}".format(s, new_s)
            print 'Press Ctrl-C to exit'
            i = new_i
            s = new_s

        time.sleep(1)


if __name__ == '__main__':
    main()
