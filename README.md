Log Analysis and Monitoring Script 
Introduction
This Python script automates log analysis and monitoring, providing real-time insights into your application's log files. It continuously monitors a specified log file, analyzes entries for specific keywords or patterns, and generates summary reports.
Features
Continuous Monitoring: Tracks new entries in the log file using tail -f.
Keyword Analysis: Counts occurrences of pre-defined keywords (errors, exceptions) or user-specified keywords from a configuration file (optional).
Summary Reports: Generates a report upon interruption (Ctrl+C) displaying the top occurring keywords and their counts.
Informative Logging: Utilizes Python's logging module for debugging and informational messages.
Error Handling: Gracefully handles KeyboardInterrupt to provide a summary report before exiting.
Installation
There's no installation required. Download the script (log-monitor.py) and run it directly using Python 3
Usage
Prerequisites:
Ensure you have Python 3.x installed.
Configuration (Optional):
The script comes with pre-defined keywords ("error", "exception"). To use a configuration file for keyword management:
Create a file named config.ini in the same directory as the script.
Add a section named KEYWORDS with each keyword on a separate line (e.g., [KEYWORDS]\nwarning=True\ncritical=True).
Alternatively, you can modify the script directly to update the keyword_counts dictionary.
Update Log File Path:
Open log-monitor.py in a text editor.
Locate the line LOG_FILE_PATH and replace /home/bharath/test_log_file.log with the actual path to your log file.
Run the Script:
Open a terminal window and navigate to the directory containing the script.
Run the script using the following command:
Bash
python log-monitor.py


Output
The script will continuously display new log entries in real-time.
When interrupted with Ctrl+C, it will generate and display a summary report showing the top occurring keywords and their counts.
Additional 
This script provides a foundation for log analysis. We can further customize for specific needs:
Advanced Filtering: Implement filtering based on log levels, patterns, or specific fields.
Alerting: Integrate email, SMS, or service APIs for notifications on critical errors.
Monitoring Integration: Explore sending data to monitoring dashboards for centralized logging.

