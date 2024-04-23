import subprocess
import signal
import logging
import time
import random
from collections import Counter

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Specify the path to the log file to monitor
LOG_FILE_PATH="/path/to/your/log/file.log"


# Initialize dictionary to store keyword counts
keyword_counts = {"error": 0, "exception": 0}

# Threshold for sending alerts
ALERT_THRESHOLD = 3

def monitor_log_file(log_file_path):
    tail_process = subprocess.Popen(['tail', '-F', log_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        for line in iter(tail_process.stdout.readline, b''):
            # Process the log line here (e.g., analyze or print it)
            logger.info(line.decode().strip())

            # Analyze log line for keywords
            for keyword in keyword_counts.keys():
                if keyword in line.decode().lower():
                    logger.debug(f"Keyword '{keyword}' found in log: {line.strip()}")
                    # Count occurrences of keywords
                    count_keywords(keyword)

                    # Send alerts if count exceeds threshold
                    if keyword_counts[keyword] >= ALERT_THRESHOLD:
                        send_alerts(keyword)

    except KeyboardInterrupt:
        print("\nLog monitoring stopped.")
        tail_process.send_signal(signal.SIGINT)
        tail_process.wait()
        generate_summary_report()  # Generate summary report before exiting

def count_keywords(keyword):
    global keyword_counts
    keyword_counts[keyword] += 1
    logger.debug(f"Keyword '{keyword}' count: {keyword_counts[keyword]}")

def generate_summary_report():
    logger.info("Top occurring keywords:")
    for keyword, count in keyword_counts.items():
        logger.info(f"{keyword}: {count}")

def send_alerts(keyword):
    # Placeholder for sending alerts
    logger.info(f"Alert: '{keyword}' occurred {keyword_counts[keyword]} times. Sending alerts...")

def log_messages():
    formats = {
        logging.INFO: "INFO message",
        logging.DEBUG: "DEBUG message",
        logging.ERROR: "ERROR message"
    }
    log_levels = [logging.INFO, logging.DEBUG, logging.ERROR]

    try:
        while True:
            log_level = random.choice(log_levels)
            log_message = formats[log_level]
            logger.log(log_level, log_message)
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Logging interrupted. Exiting.")
        generate_summary_report()  # Generate summary report before exiting

if __name__ == "__main__":
    # Start monitoring the log file in a separate thread
    subprocess.Popen(['tail', '-F', LOG_FILE_PATH])

    # Start logging messages internally
    log_messages()

