try:
    from requests_futures.sessions import FuturesSession
except ImportError:
    print "You should install requests-futures package with pip"
    import sys
    sys.exit(-1)
import time

session = FuturesSession()
start_timer = time.time()
# first request is started in background
future_one = session.get('http://httpbin.org/get')
latency_one = time.time() - start_timer

# second requests is started immediately
future_two = session.get('http://httpbin.org/get?foo=bar')
latency_two = time.time() - start_timer

# wait for the first request to complete, if it hasn't already
response_one = future_one.result()
final_latency_one = time.time() - start_timer
print('response one status: {0}, latency_one: {1},'
      ' final_latency_one: {2}'.format(
          response_one.status_code, latency_one, final_latency_one))
print(response_one.content)

# wait for the second request to complete, if it hasn't already
response_two = future_two.result()
final_latency_two = time.time() - start_timer
print('response two status: {0}'.format(response_two.status_code))
print('response two status: {0}, latency_two: {1},'
      ' final_latency_two: {2}'.format(
          response_two.status_code, latency_two, final_latency_two))
print(response_two.content)
print('total time: {0}'.format(time.time() - start_timer))
