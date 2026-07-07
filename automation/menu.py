import shlex
import sys

from automation.utils import run_streaming_command


def print_header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def print_main_menu():
    print_header("Automation Menu")
    print("1. Nmap Automation")
    print("2. Gobuster Automation")
    print("3. Exit")


def handle_nmap_menu():
    while True:
        print_header("Nmap Automation")
        print("1. Quick scan")
        print("2. Aggressive scan")
        print("3. Custom scan")
        print("4. Back")
        choice = input("Select an option: ").strip()

        if choice == "1":
            target = input("Enter target IP or domain: ").strip()
            if target:
                run_streaming_command(["nmap", "-F", target])
        elif choice == "2":
            target = input("Enter target IP or domain: ").strip()
            if target:
                run_streaming_command(["nmap", "-sC", "-sV", "-A", "-T4", target])
        elif choice == "3":
            target = input("Enter target IP or domain: ").strip()
            if target:
                custom_options = input("Enter custom Nmap options: ").strip()
                if custom_options:
                    args = ["nmap"] + shlex.split(custom_options) + [target]
                    run_streaming_command(args)
                else:
                    print("Custom options cannot be empty.")
        elif choice == "4":
            return
        else:
            print("Invalid option.")


def handle_gobuster_menu():
    print_header("Gobuster Directory Enumeration")
    target_url = input("Enter target URL: ").strip()
    wordlist_path = input("Enter wordlist path: ").strip()

    if not target_url or not wordlist_path:
        print("Target URL and wordlist path are required.")
        return

    command = ["gobuster", "dir", "-u", target_url, "-w", wordlist_path]
    run_streaming_command(command)


def main_loop():
    while True:
        print_main_menu()
        try:
            choice = input("Select an option: ").strip()
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting.")
            sys.exit(0)

        if choice == "1":
            handle_nmap_menu()
        elif choice == "2":
            handle_gobuster_menu()
        elif choice == "3":
            print("Exiting.")
            sys.exit(0)
        else:
            print("Invalid option.")
