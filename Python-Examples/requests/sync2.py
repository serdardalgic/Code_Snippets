from requests import Session
import time


session = Session()
start_timer = start_of_prog_time = time.time()

time_dict = {}

for num in xrange(1, 100):
    response = session.get('http://httpbin.org/get')
    time_dict[str(num)] = time.time() - start_timer
    start_timer = time.time()


end_time = time.time()

for num, t in time_dict.items():
    print num, "-->", t

print "Total time:", end_time - start_of_prog_time
