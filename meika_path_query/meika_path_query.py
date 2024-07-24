from art import *
import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
import os
init()


def load_wordlist(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]
def scan_path(base_url, wordlist_file):

    found_paths = []

    def scan_url(path):
        url = f"{base_url}/{path}"
        try:
            response = requests.get(url, headers={"Cache-Control": "no-cache"})
            if response.status_code == 200:
                print(f"{Fore.GREEN}[+] Found: {url} (Status Code: 200){Style.RESET_ALL}")
                found_paths.append(url)
            elif response.status_code == 304:
                print(f"{Fore.GREEN}[+] Found (Not Modified): {url} (Status Code: 304){Style.RESET_ALL}")
                found_paths.append(url)
            elif 300 <= response.status_code < 400:
                print(f"{Fore.YELLOW}[~] Redirect: {url} (Status Code: {response.status_code}){Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[-] Not found: {url} (Status Code: {response.status_code}){Style.RESET_ALL}")
        except requests.RequestException as e:
            print(f"{Fore.RED}[!] Error scanning {url}: {e}{Style.RESET_ALL}")

    wordlist = load_wordlist(wordlist_file)

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(scan_url, wordlist)

    print(f"{Fore.GREEN}\n[+] Found paths:")
    for path in found_paths:
        print(path)
    print(Style.RESET_ALL)
