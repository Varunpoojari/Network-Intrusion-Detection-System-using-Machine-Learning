# Usage Guide

## Basic Usage

### Simulation Mode

Run the system with simulated data:
```bash
python network_ids/network_ids.py
```

### Live Monitoring

Monitor live network traffic:
```bash
sudo python network_ids/live_network_ids.py
```

## Features and Options

### 1. Traffic Analysis
- Packet size monitoring
- Protocol analysis
- Port scanning detection
- Traffic rate calculation

### 2. Attack Detection
- DoS (Denial of Service)
- Port scanning
- Privilege escalation
- Unauthorized access

### 3. Alerting System
- Real-time alerts
- Confidence scoring
- Alert logging
- Email notifications (optional)

## Configuration Options

### Alert Thresholds

Modify in `config.py`:
```python
ALERT_THRESHOLDS = {
    'confidence_threshold': 0.8,
    'port_scan_threshold': 100,
    'dos_packet_threshold': 1000
}
```

### Logging Settings

```python
LOG_CONFIG = {
    'log_file': 'nids.log',
    'log_level': 'INFO',
    'log_format': '%(asctime)s - %(levelname)s - %(message)s'
}
```

## Example Use Cases

### 1. Basic Network Monitoring
```python
from network_ids import NetworkIDS

ids = NetworkIDS()
ids.monitor_traffic(duration=3600)  # Monitor for 1 hour
```

### 2. Custom Alert Handling
```python
from network_ids import NetworkIDS
from utils import AlertManager

ids = NetworkIDS()
alert_manager = AlertManager()

def custom_alert_handler(alert):
    print(f"Alert: {alert['type']} - Confidence: {alert['confidence']}%")

ids.set_alert_handler(custom_alert_handler)
ids.monitor_traffic()
```

### 3. Analyzing Specific Protocols
```python
ids.monitor_traffic(protocols=['TCP', 'UDP'])
```

## Best Practices

1. Regular Updates
   - Keep the system updated
   - Regularly retrain the model
   - Update attack signatures

2. Performance Optimization
   - Adjust packet capture settings
   - Optimize alert thresholds
   - Monitor system resources

3. Security Considerations
   - Regular security audits
   - Access control implementation
   - Secure data handling
