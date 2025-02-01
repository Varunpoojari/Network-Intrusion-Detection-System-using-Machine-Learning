# Network Intrusion Detection System (NIDS)

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-brightgreen.svg)
![Security](https://img.shields.io/badge/Security-Tools-red.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A sophisticated machine learning-based Network Intrusion Detection System (NIDS) that monitors and analyzes network traffic in real-time to detect potential security threats and anomalies.

## 🚀 Features

- **Real-time Network Monitoring**
  - Live packet capture and analysis
  - Traffic pattern recognition
  - Protocol-specific analysis (TCP, UDP, ICMP)

- **Machine Learning Integration**
  - Random Forest Classification
  - Real-time threat prediction
  - Confidence scoring for detections
  - Automated feature extraction

- **Attack Detection Capabilities**
  - DoS (Denial of Service) detection
  - Probe attack recognition
  - Privilege escalation attempts
  - Unauthorized access detection

- **Traffic Analysis**
  - Packet size analysis
  - Connection duration monitoring
  - Traffic rate calculation
  - Port scanning detection

## 📋 Prerequisites

- Python 3.9 or higher
- Root/Administrator privileges (for live capture)
- Network interface access
- Required Python packages (see requirements.txt)

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/network-ids.git
cd network-ids
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Simulation Mode
Run the system in simulation mode (no root privileges required):
```bash
python network_ids.py
```

### Live Monitoring Mode
Run with live network capture (requires root privileges):
```bash
sudo python live_network_ids.py
```

### Configuration Options
Modify the following parameters in the code:
- `n_samples`: Number of training samples
- `duration`: Monitoring duration
- Network interface selection
- Detection thresholds

## 📊 Project Structure

```
network-ids/
├── network_ids.py           # Main simulation implementation
├── live_network_ids.py      # Live monitoring implementation
├── requirements.txt         # Package dependencies
├── README.md               # Project documentation
└── .gitignore             # Git ignore rules
```

## 🛠️ Technical Details

### Machine Learning Model
- Algorithm: Random Forest Classifier
- Features:
  - Packet size
  - Connection duration
  - Protocol type
  - Port numbers
  - Traffic rates
  - Bytes per second

### Detection Capabilities
- Normal Traffic: 80% baseline
- DoS Attacks: 10% detection
- Probe Attacks: 5% detection
- Privilege Escalation: 3% detection
- Access Violations: 2% detection

## 📝 Sample Output

```
Monitoring network traffic...
Packet 1: ✅ Normal Traffic (Confidence: 95.23%)
Packet 2: 🚨 ATTACK DETECTED! (Confidence: 87.65%)
Protocol: TCP, Size: 1024 bytes
Source: 192.168.1.100:45678 → Destination: 10.0.0.1:80
```

## 🔐 Security Notes

- Requires root privileges for packet capture
- Does not store sensitive network data
- Configurable alert thresholds
- Real-time threat response

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch:
```bash
git checkout -b feature/your-feature-name
```
3. Commit your changes:
```bash
git commit -m "Add some feature"
```
4. Push to the branch:
```bash
git push origin feature/your-feature-name
```
5. Open a pull request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Future Enhancements

- [ ] Deep packet inspection
- [ ] Advanced anomaly detection
- [ ] GUI interface
- [ ] Alert logging system
- [ ] Report generation
- [ ] API integration
- [ ] Custom rule creation

## ⚠️ Disclaimer

This tool is for educational and testing purposes only. Users are responsible for complying with applicable laws and regulations regarding network monitoring and security testing.

## 📧 Contact



Project Link: [https://github.com/Varunpoojari/network-ids](https://github.com/Varunpoojari/network-ids)

## 🙏 Acknowledgments

- scikit-learn team
- Python Security community
- Network Security researchers
