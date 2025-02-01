# API Documentation

## Core Classes

### NetworkIDS

The main class for intrusion detection functionality.

#### Methods

```python
class NetworkIDS:
    def __init__(self):
        """Initialize the Network Intrusion Detection System"""
        
    def generate_sample_data(self, n_samples=1000):
        """Generate sample network traffic data
        
        Args:
            n_samples (int): Number of samples to generate
            
        Returns:
            pandas.DataFrame: Generated traffic data
        """
        
    def preprocess_data(self, df):
        """Preprocess the network traffic data
        
        Args:
            df (pandas.DataFrame): Raw network traffic data
            
        Returns:
            tuple: (X, y) preprocessed features and labels
        """
        
    def train(self, X, y):
        """Train the model
        
        Args:
            X (numpy.ndarray): Training features
            y (numpy.ndarray): Training labels
        """
        
    def monitor_traffic(self, duration=10):
        """Monitor network traffic
        
        Args:
            duration (int): Monitoring duration in seconds
        """
```

### PacketAnalyzer

Utility class for analyzing network packets.

#### Methods

```python
class PacketAnalyzer:
    @staticmethod
    def calculate_packet_rate(packet_count, duration):
        """Calculate packet rate
        
        Args:
            packet_count (int): Number of packets
            duration (float): Time duration
            
        Returns:
            float: Packets per second
        """
        
    @staticmethod
    def detect_port_scan(port_attempts, threshold):
        """Detect potential port scanning
        
        Args:
            port_attempts (list): List of attempted ports
            threshold (int): Detection threshold
            
        Returns:
            bool: True if port scan detected
        """
```

### AlertManager

Manages system alerts and notifications.

#### Methods

```python
class AlertManager:
    def __init__(self, logger):
        """Initialize AlertManager
        
        Args:
            logger: Logging instance
        """
        
    def generate_alert(self, alert_type, details):
        """Generate security alert
        
        Args:
            alert_type (str): Type of alert
            details (dict): Alert details
            
        Returns:
            dict: Formatted alert
        """
```

## Configuration

### Available Settings

```python
# Network interface settings
NETWORK_INTERFACE: str  # Network interface to monitor
CAPTURE_TIMEOUT: int   # Packet capture timeout

# Model parameters
MODEL_PARAMS: dict    # Machine learning model parameters

# Training parameters
TRAINING_PARAMS: dict  # Model training parameters

# Alert thresholds
ALERT_THRESHOLDS: dict  # Detection thresholds

# Logging configuration
LOG_CONFIG: dict  # Logging settings
```

## Utility Functions

### Logging

```python
def setup_logging(config):
    """Set up logging configuration
    
    Args:
        config (dict): Logging configuration
        
    Returns:
        logger: Configured logger instance
    """
```

### Alert Management

```python
def save_alert(alert_data, filename='alerts.json'):
    """Save alert data to JSON file
    
    Args:
        alert_data (dict): Alert information
        filename (str): Output file name
    """
```

## Examples

### Basic Implementation

```python
from network_ids import NetworkIDS
from utils import setup_logging, AlertManager

# Initialize
ids = NetworkIDS()
logger = setup_logging(LOG_CONFIG)
alert_manager = AlertManager(logger)

# Train model
df = ids.generate_sample_data()
X, y = ids.preprocess_data(df)
ids.train(X, y)

# Start monitoring
ids.monitor_traffic(duration=3600)
```

### Custom Alert Handling

```python
def custom_alert_handler(alert):
    # Custom alert processing
    print(f"Alert detected: {alert['type']}")
    save_alert(alert)

# Set custom handler
ids.set_alert_handler(custom_alert_handler)
```
