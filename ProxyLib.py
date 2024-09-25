import requests
import threading
import time

url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=350&country=all&ssl=all&anonymity=all"

response = requests.get(url, timeout=1)
proxy_list = response.text.splitlines()

proxiesList = []

def control(proxy):
    try:
        check = requests.get("https://www.google.com.tr/?hl=tr", proxies={'http': proxy, 'https': proxy}, timeout=5)
        if check.status_code == 200:
            proxiesList.append(proxy)
    except requests.exceptions.RequestException:
        pass

def main():
    threads = []
    for proxy in proxy_list:
        thread = threading.Thread(target=control, args=(proxy,))
        threads.append(thread)
        thread.start()
        time.sleep(0.3)

    for thread in threads:
        thread.join()
    
    return proxiesList
