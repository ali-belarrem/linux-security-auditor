# main.py
# Main entry point of the Linux Security Auditor tool

from auditor import check_firewall, check_open_ports, check_file_permissions, check_user_accounts
from report import generate_report

def main():
    print("=" * 50)
    print("   Linux Security Auditor - CLI Tool")
    print("=" * 50)

    results = []

    # Run firewall check
    print("\n[*] Checking firewall status...")
    firewall_result = check_firewall()
    results.append(firewall_result)
    print(f"[{firewall_result['status']}] {firewall_result['check']}: {firewall_result['detail']}")

    # Run open ports check
    print("\n[*] Checking for dangerous open ports...")
    port_results = check_open_ports()
    for r in port_results:
        results.append(r)
        print(f"[{r['status']}] {r['check']}: {r['detail']}")

    # Run file permissions check
    print("\n[*] Checking sensitive file permissions...")
    file_results = check_file_permissions()
    for r in file_results:
        results.append(r)
        print(f"[{r['status']}] {r['check']}: {r['detail']}")

    # Run user accounts check
    print("\n[*] Checking user accounts...")
    user_results = check_user_accounts()
    for r in user_results:
        results.append(r)
        print(f"[{r['status']}] {r['check']}: {r['detail']}")

    # Generate report
    save = input("\n[?] Save audit report to file? (y/n): ")
    if save.lower() == "y":
        generate_report(results)

    print("\n[*] Audit complete. Stay secure!")

if __name__ == "__main__":
    main()