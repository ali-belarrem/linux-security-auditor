# auditor.py
# Responsible for running security checks on the Linux system

import subprocess
import socket

def check_firewall():
    # Check if UFW firewall is active
    try:
        result = subprocess.run(
            ["ufw", "status"],
            capture_output=True,
            text=True
        )
        if "active" in result.stdout.lower():
            return {"check": "Firewall (UFW)", "status": "PASS", "detail": "Firewall is active"}
        else:
            return {"check": "Firewall (UFW)", "status": "FAIL", "detail": "Firewall is not active"}

    except FileNotFoundError:
        return {"check": "Firewall (UFW)", "status": "WARNING", "detail": "UFW not found on this system"}

    except Exception as e:
        return {"check": "Firewall (UFW)", "status": "ERROR", "detail": str(e)}


def check_open_ports():
    # Check for commonly dangerous open ports
    dangerous_ports = {
        21: "FTP",
        23: "Telnet",
        3306: "MySQL",
        5900: "VNC",
        6379: "Redis"
    }

    results = []
    for port, service in dangerous_ports.items():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            connection = sock.connect_ex(("127.0.0.1", port))

            if connection == 0:
                results.append({
                    "check": f"Port {port} ({service})",
                    "status": "FAIL",
                    "detail": f"Dangerous port {port} is open"
                })
            else:
                results.append({
                    "check": f"Port {port} ({service})",
                    "status": "PASS",
                    "detail": f"Port {port} is closed"
                })
            sock.close()

        except Exception as e:
            results.append({
                "check": f"Port {port} ({service})",
                "status": "ERROR",
                "detail": str(e)
            })

    return results
def check_file_permissions():
    # Check if sensitive system files have correct permissions
    import os

    sensitive_files = [
        "/etc/passwd",
        "/etc/shadow",
        "/etc/sudoers"
    ]

    results = []
    for filepath in sensitive_files:
        try:
            if os.path.exists(filepath):
                permissions = oct(os.stat(filepath).st_mode)[-3:]
                if permissions in ["644", "400", "440"]:
                    results.append({
                        "check": f"File {filepath}",
                        "status": "PASS",
                        "detail": f"Permissions are safe: {permissions}"
                    })
                else:
                    results.append({
                        "check": f"File {filepath}",
                        "status": "FAIL",
                        "detail": f"Unsafe permissions detected: {permissions}"
                    })
            else:
                results.append({
                    "check": f"File {filepath}",
                    "status": "WARNING",
                    "detail": "File not found on this system"
                })

        except Exception as e:
            results.append({
                "check": f"File {filepath}",
                "status": "ERROR",
                "detail": str(e)
            })

    return results
    
def check_user_accounts():
    # Check for dangerous user account configurations
    results = []

    try:
        result = subprocess.run(
            ["cat", "/etc/passwd"],
            capture_output=True,
            text=True
        )

        users_with_shell = []
        for line in result.stdout.splitlines():
            parts = line.split(":")
            if len(parts) >= 7 and parts[6] in ["/bin/bash", "/bin/sh"]:
                users_with_shell.append(parts[0])

        if len(users_with_shell) > 2:
            results.append({
                "check": "User Accounts",
                "status": "WARNING",
                "detail": f"Multiple users with shell access: {', '.join(users_with_shell)}"
            })
        else:
            results.append({
                "check": "User Accounts",
                "status": "PASS",
                "detail": f"Shell access users: {', '.join(users_with_shell)}"
            })

    except Exception as e:
        results.append({
            "check": "User Accounts",
            "status": "WARNING",
            "detail": "Could not read user accounts on this system"
        })

    return results