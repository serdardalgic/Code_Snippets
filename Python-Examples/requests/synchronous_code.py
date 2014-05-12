try:
    from requests import Session
except ImportError:
    print "You should install requests package with pip"
    import sys
    sys.exit(-1)
import time

session = Session()
start_timer = time.time()
# first requests starts and blocks until finished
response_one = session.get('http://httpbin.org/get')
latency_one = time.time() - start_timer

# second request starts once first is finished
response_two = session.get('http://httpbin.org/get?foo=bar')
latency_two = time.time() - start_timer
# both requests are complete

print('response one status: {0}, response time: {1}'.format(
    response_one.status_code, latency_one))
print(response_one.content)
print('response two status: {0}, response time: {1}'.format(
    response_two.status_code, latency_two))
print(response_two.content)
print('total time: {0}'.format(time.time() - start_timer))
