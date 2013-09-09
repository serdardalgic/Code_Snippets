# Example; Named tuple benchmark.
# See this blog post:
# http://www.boduch.ca/2009/10/python-named-tuples.html

# Do imports.
from collections import namedtuple
from timeit import Timer

# Create a named tuple type along with fields.
MyTuple = namedtuple("MyTuple", "one two three")

# Instantiate a test named tuple and dictionary.
my_tuple = MyTuple(one=1, two=2, three=3)
my_dict = {"one": 1, "two": 2, "three": 3}


# Test function.  Read tuple values.
def run_tuple():
    one = my_tuple.one
    two = my_tuple.two
    three = my_tuple.three

# Test function.  Read dictionary values.


def run_dict():
    one = my_dict["one"]
    two = my_dict["two"]
    three = my_dict["three"]

# Main.
if __name__ == "__main__":

    # Setup timers.
    tuple_timer = Timer("run_tuple()",
                        "from __main__ import run_tuple")
    dict_timer = Timer("run_dict()",
                       "from __main__ import run_dict")

    # Display results.
    print "TUPLE:", tuple_timer.timeit(10000000)
    print "DICT: ", dict_timer.timeit(10000000)
