import sys
import requests

print(sys.executable)
print(sys.version)
r = requests.get("https://www.google.com/")
print(r.status_code)
n = input()
print(n * 2)
