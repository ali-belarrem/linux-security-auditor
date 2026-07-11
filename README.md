# Linux Security Auditor — CLI Tool

A Python command-line tool that audits Linux system security by checking
firewall status, dangerous open ports, sensitive file permissions, and
user accounts. Generates a full security report at the end.

Inspired by security concepts learned through the Cisco Network Defense
certification and current industrial internship at OCP Group.

## Features
- Check if UFW firewall is active
- Scan for dangerous open ports (FTP, Telnet, MySQL, VNC, Redis)
- Verify sensitive file permissions (/etc/passwd, /etc/shadow, /etc/sudoers)
- Inspect user accounts with shell access
- Export a full audit report to a text file

## Technologies Used
- Python 3
- subprocess module
- socket module
- os module

## Usage

Run the tool using this command:

    python main.py

Follow the prompts — the tool will run all checks automatically
and ask if you want to save the report.

## Project Structure

    linux-security-auditor/
    ├── main.py          Main entry point
    ├── auditor.py       All security check functions
    ├── report.py        Report generation logic
    └── requirements.txt Dependencies

## Author
Ali Belarrem — First Year Computer Science Student | OCP Intern