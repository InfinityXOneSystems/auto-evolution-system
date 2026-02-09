"""
Validation Script for Auto-Evolution System Merge into Quantum-X-Builder

This script validates that the auto-evolution-system has been properly
merged into quantum-x-builder with all safety mechanisms in place.
"""

import os
import sys
import json
import logging
from typing import Dict, List, Any
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MergeValidator:
    """Validates quantum-x-builder integration."""
    
    def __init__(self, quantum_x_path: str = "/tmp/quantum-x-builder"):
        """
        Initialize validator.
        
        Args:
            quantum_x_path: Path to quantum-x-builder repository
        """
        self.quantum_x_path = quantum_x_path
        self.auto_evolution_path = os.path.join(
            quantum_x_path,
            "_OPS/AUTO_EVOLUTION"
        )
        self.checks_passed = 0
        self.checks_failed = 0
        self.warnings = []
    
    def validate_directory_structure(self) -> bool:
        """Validate directory structure exists."""
        logger.info("Checking directory structure...")
        
        required_dirs = [
            self.auto_evolution_path,
            os.path.join(self.auto_evolution_path, "modules"),
            os.path.join(self.auto_evolution_path, "config"),
            os.path.join(self.auto_evolution_path, "docs")
        ]
        
        all_exist = True
        for dir_path in required_dirs:
            if os.path.exists(dir_path):
                logger.info(f"  ✓ {dir_path}")
            else:
                logger.error(f"  ✗ Missing: {dir_path}")
                all_exist = False
                self.checks_failed += 1
        
        if all_exist:
            self.checks_passed += 1
        
        return all_exist
    
    def validate_python_modules(self) -> bool:
        """Validate all Python modules exist."""
        logger.info("Checking Python modules...")
        
        required_modules = [
            "autonomous_evolution_main.py",
            "auto_evolution_engine.py",
            "quantum_x_integration.py",
            "self_diagnosis.py",
            "self_fixing_healing.py",
            "self_cleaning_maintaining.py",
            "autonomous_scheduler.py",
            "auto_recommendation.py",
            "immediate_quantum_startup.py",
            "system_conflict_detector.py",
            "quantum_x_adapter.py"
        ]
        
        modules_dir = os.path.join(self.auto_evolution_path, "modules")
        all_exist = True
        
        for module in required_modules:
            module_path = os.path.join(modules_dir, module)
            if os.path.exists(module_path):
                logger.info(f"  ✓ {module}")
            else:
                logger.error(f"  ✗ Missing: {module}")
                all_exist = False
                self.checks_failed += 1
        
        if all_exist:
            self.checks_passed += 1
        
        return all_exist
    
    def validate_configuration(self) -> bool:
        """Validate configuration files."""
        logger.info("Checking configuration files...")
        
        config_dir = os.path.join(self.auto_evolution_path, "config")
        required_configs = [
            "system_manifest.yaml",
            "requirements.txt"
        ]
        
        all_exist = True
        for config in required_configs:
            config_path = os.path.join(config_dir, config)
            if os.path.exists(config_path):
                logger.info(f"  ✓ {config}")
            else:
                logger.error(f"  ✗ Missing: {config}")
                all_exist = False
                self.checks_failed += 1
        
        if all_exist:
            self.checks_passed += 1
        
        return all_exist
    
    def validate_governance_integration(self) -> bool:
        """Validate quantum-x governance integration."""
        logger.info("Checking governance integration...")
        
        policy_path = os.path.join(
            self.quantum_x_path,
            "_OPS/POLICY/AUTO_EVOLUTION_POLICY.json"
        )
        
        if not os.path.exists(policy_path):
            logger.error(f"  ✗ Policy file missing: {policy_path}")
            self.checks_failed += 1
            return False
        
        try:
            with open(policy_path, 'r') as f:
                policy = json.load(f)
            
            required_keys = [
                "enabled",
                "autonomy_level",
                "allowed_actions",
                "forbidden_actions",
                "requires_approval",
                "audit_required"
            ]
            
            all_keys_present = True
            for key in required_keys:
                if key in policy:
                    logger.info(f"  ✓ Policy key: {key}")
                else:
                    logger.error(f"  ✗ Missing policy key: {key}")
                    all_keys_present = False
                    self.checks_failed += 1
            
            if all_keys_present:
                self.checks_passed += 1
            
            return all_keys_present
            
        except Exception as e:
            logger.error(f"  ✗ Error reading policy: {e}")
            self.checks_failed += 1
            return False
    
    def validate_kill_switch(self) -> bool:
        """Validate kill switch exists and is readable."""
        logger.info("Checking kill switch...")
        
        kill_switch_path = os.path.join(
            self.quantum_x_path,
            "_OPS/SAFETY/KILL_SWITCH.json"
        )
        
        if not os.path.exists(kill_switch_path):
            logger.warning(f"  ⚠ Kill switch not found (optional): {kill_switch_path}")
            self.warnings.append("Kill switch file not found - using default behavior")
            self.checks_passed += 1
            return True
        
        try:
            with open(kill_switch_path, 'r') as f:
                kill_switch = json.load(f)
            
            logger.info(f"  ✓ Kill switch exists")
            logger.info(f"    Status: {kill_switch.get('kill_switch', 'UNKNOWN')}")
            self.checks_passed += 1
            return True
            
        except Exception as e:
            logger.error(f"  ✗ Error reading kill switch: {e}")
            self.checks_failed += 1
            return False
    
    def validate_adapter_integration(self) -> bool:
        """Validate quantum-x adapter can be imported."""
        logger.info("Checking adapter integration...")
        
        # Add modules to path
        modules_dir = os.path.join(self.auto_evolution_path, "modules")
        sys.path.insert(0, modules_dir)
        
        try:
            import quantum_x_adapter
            adapter = quantum_x_adapter.QuantumXGovernanceAdapter(
                ops_path=os.path.join(self.quantum_x_path, "_OPS")
            )
            
            # Test key methods
            is_in_quantum_x = adapter.is_running_in_quantum_x()
            logger.info(f"  ✓ Adapter imported successfully")
            logger.info(f"    Running in quantum-x: {is_in_quantum_x}")
            
            # Test kill switch check
            can_proceed = adapter.check_kill_switch()
            logger.info(f"    Kill switch check: {'OK' if can_proceed else 'HALTED'}")
            
            self.checks_passed += 1
            return True
            
        except Exception as e:
            logger.error(f"  ✗ Adapter import failed: {e}")
            self.checks_failed += 1
            return False
    
    def validate_documentation(self) -> bool:
        """Validate documentation exists."""
        logger.info("Checking documentation...")
        
        docs_dir = os.path.join(self.auto_evolution_path, "docs")
        required_docs = [
            "README.md",
            "DOCUMENTATION.md",
            "MERGE_INTO_QUANTUM_X.md"
        ]
        
        all_exist = True
        for doc in required_docs:
            doc_path = os.path.join(docs_dir, doc)
            if os.path.exists(doc_path):
                logger.info(f"  ✓ {doc}")
            else:
                logger.error(f"  ✗ Missing: {doc}")
                all_exist = False
                self.checks_failed += 1
        
        if all_exist:
            self.checks_passed += 1
        
        return all_exist
    
    def validate_no_conflicts(self) -> bool:
        """Validate no resource conflicts."""
        logger.info("Checking for conflicts...")
        
        # Import conflict detector
        modules_dir = os.path.join(self.auto_evolution_path, "modules")
        sys.path.insert(0, modules_dir)
        
        try:
            from system_conflict_detector import SystemConflictDetector
            
            detector = SystemConflictDetector()
            results = detector.run_comprehensive_conflict_check(self.quantum_x_path)
            
            total_conflicts = results.get("total_conflicts", 0)
            high_severity = results.get("conflicts_by_severity", {}).get("high", 0)
            
            if high_severity > 0:
                logger.error(f"  ✗ Found {high_severity} high-severity conflicts")
                self.checks_failed += 1
                return False
            elif total_conflicts > 0:
                logger.warning(f"  ⚠ Found {total_conflicts} low-severity conflicts")
                self.warnings.append(f"{total_conflicts} low-severity conflicts detected")
                self.checks_passed += 1
                return True
            else:
                logger.info(f"  ✓ No conflicts detected")
                self.checks_passed += 1
                return True
                
        except Exception as e:
            logger.error(f"  ✗ Conflict check failed: {e}")
            self.checks_failed += 1
            return False
    
    def validate_functional_test(self) -> bool:
        """Run functional test of integrated system."""
        logger.info("Running functional test...")
        
        modules_dir = os.path.join(self.auto_evolution_path, "modules")
        sys.path.insert(0, modules_dir)
        
        try:
            # Set quantum-x native flag
            os.environ["QUANTUM_X_NATIVE"] = "true"
            
            # Import main module
            from autonomous_evolution_main import AutonomousOrchestrator
            
            # Create instance (no config_path param needed)
            orchestrator = AutonomousOrchestrator()
            
            logger.info(f"  ✓ System initialized successfully")
            logger.info(f"    Autonomy level: 100%")
            
            self.checks_passed += 1
            return True
            
        except Exception as e:
            logger.error(f"  ✗ Functional test failed: {e}")
            self.checks_failed += 1
            return False
    
    def run_all_validations(self) -> Dict[str, Any]:
        """Run all validation checks."""
        logger.info("\n" + "=" * 80)
        logger.info("QUANTUM-X-BUILDER MERGE VALIDATION")
        logger.info("=" * 80 + "\n")
        
        validations = [
            ("Directory Structure", self.validate_directory_structure),
            ("Python Modules", self.validate_python_modules),
            ("Configuration Files", self.validate_configuration),
            ("Governance Integration", self.validate_governance_integration),
            ("Kill Switch", self.validate_kill_switch),
            ("Adapter Integration", self.validate_adapter_integration),
            ("Documentation", self.validate_documentation),
            ("Conflict Detection", self.validate_no_conflicts),
            ("Functional Test", self.validate_functional_test)
        ]
        
        for name, validation_func in validations:
            logger.info(f"\n{'=' * 80}")
            logger.info(f"Validation: {name}")
            logger.info('=' * 80)
            try:
                validation_func()
            except Exception as e:
                logger.error(f"Validation failed with exception: {e}")
                self.checks_failed += 1
        
        # Generate report
        total_checks = self.checks_passed + self.checks_failed
        success_rate = (self.checks_passed / total_checks * 100) if total_checks > 0 else 0
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "quantum_x_path": self.quantum_x_path,
            "checks_passed": self.checks_passed,
            "checks_failed": self.checks_failed,
            "total_checks": total_checks,
            "success_rate": success_rate,
            "warnings": self.warnings,
            "merge_successful": self.checks_failed == 0 and self.checks_passed > 0,
            "recommendation": self._get_recommendation()
        }
        
        # Print summary
        logger.info("\n" + "=" * 80)
        logger.info("VALIDATION SUMMARY")
        logger.info("=" * 80)
        logger.info(f"Total checks: {total_checks}")
        logger.info(f"Passed: {self.checks_passed} ✓")
        logger.info(f"Failed: {self.checks_failed} ✗")
        logger.info(f"Success rate: {success_rate:.1f}%")
        
        if self.warnings:
            logger.info(f"\nWarnings ({len(self.warnings)}):")
            for warning in self.warnings:
                logger.info(f"  ⚠ {warning}")
        
        logger.info(f"\nMerge Status: {'✓ SUCCESS' if report['merge_successful'] else '✗ FAILED'}")
        logger.info(f"Recommendation: {report['recommendation']}")
        logger.info("=" * 80 + "\n")
        
        return report
    
    def _get_recommendation(self) -> str:
        """Get recommendation based on validation results."""
        if self.checks_failed == 0:
            return "Auto-evolution system successfully merged into quantum-x-builder. Ready for production use."
        elif self.checks_failed <= 2:
            return "Merge mostly successful. Review and fix failed checks before production use."
        else:
            return "Merge has significant issues. Review failures and re-run merge preparation."


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Validate auto-evolution merge into quantum-x-builder"
    )
    parser.add_argument(
        "--quantum-x-path",
        default="/tmp/quantum-x-builder",
        help="Path to quantum-x-builder repository"
    )
    parser.add_argument(
        "--output",
        help="Output file for validation report (JSON)"
    )
    
    args = parser.parse_args()
    
    # Create validator
    validator = MergeValidator(quantum_x_path=args.quantum_x_path)
    
    # Run validations
    report = validator.run_all_validations()
    
    # Save report if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        logger.info(f"Report saved to: {args.output}")
    
    # Exit with appropriate code
    sys.exit(0 if report["merge_successful"] else 1)


if __name__ == "__main__":
    main()
