# utils.py
"""Utility functions for the NIDS"""

import logging
from logging.handlers import RotatingFileHandler
import json
import time
from datetime import datetime

def setup_logging(config):
    """Set up logging configuration"""
    logger = logging.getLogger('NIDS')
    logger.setLevel(logging.INFO)

    # Create handlers
    file_handler = RotatingFileHandler(
        config['log_file'],
        maxBytes=10000000,
        backupCount=5
    )
    console_handler = logging.StreamHandler()

    # Create formatters and add it to handlers
    formatter = logging.Formatter(config['log_format'])
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def save_alert(alert_data, filename='alerts.json'):
    """Save alert data to JSON file"""
    try:
        with open(filename, 'r') as f:
            alerts = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        alerts = []

    alert_data['timestamp'] = datetime.now().isoformat()
    alerts.append(alert_data)

    with open(filename, 'w') as f:
        json.dump(alerts, f, indent=4)

class PacketAnalyzer:
    """Analyze network packets for specific patterns"""

    @staticmethod
    def calculate_packet_rate(packet_count, duration):
        """Calculate packet rate"""
        return packet_count / duration if duration > 0 else 0

    @staticmethod
    def detect_port_scan(port_attempts, threshold):
        """Detect potential port scanning"""
        return len(port_attempts) > threshold

    @staticmethod
    def analyze_payload(payload):
        """Analyze packet payload for suspicious patterns"""
        suspicious_patterns = [
            'eval(',
            'exec(',
            '<script>',
            'union select',
            'drop table'
        ]
        return any(pattern in payload.lower() for pattern in suspicious_patterns)

class AlertManager:
    """Manage and format security alerts"""

    def __init__(self, logger):
        self.logger = logger

    def generate_alert(self, alert_type, details):
        """Generate formatted security alert"""
        alert = {
            'type': alert_type,
            'timestamp': time.time(),
            'details': details
        }
        self.logger.warning(f"Security Alert: {alert_type}")
        save_alert(alert)
        return alert

    def check_threshold(self, value, threshold):
        """Check if value exceeds threshold"""
        return value > threshold
