from art import *
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from meika_path_query import meika_path_query


def main():
    print(text2art("MEIKA"))

    while True:
        print("Select an option:")
        print("1. Start Path Scanner")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print(text2art("PATH QUERY"))
            base_url = input("Input website URL: ")
            wordlist_file = 'meika_path_query/wordlist.txt'
            meika_path_query.scan_path(base_url, wordlist_file)
        elif choice == "2":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
