import ctypes
import mmap
import os
import struct


def main():
    # Create new empty file to back memory map on disk
    fd = os.open('/tmp/mmaptest', os.O_CREAT | os.O_TRUNC | os.O_RDWR)

    # Zero out the file to insure it's the right size
    assert os.write(fd, '\x00' * mmap.PAGESIZE) == mmap.PAGESIZE

    # Create the mmap instace with the following params:
    # fd: File descriptor which backs the mapping or -1 for anonymous mapping
    # length: Must in multiples of PAGESIZE (usually 4 KB)
    # flags: MAP_SHARED means other processes can share this mmap
    # prot: PROT_WRITE means this process can write to this mmap
    buf = mmap.mmap(fd, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_WRITE)

    # Now create an int in the memory mapping
    i = ctypes.c_int.from_buffer(buf)

    # Set a value
    i.value = 10

    # And manipulate it for kicks
    i.value += 1

    assert i.value == 11

    # Before we create a new value, we need to find the offset of the next free
    # memory address within the map
    offset = struct.calcsize(i._type_)

    # The offset should be uninitialized ('\x00')
    assert buf[offset] == '\x00'

    # Now create a string containing 'foo' by first creating a c_char array
    s_type = ctypes.c_char * (len('foo'))

    # Now create the ctypes instance
    s = s_type.from_buffer(buf, offset)

    # And finally set it
    s.raw = 'foo'

    print 'First 10 bytes of memory mapping: %r' % buf[:10]
    raw_input('Now run shared_memory_read.py and press ENTER')

    print
    print 'Changing i'
    i.value *= i.value

    print 'Changing s'
    s.raw = 'bar'

    new_i = raw_input('Enter a new value for i: ')
    i.value = int(new_i)

if __name__ == '__main__':
    main()
