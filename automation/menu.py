import shlex
import sys
from urllib.parse import urlparse

from automation.utils import run_streaming_command


def print_header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def print_main_menu():
    print_header("Automation Menu")
    print("1. Nmap Automation")
    print("2. Gobuster Automation")
    print("3. Enum4linux Automation")
    print("4. Exit")


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


def normalize_target_url(target):
    parsed = urlparse(target)
    if parsed.scheme and parsed.netloc:
        return target
    return "http://" + target


def handle_gobuster_menu():
    print_header("Gobuster Directory Enumeration")
    target_url = input("Enter target URL or IP: ").strip()
    wordlist_path = input("Enter wordlist path: ").strip()

    if not target_url or not wordlist_path:
        print("Target URL or IP and wordlist path are required.")
        return

    normalized_url = normalize_target_url(target_url)
    command = ["gobuster", "dir", "-u", normalized_url, "-w", wordlist_path]
    run_streaming_command(command)


def handle_enum4linux_menu():
    print_header("Enum4linux Enumeration")
    target_ip = input("Enter target IP: ").strip()

    if not target_ip:
        print("Target IP is required.")
        return

    command = ["enum4linux", "-a", target_ip]
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
            handle_enum4linux_menu()
        elif choice == "4":
            print("Exiting.")
            sys.exit(0)
        else:
            print("Invalid option.")
