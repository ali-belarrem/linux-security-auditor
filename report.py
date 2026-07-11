# report.py
# Responsible for generating a security audit report as a text file

from datetime import datetime

def generate_report(results):
    # Create a unique report filename using current timestamp
    filename = f"security_report_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    with open(filename, "w") as f:
        f.write("=" * 50 + "\n")
        f.write("   Linux Security Auditor - Report\n")
        f.write(f"   Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n\n")

        passed = 0
        failed = 0
        warnings = 0

        for item in results:
            f.write(f"[{item['status']}] {item['check']}\n")
            f.write(f"      Detail: {item['detail']}\n\n")

            if item['status'] == "PASS":
                passed += 1
            elif item['status'] == "FAIL":
                failed += 1
            else:
                warnings += 1

        f.write("=" * 50 + "\n")
        f.write("SUMMARY\n")
        f.write("=" * 50 + "\n")
        f.write(f"Total Checks : {len(results)}\n")
        f.write(f"Passed       : {passed}\n")
        f.write(f"Failed       : {failed}\n")
        f.write(f"Warnings     : {warnings}\n")

    print(f"\n[+] Report saved to: {filename}")
    return filename