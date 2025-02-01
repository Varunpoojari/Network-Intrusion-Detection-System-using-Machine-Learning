# test_nids.py
"""Unit tests for the NIDS"""

import unittest
import pandas as pd
import numpy as np
from network_ids import NetworkIDS
from utils import PacketAnalyzer, AlertManager
import logging

class TestNetworkIDS(unittest.TestCase):
    """Test cases for NetworkIDS class"""

    def setUp(self):
        """Set up test environment"""
        self.ids = NetworkIDS()
        self.logger = logging.getLogger('test_logger')

    def test_data_generation(self):
        """Test sample data generation"""
        df = self.ids.generate_sample_data(n_samples=100)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 100)
        self.assertTrue('packet_size' in df.columns)
        self.assertTrue('protocol' in df.columns)

    def test_preprocessing(self):
        """Test data preprocessing"""
        df = self.ids.generate_sample_data(n_samples=100)
        X, y = self.ids.preprocess_data(df)
        self.assertEqual(X.shape[0], 100)
        self.assertTrue(isinstance(y, pd.Series))

    def test_model_training(self):
        """Test model training"""
        df = self.ids.generate_sample_data(n_samples=100)
        X, y = self.ids.preprocess_data(df)
        self.ids.train(X, y)
        self.assertIsNotNone(self.ids.model)

class TestPacketAnalyzer(unittest.TestCase):
    """Test cases for PacketAnalyzer class"""

    def setUp(self):
        """Set up test environment"""
        self.analyzer = PacketAnalyzer()

    def test_packet_rate(self):
        """Test packet rate calculation"""
        rate = self.analyzer.calculate_packet_rate(100, 10)
        self.assertEqual(rate, 10.0)

    def test_port_scan_detection(self):
        """Test port scan detection"""
        ports = list(range(100))
        result = self.analyzer.detect_port_scan(ports, 50)
        self.assertTrue(result)

class TestAlertManager(unittest.TestCase):
    """Test cases for AlertManager class"""

    def setUp(self):
        """Set up test environment"""
        self.logger = logging.getLogger('test_logger')
        self.alert_manager = AlertManager(self.logger)

    def test_alert_generation(self):
        """Test alert generation"""
        alert = self.alert_manager.generate_alert(
            'test_alert',
            {'source': '192.168.1.1', 'destination': '192.168.1.2'}
        )
        self.assertEqual(alert['type'], 'test_alert')
        self.assertTrue('timestamp' in alert)

    def test_threshold_check(self):
        """Test threshold checking"""
        result = self.alert_manager.check_threshold(100, 50)
        self.assertTrue(result)
        result = self.alert_manager.check_threshold(25, 50)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
