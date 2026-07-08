# Pentest Automation Tool

A Python-based CLI utility designed to simplify and automate common reconnaissance and enumeration tasks during penetration testing. It provides an interactive menu to manage tools like Nmap, Gobuster, Enum4linux, and DNS utilities.

## Features
- **Nmap:** Perform quick, aggressive, or fully custom port scans.
- **Gobuster:** Automated directory brute-forcing for web applications.
- **DNS Enumeration:** Query various DNS records (AXFR, NS, MX, SOA, TXT, etc.).
- **Enum4linux:** Simplified SMB/Windows enumeration.

## Prerequisites
Ensure the following tools are installed on your system and accessible via your `$PATH`:
- `nmap`
- `gobuster`
- `enum4linux`
- `dig` (usually part of `dnsutils`)

## Installation
1. Clone the repository:
   ```bash
   cd /opt
   git clone https://github.com/yigitemreyildirim/NyxaRadar
   cd /NyxaRadar
   python main.py
