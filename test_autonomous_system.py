#!/usr/bin/env python3
"""
Simple Test Suite for Autonomous Evolution System

Validates core functionality of all system modules.
"""

import os
import sys
import json
import unittest

# Add gpt directory to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gpt'))

from quantum_x_integration import QuantumXIntegration
from self_diagnosis import SelfDiagnosisSystem
from self_fixing_healing import SelfFixingSystem, SelfHealingSystem
from self_cleaning_maintaining import SelfCleaningSystem, SelfMaintainingSystem
from auto_recommendation import AutoRecommendationSystem
from autonomous_scheduler import AutonomousScheduler


class TestAutonomousEvolutionSystem(unittest.TestCase):
    """Test suite for the autonomous evolution system."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_code_path = os.path.join(os.path.dirname(__file__), 'gpt')
    
    def test_quantum_x_integration_init(self):
        """Test Quantum-X integration initialization."""
        integration = QuantumXIntegration()
        self.assertIsNotNone(integration)
        self.assertIsNotNone(integration.quantum_x_repo_url)
        
        status = integration.get_integration_status()
        self.assertIn('repository_url', status)
        print("✓ Quantum-X Integration: PASSED")
    
    def test_self_diagnosis_init(self):
        """Test self-diagnosis system initialization."""
        diagnosis = SelfDiagnosisSystem()
        self.assertIsNotNone(diagnosis)
        
        # Test resource check
        resources = diagnosis.check_system_resources()
        self.assertIn('cpu_percent', resources)
        self.assertIn('memory_percent', resources)
        print("✓ Self-Diagnosis System: PASSED")
    
    def test_self_fixing_system(self):
        """Test self-fixing system."""
        fixer = SelfFixingSystem()
        self.assertIsNotNone(fixer)
        self.assertTrue(fixer.auto_fix_enabled)
        print("✓ Self-Fixing System: PASSED")
    
    def test_self_healing_system(self):
        """Test self-healing system."""
        healer = SelfHealingSystem()
        self.assertIsNotNone(healer)
        
        # Test recovery
        test_error = {"error": "test error", "timestamp": "2026-01-01"}
        result = healer.recover_from_crash(test_error)
        self.assertTrue(result['success'])
        print("✓ Self-Healing System: PASSED")
    
    def test_self_cleaning_system(self):
        """Test self-cleaning system."""
        cleaner = SelfCleaningSystem()
        self.assertIsNotNone(cleaner)
        
        # Test duplicate detection
        result = cleaner.remove_duplicate_code(self.test_code_path)
        self.assertTrue(result['success'])
        print("✓ Self-Cleaning System: PASSED")
    
    def test_self_maintaining_system(self):
        """Test self-maintaining system."""
        maintainer = SelfMaintainingSystem()
        self.assertIsNotNone(maintainer)
        
        # Test security scan
        result = maintainer.perform_security_scan(self.test_code_path)
        self.assertTrue(result['success'])
        print("✓ Self-Maintaining System: PASSED")
    
    def test_auto_recommendation_system(self):
        """Test auto-recommendation system."""
        recommender = AutoRecommendationSystem()
        self.assertIsNotNone(recommender)
        
        # Test recommendation generation
        test_metrics = {
            "cpu_percent": 95,
            "memory_percent": 88,
            "python_files": 10,
            "missing_docstrings": 5
        }
        
        recommendations = recommender.analyze_metrics_for_recommendations(test_metrics)
        self.assertIsInstance(recommendations, list)
        print("✓ Auto-Recommendation System: PASSED")
    
    def test_autonomous_scheduler(self):
        """Test autonomous scheduler."""
        scheduler = AutonomousScheduler()
        self.assertIsNotNone(scheduler)
        
        # Test task scheduling
        def dummy_task():
            return {"status": "completed"}
        
        result = scheduler.schedule_daily_task("test_task", dummy_task, "12:00")
        self.assertTrue(result['success'])
        
        status = scheduler.get_status()
        self.assertFalse(status['running'])  # Not started yet
        print("✓ Autonomous Scheduler: PASSED")
    
    def test_system_integration(self):
        """Test that all systems can work together."""
        # Initialize systems
        diagnosis = SelfDiagnosisSystem()
        recommender = AutoRecommendationSystem()
        
        # Run diagnosis
        diagnosis_result = diagnosis.run_comprehensive_diagnosis(self.test_code_path)
        self.assertIn('timestamp', diagnosis_result)
        
        # Generate recommendations based on diagnosis
        strategy = recommender.generate_evolutionary_strategy(
            diagnosis_result,
            {"metrics": {"total_files": 10}}
        )
        
        self.assertIn('total_recommendations', strategy)
        print("✓ System Integration: PASSED")


def run_tests():
    """Run all tests and display results."""
    print("\n" + "=" * 80)
    print("AUTONOMOUS EVOLUTION SYSTEM - TEST SUITE")
    print("=" * 80 + "\n")
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestAutonomousEvolutionSystem)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 80)
    print("TEST RESULTS SUMMARY")
    print("=" * 80)
    print(f"Tests Run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 80 + "\n")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
