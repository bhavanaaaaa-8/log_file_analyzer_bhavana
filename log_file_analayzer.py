
import re
from collections import Counter


# Step 1: Parse individual log lines
def parse_log_line(line):

    log_pattern = re.compile(
        r'(\S+) \S+ \S+ \[.*?\] '
        r'"(\S+) (.*?) HTTP/[\d.]+" '
        r'(\d{3})'
    )

    match = log_pattern.search(line)

    if not match:
        return None

    ip, method, endpoint, status = match.groups()

    return {
        "ip": ip,
        "method": method,
        "endpoint": endpoint,
        "status": int(status)
    }


# Step 2: Analyse parsed log entries
def analyze_logs(filename):

    ip_addresses = Counter()
    endpoints = Counter()
    status_codes = Counter()

    total_requests = 0
    error_requests = 0
    malformed_lines = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:

            for line in file:

                entry = parse_log_line(line)

                # Skip malformed entries
                if entry is None:
                    malformed_lines += 1
                    continue

                total_requests += 1

                ip_addresses[entry["ip"]] += 1
                endpoints[entry["endpoint"]] += 1
                status_codes[entry["status"]] += 1

                if entry["status"] >= 400:
                    error_requests += 1

    except FileNotFoundError:
        print("Error: Log file not found!")
        return

    except PermissionError:
        print("Error: Permission denied!")
        return

    # Step 3: Display report
    print("\n===== SERVER LOG ANALYSIS =====")

    print("Total Requests:", total_requests)
    print("Error Responses:", error_requests)
    print("Malformed Lines:", malformed_lines)

    print("\nHTTP Status Codes:")
    for code, count in sorted(status_codes.items()):
        print(code, ":", count)

    print("\nTop 5 IP Addresses:")
    for ip, count in ip_addresses.most_common(5):
        print(ip, ":", count)

    print("\nTop 5 Endpoints:")
    for endpoint, count in endpoints.most_common(5):
        print(endpoint, ":", count)


# Main program
if __name__ == "__main__":
    analyze_logs("server.log")
