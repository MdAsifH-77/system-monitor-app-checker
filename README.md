# System Health Monitor & Application Health Checker

## Description

This project includes:

- A System Health Monitor script (`system_monitor.py`) that checks CPU, Memory, and Disk usage, logging warnings if thresholds are exceeded.
- An Application Health Checker script (`app_health_checker.py`) that checks if a specified URL is up using HTTP status codes.

## How to Run

1. Ensure Python is installed on your system.
2. Install required packages:
```
pip install psutil requests
```
3. Run the system monitor:
```
python system_monitor.py
```
4. Run the application health checker:
```
python app_health_checker.py
```

## Output

- System monitor prints CPU, Memory, and Disk usage and logs warnings to `system_health.log` if thresholds are exceeded.
- Application health checker prints if the application is up or down based on HTTP status codes.
