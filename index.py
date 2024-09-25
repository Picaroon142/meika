from art import *
import threading
import sys
import ProxyLib
import SubDomainMaker
import colorama
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from domainlib_path_query import domainlib_path_query

def main():
    print(text2art("DomainLib"))
    print(f'{colorama.Fore.YELLOW} Proxies are being set up... {colorama.Fore.RESET}')
    res = ProxyLib.main()

    while True:
        print("Select an option:")
        print("1. Start Path Scanner")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print(text2art("PATH QUERY"))
            base_url = input("Input website URL: ")
            fileName = input("Log file name: ")
            wordlist_file = 'domainlib_path_query/wordlist.txt'

            thread1 = threading.Thread(target=domainlib_path_query.scan_path(base_url, wordlist_file, fileName, res), args={})
            thread1.start()

            with open(".//domainlib_path_query//dlist.txt", 'r+', encoding='utf-8') as file:
                for subDomain in file:
                    base_url_subdomain = SubDomainMaker.DomainMake(base_url, subDomain)

                    thread2 = threading.Thread(target=domainlib_path_query.scan_path(base_url_subdomain, wordlist_file, fileName, res), args={})
                    thread2.start()
            
        elif choice == "2":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
