Copy code
import requests
import time
from functools import wraps

def cache_result(expiration_time):
    def decorator(func):
        cache = {}

        @wraps(func)
        def wrapper(url):
            if url in cache and time.time() - cache[url]['timestamp'] < expiration_time:
                print(f"Using cached result for {url}")
                return cache[url]['content']

            print(f"Fetching page for {url}")
            response = requests.get(url)
            content = response.text

            cache[url] = {
                'content': content,
                'timestamp': time.time()
            }

            return content

        return wrapper

    return decorator

@cache_result(expiration_time=10)
def get_page(url):
    return requests.get(url).text

url = 'http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.example.com'
content = get_page(url)
print(content)
