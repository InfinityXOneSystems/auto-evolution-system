"""
Merge Preparation Module for Quantum-X-Builder Integration

This module prepares the auto-evolution-system for safe and intelligent
merging into the quantum-x-builder repository.
"""

import os
import sys
import json
import shutil
import logging
from typing import Dict, List, Any
from datetime import datetime
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MergePreparation:
    """
    Prepares auto-evolution-system for merging into quantum-x-builder.
    """
    
    def __init__(
        self, 
        auto_evolution_root: str = None,
        quantum_x_path: str = "/tmp/quantum-x-builder",
        output_dir: str = "/tmp/merge-preparation"
    ):
        """
        Initialize merge preparation.
        
        Args:
            auto_evolution_root: Root path of auto-evolution-system
            quantum_x_path: Path to quantum-x-builder repository
            output_dir: Directory for merge preparation output
        """
        self.auto_evolution_root = auto_evolution_root or os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
        self.quantum_x_path = quantum_x_path
        self.output_dir = output_dir
        
        # Files to merge
        self.python_modules = [
            "autonomous_evolution_main.py",
            "auto_evolution_engine.py",
            "quantum_x_integration.py",
            "self_diagnosis.py",
            "self_fixing_healing.py",
            "self_cleaning_maintaining.py",
            "autonomous_scheduler.py",
            "auto_recommendation.py",
            "immediate_quantum_startup.py",
            "system_conflict_detector.py"
        ]
        
        self.config_files = [
            "system_manifest.yaml",
            "requirements.txt"
        ]
        
        self.doc_files = [
            "README.md",
            "DOCUMENTATION.md",
            "QUANTUM_INTEGRATION.md",
            "QUICKSTART.md",
            "MERGE_INTO_QUANTUM_X.md"
        ]
        
        logger.info(f"MergePreparation initialized")
        logger.info(f"  Auto-Evolution Root: {self.auto_evolution_root}")
        logger.info(f"  Quantum-X Path: {self.quantum_x_path}")
        logger.info(f"  Output Directory: {self.output_dir}")
    
    def analyze_quantum_x_structure(self) -> Dict[str, Any]:
        """
        Analyze quantum-x-builder repository structure.
        
        Returns:
            Dict with structure analysis
        """
        logger.info("Analyzing quantum-x-builder structure...")
        
        if not os.path.exists(self.quantum_x_path):
            return {
                "success": False,
                "error": f"Quantum-X path does not exist: {self.quantum_x_path}",
                "recommendation": "Run immediate_quantum_startup.py first"
            }
        
        analysis = {
            "success": True,
            "quantum_x_exists": True,
            "has_ops_directory": os.path.exists(os.path.join(self.quantum_x_path, "_OPS")),
            "has_backend": os.path.exists(os.path.join(self.quantum_x_path, "backend")),
            "has_frontend": os.path.exists(os.path.join(self.quantum_x_path, "frontend")),
            "has_autonomous_partner": False,
            "suggested_integration_path": None,
            "conflicts": []
        }
        
        # Check for existing autonomous components
        autonomous_paths = [
            "vizual-x/autonomous-partner",
            "frontend/src/autonomous-partner",
            "docs/auto-ops"
        ]
        
        for path in autonomous_paths:
            full_path = os.path.join(self.quantum_x_path, path)
            if os.path.exists(full_path):
                analysis["has_autonomous_partner"] = True
                analysis["existing_autonomous_paths"] = autonomous_paths
                break
        
        # Determine best integration path
        if analysis["has_ops_directory"]:
            analysis["suggested_integration_path"] = "_OPS/AUTO_EVOLUTION"
            analysis["integration_strategy"] = "ops_integration"
        elif analysis["has_backend"]:
            analysis["suggested_integration_path"] = "backend/autonomous-evolution"
            analysis["integration_strategy"] = "backend_integration"
        else:
            analysis["suggested_integration_path"] = "auto-evolution-system"
            analysis["integration_strategy"] = "standalone_directory"
        
        logger.info(f"✓ Analysis complete. Suggested path: {analysis['suggested_integration_path']}")
        return analysis
    
    def check_merge_conflicts(self) -> Dict[str, Any]:
        """
        Check for potential conflicts before merge.
        
        Returns:
            Dict with conflict analysis
        """
        logger.info("Checking for merge conflicts...")
        
        conflicts = {
            "path_conflicts": [],
            "file_conflicts": [],
            "module_conflicts": [],
            "configuration_conflicts": [],
            "severity": "none"
        }
        
        # Check if target paths exist in quantum-x
        analysis = self.analyze_quantum_x_structure()
        if not analysis["success"]:
            conflicts["severity"] = "critical"
            conflicts["error"] = analysis.get("error")
            return conflicts
        
        target_path = os.path.join(
            self.quantum_x_path,
            analysis["suggested_integration_path"]
        )
        
        if os.path.exists(target_path):
            conflicts["path_conflicts"].append({
                "type": "directory_exists",
                "path": target_path,
                "severity": "medium",
                "message": f"Target directory already exists: {target_path}",
                "resolution": "Use different path or merge contents carefully"
            })
            conflicts["severity"] = "medium"
        
        # Check for file name conflicts
        if os.path.exists(target_path):
            for module in self.python_modules:
                module_path = os.path.join(target_path, "modules", module)
                if os.path.exists(module_path):
                    conflicts["file_conflicts"].append({
                        "type": "file_exists",
                        "file": module,
                        "path": module_path,
                        "severity": "high",
                        "message": f"File already exists: {module}",
                        "resolution": "Backup existing file or skip if identical"
                    })
                    if conflicts["severity"] != "critical":
                        conflicts["severity"] = "high"
        
        # Check for governance conflicts
        policy_file = os.path.join(
            self.quantum_x_path,
            "_OPS/POLICY/AUTO_EVOLUTION_POLICY.json"
        )
        if os.path.exists(policy_file):
            conflicts["configuration_conflicts"].append({
                "type": "policy_exists",
                "file": policy_file,
                "severity": "low",
                "message": "Auto-evolution policy already exists",
                "resolution": "Merge policies or use existing"
            })
        
        total_conflicts = (
            len(conflicts["path_conflicts"]) +
            len(conflicts["file_conflicts"]) +
            len(conflicts["module_conflicts"]) +
            len(conflicts["configuration_conflicts"])
        )
        
        conflicts["total_conflicts"] = total_conflicts
        conflicts["can_proceed"] = conflicts["severity"] not in ["critical", "high"]
        
        logger.info(f"✓ Conflict check complete. Found {total_conflicts} potential conflicts")
        logger.info(f"  Severity: {conflicts['severity']}")
        logger.info(f"  Can proceed: {conflicts['can_proceed']}")
        
        return conflicts
    
    def prepare_merge_package(self) -> Dict[str, Any]:
        """
        Prepare a merge package with all necessary files.
        
        Returns:
            Dict with package preparation results
        """
        logger.info("Preparing merge package...")
        
        # Create output directory structure
        os.makedirs(self.output_dir, exist_ok=True)
        
        package = {
            "success": False,
            "package_path": self.output_dir,
            "files_copied": [],
            "errors": [],
            "timestamp": datetime.now().isoformat()
        }
        
        try:
            # Analyze target structure
            analysis = self.analyze_quantum_x_structure()
            if not analysis["success"]:
                package["errors"].append(analysis.get("error"))
                return package
            
            # Create directory structure
            modules_dir = os.path.join(self.output_dir, "modules")
            config_dir = os.path.join(self.output_dir, "config")
            docs_dir = os.path.join(self.output_dir, "docs")
            
            os.makedirs(modules_dir, exist_ok=True)
            os.makedirs(config_dir, exist_ok=True)
            os.makedirs(docs_dir, exist_ok=True)
            
            # Copy Python modules
            gpt_dir = os.path.join(self.auto_evolution_root, "gpt")
            for module in self.python_modules:
                src = os.path.join(gpt_dir, module)
                dst = os.path.join(modules_dir, module)
                if os.path.exists(src):
                    shutil.copy2(src, dst)
                    package["files_copied"].append(module)
                    logger.info(f"  ✓ Copied: {module}")
                else:
                    package["errors"].append(f"Module not found: {module}")
                    logger.warning(f"  ✗ Missing: {module}")
            
            # Copy configuration files
            for config in self.config_files:
                src = os.path.join(self.auto_evolution_root, config)
                dst = os.path.join(config_dir, config)
                if os.path.exists(src):
                    shutil.copy2(src, dst)
                    package["files_copied"].append(config)
                    logger.info(f"  ✓ Copied: {config}")
            
            # Copy documentation
            for doc in self.doc_files:
                src = os.path.join(self.auto_evolution_root, doc)
                dst = os.path.join(docs_dir, doc)
                if os.path.exists(src):
                    shutil.copy2(src, dst)
                    package["files_copied"].append(doc)
                    logger.info(f"  ✓ Copied: {doc}")
            
            # Create quantum-x adapter
            self._create_quantum_x_adapter(modules_dir)
            package["files_copied"].append("quantum_x_adapter.py")
            
            # Create integration manifest
            manifest = self._create_integration_manifest(analysis)
            manifest_path = os.path.join(self.output_dir, "integration_manifest.json")
            with open(manifest_path, 'w') as f:
                json.dump(manifest, f, indent=2)
            package["files_copied"].append("integration_manifest.json")
            
            # Create installation script
            self._create_installation_script(analysis)
            package["files_copied"].append("install_to_quantum_x.sh")
            
            package["success"] = True
            package["total_files"] = len(package["files_copied"])
            
            logger.info(f"✓ Merge package prepared successfully")
            logger.info(f"  Total files: {package['total_files']}")
            logger.info(f"  Package location: {self.output_dir}")
            
        except Exception as e:
            logger.error(f"Error preparing merge package: {e}")
            package["errors"].append(str(e))
        
        return package
    
    def _create_quantum_x_adapter(self, output_dir: str):
        """Create quantum-x governance adapter module."""
        adapter_code = '''"""
Quantum-X Governance Adapter for Auto-Evolution-System

This adapter ensures auto-evolution-system operates within
quantum-x-builder's PAT (Policy-Authority-Truth) governance model.
"""

import os
import json
import logging
from typing import Dict, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class QuantumXGovernanceAdapter:
    """Adapter for quantum-x governance integration."""
    
    def __init__(self, ops_path: str = None):
        """
        Initialize governance adapter.
        
        Args:
            ops_path: Path to _OPS directory (default: auto-detect)
        """
        self.ops_path = ops_path or self._detect_ops_path()
        self.kill_switch_path = os.path.join(self.ops_path, "SAFETY/KILL_SWITCH.json")
        self.policy_path = os.path.join(self.ops_path, "POLICY/AUTO_EVOLUTION_POLICY.json")
        self.audit_path = os.path.join(self.ops_path, "AUDIT")
        
        logger.info(f"QuantumXGovernanceAdapter initialized with ops_path: {self.ops_path}")
    
    def _detect_ops_path(self) -> str:
        """Auto-detect _OPS directory path."""
        # Try common locations
        possible_paths = [
            "/_OPS",
            "../_OPS",
            "../../_OPS",
            os.path.expanduser("~/quantum-x-builder/_OPS")
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                return path
        
        # Default fallback
        return "/_OPS"
    
    def is_running_in_quantum_x(self) -> bool:
        """
        Detect if running inside quantum-x-builder.
        
        Returns:
            True if running in quantum-x environment
        """
        # Check for quantum-x environment variable
        if os.getenv("QUANTUM_X_NATIVE") == "true":
            return True
        
        # Check for _OPS directory
        if os.path.exists(self.ops_path):
            return True
        
        # Check for quantum-x markers
        markers = [
            "SYSTEM_INTEGRATION_MANIFEST.json",
            "backend/package.json",
            "frontend/package.json"
        ]
        
        for marker in markers:
            if os.path.exists(marker):
                return True
        
        return False
    
    def check_kill_switch(self) -> bool:
        """
        Check if quantum-x kill switch is armed.
        
        Returns:
            True if operations should continue, False if halted
        """
        if not os.path.exists(self.kill_switch_path):
            # No kill switch file means proceed
            return True
        
        try:
            with open(self.kill_switch_path, 'r') as f:
                kill_switch = json.load(f)
            
            if kill_switch.get("kill_switch") == "ARMED":
                logger.warning("⚠ Kill switch is ARMED - halting operations")
                return False
            
            return True
            
        except Exception as e:
            logger.error(f"Error reading kill switch: {e}")
            # Fail safe: stop on error
            return False
    
    def check_policy_permission(self, action: str) -> bool:
        """
        Check if action is permitted by policy.
        
        Args:
            action: Action to check permission for
        
        Returns:
            True if action is permitted
        """
        if not os.path.exists(self.policy_path):
            # No policy file means use default permissive mode
            logger.warning("No policy file found - using permissive mode")
            return True
        
        try:
            with open(self.policy_path, 'r') as f:
                policy = json.load(f)
            
            # Check if auto-evolution is enabled
            if not policy.get("enabled", True):
                logger.warning(f"Auto-evolution is disabled by policy")
                return False
            
            # Check forbidden actions
            forbidden = policy.get("forbidden_actions", [])
            if action in forbidden:
                logger.warning(f"Action '{action}' is forbidden by policy")
                return False
            
            # Check requires approval
            requires_approval = policy.get("requires_approval", [])
            if action in requires_approval:
                logger.warning(f"Action '{action}' requires approval")
                return False  # TODO: Implement approval workflow
            
            return True
            
        except Exception as e:
            logger.error(f"Error reading policy: {e}")
            # Fail safe: deny on error
            return False
    
    def audit_log(self, action: str, details: Dict[str, Any]):
        """
        Log action to quantum-x audit trail.
        
        Args:
            action: Action being performed
            details: Details to log
        """
        if not os.path.exists(self.audit_path):
            os.makedirs(self.audit_path, exist_ok=True)
        
        try:
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "system": "auto-evolution",
                "action": action,
                "details": details
            }
            
            # Create timestamped log file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = os.path.join(
                self.audit_path,
                f"auto_evolution_{timestamp}.json"
            )
            
            with open(log_file, 'w') as f:
                json.dump(log_entry, f, indent=2)
            
            logger.info(f"✓ Audit logged: {action}")
            
        except Exception as e:
            logger.error(f"Error writing audit log: {e}")
    
    def get_autonomy_level(self) -> str:
        """
        Get current autonomy level from policy.
        
        Returns:
            Autonomy level string
        """
        if not os.path.exists(self.policy_path):
            return "AUTONOMOUS"
        
        try:
            with open(self.policy_path, 'r') as f:
                policy = json.load(f)
            return policy.get("autonomy_level", "SUPERVISED")
        except:
            return "SUPERVISED"


# Global adapter instance
_adapter = None


def get_adapter() -> QuantumXGovernanceAdapter:
    """Get global adapter instance."""
    global _adapter
    if _adapter is None:
        _adapter = QuantumXGovernanceAdapter()
    return _adapter
'''
        
        adapter_path = os.path.join(output_dir, "quantum_x_adapter.py")
        with open(adapter_path, 'w') as f:
            f.write(adapter_code)
        
        logger.info("  ✓ Created quantum_x_adapter.py")
    
    def _create_integration_manifest(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Create integration manifest."""
        return {
            "merge_type": "auto_evolution_into_quantum_x",
            "version": "1.0.0",
            "timestamp": datetime.now().isoformat(),
            "source": {
                "system": "auto-evolution-system",
                "repository": "InfinityXOneSystems/auto-evolution-system",
                "modules": self.python_modules,
                "config_files": self.config_files,
                "documentation": self.doc_files
            },
            "target": {
                "system": "quantum-x-builder",
                "repository": "InfinityXOneSystems/quantum-x-builder",
                "integration_path": analysis.get("suggested_integration_path"),
                "integration_strategy": analysis.get("integration_strategy"),
                "has_ops_directory": analysis.get("has_ops_directory"),
                "has_autonomous_partner": analysis.get("has_autonomous_partner")
            },
            "compatibility": {
                "governance_model": "PAT (Policy-Authority-Truth)",
                "requires_adapter": True,
                "python_version": "3.8+",
                "node_compatibility": "N/A"
            },
            "safety": {
                "kill_switch_integration": True,
                "policy_enforcement": True,
                "audit_logging": True,
                "rollback_available": True
            }
        }
    
    def _create_installation_script(self, analysis: Dict[str, Any]):
        """Create installation script for quantum-x."""
        script = f'''#!/bin/bash
# Auto-Evolution System Installation Script for Quantum-X-Builder
# Generated: {datetime.now().isoformat()}

set -e

echo "========================================================================"
echo "Auto-Evolution System - Quantum-X-Builder Integration"
echo "========================================================================"

# Configuration
QUANTUM_X_ROOT="$1"
INTEGRATION_PATH="{analysis.get('suggested_integration_path', '_OPS/AUTO_EVOLUTION')}"
PACKAGE_DIR="$(pwd)"

if [ -z "$QUANTUM_X_ROOT" ]; then
    echo "Usage: $0 <quantum-x-builder-root>"
    echo "Example: $0 /tmp/quantum-x-builder"
    exit 1
fi

if [ ! -d "$QUANTUM_X_ROOT" ]; then
    echo "Error: Quantum-X root directory not found: $QUANTUM_X_ROOT"
    exit 1
fi

echo "Installing to: $QUANTUM_X_ROOT/$INTEGRATION_PATH"

# Create target directory
TARGET_DIR="$QUANTUM_X_ROOT/$INTEGRATION_PATH"
mkdir -p "$TARGET_DIR"

# Copy modules
echo "Copying Python modules..."
mkdir -p "$TARGET_DIR/modules"
cp -r modules/* "$TARGET_DIR/modules/"

# Copy configuration
echo "Copying configuration files..."
mkdir -p "$TARGET_DIR/config"
cp -r config/* "$TARGET_DIR/config/"

# Copy documentation
echo "Copying documentation..."
mkdir -p "$TARGET_DIR/docs"
cp -r docs/* "$TARGET_DIR/docs/"

# Create policy file if _OPS exists
if [ -d "$QUANTUM_X_ROOT/_OPS/POLICY" ]; then
    echo "Creating auto-evolution policy..."
    cat > "$QUANTUM_X_ROOT/_OPS/POLICY/AUTO_EVOLUTION_POLICY.json" << 'EOF'
{{
  "enabled": true,
  "autonomy_level": "SUPERVISED",
  "allowed_actions": [
    "self_diagnosis",
    "self_cleaning",
    "analysis",
    "recommendations"
  ],
  "forbidden_actions": [
    "file_deletion_outside_temp",
    "dependency_updates_without_approval",
    "policy_modification"
  ],
  "requires_approval": [
    "self_fixing",
    "self_healing",
    "code_modifications"
  ],
  "audit_required": true
}}
EOF
fi

# Set environment variable
echo "Setting QUANTUM_X_NATIVE environment variable..."
echo "export QUANTUM_X_NATIVE=true" >> "$QUANTUM_X_ROOT/.env"

# Install Python dependencies
if [ -f "$TARGET_DIR/config/requirements.txt" ]; then
    echo "Installing Python dependencies..."
    pip install -r "$TARGET_DIR/config/requirements.txt"
fi

echo ""
echo "========================================================================"
echo "✓ Installation Complete!"
echo "========================================================================"
echo "Integration path: $TARGET_DIR"
echo ""
echo "Next steps:"
echo "1. Review the integration documentation in $TARGET_DIR/docs/"
echo "2. Test the installation with: python $TARGET_DIR/modules/autonomous_evolution_main.py --mode status"
echo "3. Update quantum-x SYSTEM_INTEGRATION_MANIFEST.json if needed"
echo ""
'''
        
        script_path = os.path.join(self.output_dir, "install_to_quantum_x.sh")
        with open(script_path, 'w') as f:
            f.write(script)
        
        # Make executable
        os.chmod(script_path, 0o755)
        
        logger.info("  ✓ Created install_to_quantum_x.sh")
    
    def generate_merge_report(self) -> Dict[str, Any]:
        """
        Generate comprehensive merge preparation report.
        
        Returns:
            Dict with full merge report
        """
        logger.info("\n" + "=" * 80)
        logger.info("GENERATING MERGE PREPARATION REPORT")
        logger.info("=" * 80)
        
        # Run all checks
        analysis = self.analyze_quantum_x_structure()
        conflicts = self.check_merge_conflicts()
        package = self.prepare_merge_package()
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "ready_to_merge": (
                analysis.get("success", False) and
                conflicts.get("can_proceed", False) and
                package.get("success", False)
            ),
            "analysis": analysis,
            "conflicts": conflicts,
            "package": package,
            "recommendations": []
        }
        
        # Generate recommendations
        if not analysis.get("success"):
            report["recommendations"].append(
                "Run immediate_quantum_startup.py to clone quantum-x-builder first"
            )
        
        if conflicts.get("severity") in ["high", "critical"]:
            report["recommendations"].append(
                "Resolve high/critical conflicts before proceeding with merge"
            )
        
        if not package.get("success"):
            report["recommendations"].append(
                "Fix package preparation errors before attempting merge"
            )
        
        if report["ready_to_merge"]:
            report["recommendations"].append(
                f"Package ready at: {self.output_dir}"
            )
            report["recommendations"].append(
                f"Run: cd {self.output_dir} && ./install_to_quantum_x.sh <quantum-x-path>"
            )
        
        # Save report
        report_path = os.path.join(self.output_dir, "merge_preparation_report.json")
        os.makedirs(self.output_dir, exist_ok=True)
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info("\n" + "=" * 80)
        logger.info("MERGE PREPARATION REPORT")
        logger.info("=" * 80)
        logger.info(f"Ready to merge: {report['ready_to_merge']}")
        logger.info(f"Conflicts severity: {conflicts.get('severity', 'none')}")
        logger.info(f"Package prepared: {package.get('success', False)}")
        logger.info(f"Report saved to: {report_path}")
        
        if report["recommendations"]:
            logger.info("\nRecommendations:")
            for i, rec in enumerate(report["recommendations"], 1):
                logger.info(f"  {i}. {rec}")
        
        logger.info("=" * 80)
        
        return report


def main():
    """Main entry point for merge preparation."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Prepare auto-evolution-system for merging into quantum-x-builder"
    )
    parser.add_argument(
        "--quantum-x-path",
        default="/tmp/quantum-x-builder",
        help="Path to quantum-x-builder repository"
    )
    parser.add_argument(
        "--output-dir",
        default="/tmp/merge-preparation",
        help="Output directory for merge package"
    )
    
    args = parser.parse_args()
    
    # Create merge preparation instance
    prep = MergePreparation(
        quantum_x_path=args.quantum_x_path,
        output_dir=args.output_dir
    )
    
    # Generate report
    report = prep.generate_merge_report()
    
    # Exit with appropriate code
    sys.exit(0 if report["ready_to_merge"] else 1)


if __name__ == "__main__":
    main()
