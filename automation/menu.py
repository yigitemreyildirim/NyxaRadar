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
    print("4. DNS Enumeration")
    print("5. Exit")


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


def build_dig_command(choice, target, nameserver=None):
    if choice == "1":
        return ["dig", f"@{nameserver or 'ns1.hedefsite.com'}", target, "AXFR"]
    if choice == "2":
        return ["dig", target, "NS"]
    if choice == "3":
        return ["dig", target, "MX"]
    if choice == "4":
        return ["dig", target, "SOA"]
    if choice == "5":
        return ["dig", target, "TXT"]
    if choice == "6":
        return ["dig", target, "ANY"]
    if choice == "7":
        return None
    return None


def handle_dns_menu():
    while True:
        print_header("DNS Enumeration")
        print("1. AXFR transfer")
        print("2. NS records")
        print("3. MX records")
        print("4. SOA records")
        print("5. TXT records")
        print("6. ANY records")
        print("7. Custom dig query")
        print("8. Back")
        choice = input("Select an option: ").strip()

        if choice == "8":
            return

        target = input("Enter target domain: ").strip()
        if not target:
            print("Target domain is required.")
            continue

        if choice == "1":
            nameserver = input("Enter nameserver (default: ns1.hedefsite.com): ").strip() or "ns1.hedefsite.com"
            command = build_dig_command(choice, target, nameserver)
        elif choice == "7":
            custom_options = input("Enter custom dig options: ").strip()
            if not custom_options:
                print("Custom dig options cannot be empty.")
                continue
            command = ["dig"] + shlex.split(custom_options) + [target]
        else:
            command = build_dig_command(choice, target)

        if command is None:
            print("Invalid option.")
            continue

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
            handle_dns_menu()
        elif choice == "5":
            print("Exiting.")
            sys.exit(0)
        else:
            print("Invalid option.")
