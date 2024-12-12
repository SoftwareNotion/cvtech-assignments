import ctypes
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

hamImg = "https://upload.wikimedia.org/wikipedia/commons/a/a9/Ham_%284%29.jpg"
urllib.request.urlretrieve(hamImg, )