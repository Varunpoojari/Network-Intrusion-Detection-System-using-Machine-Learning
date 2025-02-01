# config.py
"""Configuration settings for the NIDS"""

# Network interface settings
NETWORK_INTERFACE = "en0"  # Change according to your system
CAPTURE_TIMEOUT = 120  # Seconds

# Model parameters
MODEL_PARAMS = {
    'n_estimators': 100,
    'random_state': 42,
    'n_jobs': -1
}

# Training parameters
TRAINING_PARAMS = {
    'test_size': 0.2,
    'random_state': 42
}

# Alert thresholds
ALERT_THRESHOLDS = {
    'confidence_threshold': 0.8,
    'port_scan_threshold': 100,
    'dos_packet_threshold': 1000
}

# Logging configuration
LOG_CONFIG = {
    'log_file': 'nids.log',
    'log_level': 'INFO',
    'log_format': '%(asctime)s - %(levelname)s - %(message)s'
}

# Feature settings
FEATURES = [
    'packet_size',
    'connection_duration',
    'protocol',
    'port',
    'packets_per_second',
    'bytes_per_second'
]

# Attack types
ATTACK_TYPES = {
    'normal': 0.8,
    'dos': 0.1,
    'probe': 0.05,
    'privilege': 0.03,
    'access': 0.02
}
