🔐 Security Monitoring and Incident Response System
🛡 Mini SOC Project
📌 Project Overview

This project simulates a real-world Security Operations Center (SOC) environment by implementing log monitoring, threat detection, incident classification, and structured response handling.

The system analyzes system logs, detects suspicious behavior using predefined detection rules, generates automated alerts, and maintains incident records inside a centralized dashboard.

It demonstrates practical implementation of cybersecurity monitoring and incident management concepts.

🎯 Project Objectives

Analyze system logs to detect abnormal behavior

Implement a rule-based threat detection engine

Classify incidents based on severity levels

Generate automated security alerts

Maintain structured incident tracking

Provide centralized monitoring dashboard

Simulate real-world attack scenarios

🏗 Project Architecture
Log Collection (logs.txt)
        ↓
Log Analysis Engine (detection.py)
        ↓
Rule-Based Detection Logic
        ↓
Alert Generation
        ↓
SQLite Database (sentinelx.db)
        ↓
Flask Web Application
        ↓
Security Dashboard
        ↓
Incident Monitoring & Response
🔄 Workflow

Logs are collected from system activity

Detection engine processes logs using predefined rules

Suspicious activity generates an alert

Alert is stored in the database

Dashboard displays active and closed incidents

Analyst reviews and closes incidents

📂 Project Structure
Security-Monitoring-and-Incident-Response-SOC
│
├── app.py
├── detection.py
├── sentinelx.db
├── logs.txt
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── forgot_password.html
│   ├── dashboard.html
│   ├── open_alerts.html
│   └── closed_alerts.html
│
├── static/
│   └── style.css
│
└── README.md
🧠 Project Modules Breakdown

Although the project is implemented as a Flask web application inside the SentinelX-Dashboard folder, it logically consists of multiple functional modules:

🔎 Log Analysis

Processes system logs from logs.txt

Extracts timestamps, IP addresses, and activity patterns

Identifies suspicious behavior based on predefined rules

Feeds processed data into the detection engine

🚨 Detection Engine

Implements rule-based threat detection logic

Detects brute force attempts

Detects suspicious admin login

Detects large data transfer

Generates structured alerts with severity classification

🛡 Incident Response

Stores detected incidents inside SQLite database

Classifies incidents based on severity (Low / Medium / High)

Displays incidents on dashboard

Allows analyst to review and mark incidents as closed

Maintains structured incident lifecycle tracking

🔄 Future Enhancements

Real-time log monitoring

AI-based anomaly detection

Live analytics dashboard

Email & SMS alert integration

Automated response playbooks

SIEM tool integration

Cloud deployment support

🔎 Log Analysis
Example Logs Processed by the System
Failed login from IP 192.168.1.10
Admin login at 02:15 AM
Large data transfer detected (2GB)
✅ Normal Activity

Login during working hours

Limited failed login attempts

Internal IP access

Small data transfers

🚨 Suspicious Activity

Multiple failed login attempts

Admin login at unusual hours

External IP login

Large data transfer (>1GB)

Unauthorized access attempts

🚨 Detection Engine

The system uses rule-based logic to detect threats.

🔴 Brute Force Detection

Condition: Failed login attempts exceed threshold
Severity: HIGH

🔴 Suspicious Admin Login

Condition: Login outside working hours or from external IP
Severity: HIGH

🟡 Large Data Transfer

Condition: Data transfer > 1GB
Severity: MEDIUM

🔵 General Anomaly Detection

Condition: Abnormal activity pattern
Severity: LOW / MEDIUM

📊 Incident Classification
Severity	Description	Required Action
LOW	Minor anomaly	Monitor
MEDIUM	Suspicious activity	Investigation required
HIGH	Confirmed threat	Immediate response required
🛡 Incident Response Workflow

Detection Engine identifies suspicious activity

Automated alert is generated

Alert is stored in database

Incident is displayed on dashboard

Analyst reviews details

Appropriate response action is taken

Incident status updated to Closed after resolution

Possible Response Actions

Account Lock

Password Reset

IP Blocking

System Isolation

Escalation to Security Team

🧪 Simulated Attack Scenarios

Brute Force Attack

Midnight Admin Login

Large Data Exfiltration

Unauthorized Access Attempts

Each scenario triggers detection rules and generates alerts automatically.

🚀 Future Improvements

Real-time log monitoring

AI-based anomaly detection

Live analytics dashboard

Email/SMS alert integration

Automated response playbooks

SIEM integration

Cloud deployment support

💡 Technologies Used

Python

Flask

SQLite

HTML / CSS

Regex-Based Log Parsing

Rule-Based Threat Detection

👨‍💻 Developed As

Internship Project
Focused on Security Monitoring & Incident Response Simulation
