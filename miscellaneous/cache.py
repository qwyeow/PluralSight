"""
Use class instance to cache state variable
Use __call__ to create calleable instance
Caching can improve performance between calls
""" 
import socket
from pprint import pprint as pp


class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        """
        Cache the host and address

        Arg:
            host: host name

        Return:
            IP address
        """
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()   

    def has_host(self, host):
        return host in self._cache     


if __name__ == "__main__":
    resolve = Resolver()
    resolve("sixty-north.com")
    pp(resolve._cache)
    resolve("pluralsight.com")
    pp(resolve._cache)
    pp(resolve.has_host("sixty-north.com"))
    resolve.clear()
    pp(resolve._cache)
    pp(resolve.has_host("sixty-north.com"))


'''
$ python3
>>> import cache
>>> R = cache.Resolver()
>>> R("sixty-north.com")
'93.93.131.30'
>>> R("pluralsight.com")
'54.191.217.222'
>>> R._cache
{'sixty-north.com': '93.93.131.30', 'pluralsight.com': '54.191.217.222'}
>>> R.has_host("sixty-north.com")
True
>>> R.clear()
>>> R.has_host("sixty-north.com")
False
>>> R._cache
{}
'''