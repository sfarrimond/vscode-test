import requests

r = requests.get("https://coreyms.com", timeout=30)
print(r.status_code)
