import re
from collections import defaultdict
from datetime import datetime


def analyze_logs():
    alerts = []

    try:
        with open("logs.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        return []

    failed_by_ip = defaultdict(int)

    for line in lines:
        line = line.strip()

        timestamp_match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", line)
        timestamp = timestamp_match.group() if timestamp_match else "Unknown"

        ip_match = re.search(r"IP:(\d+\.\d+\.\d+\.\d+)", line)
        ip = ip_match.group(1) if ip_match else "Unknown"

        if "Failed login" in line:
            failed_by_ip[ip] += 1

        if "Admin login" in line:
            if timestamp != "Unknown":
                hour = int(timestamp.split()[1].split(":")[0])
                if hour >= 0 and hour <= 5:
                    alerts.append({
                        "title": "Suspicious Admin Login (Off Hours)",
                        "severity": "High",
                        "details": f"{timestamp} | IP: {ip}"
                    })

        if "Large data transfer" in line:
            alerts.append({
                "title": "Unusual Data Transfer Activity",
                "severity": "Medium",
                "details": f"{timestamp} | IP: {ip}"
            })

    for ip, count in failed_by_ip.items():
        if count >= 3:
            alerts.append({
                "title": "Brute Force Attempt Detected",
                "severity": "High",
                "details": f"IP: {ip} | Failed Attempts: {count}"
            })

    return alerts