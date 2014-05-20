from requests_futures.sessions import FuturesSession
import time


session = FuturesSession(max_workers=50)
start_timer = start_of_prog_time = time.time()

time_dict = {}
start_dict = {}
reqs = []

for num in xrange(1, 1000):
    future = session.get('http://httpbin.org/get')
    start_dict[str(num)] = time.time() - start_timer
    start_timer = time.time()
    reqs.append(future)

num = 1

for req in reqs:
    response = req.result()
    time_dict[str(num)] = time.time() - start_dict[str(num)]
    num = num + 1

end_time = time.time()

for num, t in time_dict.items():
    print num, "-->", t

print "Total time:", end_time - start_of_prog_time
