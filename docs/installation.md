# Installation Guide

## Prerequisites

Before installing the Network Intrusion Detection System, ensure you have:

- Python 3.9 or higher
- pip (Python package manager)
- Git (for cloning the repository)
- Root/Administrator privileges (for live packet capture)

## Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/your-username/network-ids.git
cd network-ids
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

1. Basic Configuration:
   - Open `network_ids/config.py`
   - Update `NETWORK_INTERFACE` to match your system
   - Adjust alert thresholds if needed

2. Optional: Environment-specific settings
   - Copy `.env.example` to `.env`
   - Update variables as needed

## Verification

Test your installation:
```bash
python -m pytest tests/
```

## Troubleshooting

Common issues and solutions:

1. Permission Errors
   - Ensure proper privileges for packet capture
   - Run with sudo/administrator rights

2. Package Installation Issues
   - Update pip: `python -m pip install --upgrade pip`
   - Install system dependencies if needed

3. Network Interface Problems
   - List available interfaces: `python -c "from scapy.all import show_interfaces; show_interfaces()"`
   - Update config.py with correct interface name
